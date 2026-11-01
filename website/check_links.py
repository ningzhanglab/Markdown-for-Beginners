#!/usr/bin/env python3
"""Check the external (http/https) links written in this repository's Markdown files.

    python website/check_links.py            # check every link
    python website/check_links.py --timeout 30

What counts as a problem:
  FAIL  404, 410, or a host that cannot be found. These are really broken; the run fails.
  WARN  403, 429, timeouts, server errors. Many sites refuse automated requests or are
        briefly down, so these are listed but do not fail the run.

Links inside code blocks and example addresses (example.com and friends) are skipped,
because they are teaching examples, not real destinations.
Only the Python standard library is used.
"""
import argparse
import concurrent.futures as cf
import os
import re
import socket
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "_docs", "_site", "node_modules"}
EXAMPLE_HOSTS = ("example.com", "example.org", "example.net", "example.edu")
UA = "Mozilla/5.0 (compatible; markdown-for-beginners-linkcheck/1.0)"

URL_RE = re.compile(r"https?://[^\s<>\")\]]+")


def strip_trailing(url):
    return url.rstrip(".,;:!?*'`")


def collect(root, include_local=False):
    """Return {url: [file, ...]} for links found outside fenced code and inline code."""
    found = {}
    for folder, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if not name.endswith(".md"):
                continue
            path = os.path.join(folder, name)
            fence = None
            with open(path, encoding="utf-8") as f:
                for line in f:
                    m = re.match(r"^\s*(`{3,}|~{3,})", line)
                    if fence is None and m:
                        fence = m.group(1)
                        continue
                    if fence is not None:
                        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
                            fence = None
                        continue
                    line = re.sub(r"`[^`]*`", "", line)
                    for raw in URL_RE.findall(line):
                        url = strip_trailing(raw)
                        host = (urlparse(url).hostname or "").lower()
                        if not host or "..." in url:
                            continue
                        if host.endswith(EXAMPLE_HOSTS) and not include_local:
                            continue
                        if host in ("localhost", "127.0.0.1", "::1") and not include_local:
                            continue
                        found.setdefault(url, []).append(os.path.relpath(path, root))
    return found


def check(url, timeout):
    """Return (level, detail) where level is OK, WARN or FAIL."""
    last = ("WARN", "no response")
    for attempt in range(2):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return "OK", str(resp.status)
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return "FAIL", f"HTTP {e.code}"
            last = ("WARN", f"HTTP {e.code}")
            if e.code in (403, 429, 999):
                return last  # bot protection; retrying will not help
        except urllib.error.URLError as e:
            reason = e.reason
            if isinstance(reason, socket.gaierror):
                return "FAIL", "host not found"
            last = ("WARN", f"{type(reason).__name__}: {reason}")
        except (socket.timeout, TimeoutError):
            last = ("WARN", "timed out")
        except Exception as e:  # keep one odd link from stopping the whole run
            last = ("WARN", f"{type(e).__name__}: {e}")
    return last


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=ROOT, help="folder to scan (default: the repository)")
    ap.add_argument("--timeout", type=float, default=20)
    ap.add_argument("--include-local", action="store_true", help="also check localhost and example.* (for testing)")
    args = ap.parse_args()

    links = collect(args.root, args.include_local)
    print(f"Checking {len(links)} external links...\n")
    results = {}
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        futures = {pool.submit(check, u, args.timeout): u for u in links}
        for fut in cf.as_completed(futures):
            results[futures[fut]] = fut.result()

    fails = warns = 0
    lines = []
    for url in sorted(results):
        level, detail = results[url]
        if level == "OK":
            continue
        fails += level == "FAIL"
        warns += level == "WARN"
        lines.append(f"{level}  {detail:<22} {url}\n      in: {', '.join(sorted(set(links[url])))}")
    print("\n".join(lines) if lines else "All links responded.")
    print(f"\n{len(links) - fails - warns} ok, {warns} warnings, {fails} broken")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as f:
            f.write(f"### Link check\n\n{len(links) - fails - warns} ok, {warns} warnings, {fails} broken\n\n")
            if lines:
                f.write("```\n" + "\n".join(lines) + "\n```\n")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
