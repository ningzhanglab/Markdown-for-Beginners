# Practice Exercises

Short tasks to build the habit. For each one:

1. Type your answer in the practice editor on the website, or in any Markdown editor with a preview.
2. Check how it looks.
3. Open **Show a solution** and compare. Yours does not have to match word for word.

If you are stuck on a symbol, keep the Simple Cheat Sheet open.

## Exercise 1: Headings

Write a title called **My Reading List** and two smaller section headings called **Books** and **Articles**.

<details>
<summary>Show a solution</summary>

```markdown
# My Reading List

## Books

## Articles
```

</details>

## Exercise 2: Bold and italic

Write the sentence "Markdown is simple" so that the word **simple** is bold, and add a second sentence where the words *plain text* are italic.

<details>
<summary>Show a solution</summary>

```markdown
Markdown is **simple**.

I can write it in *plain text*.
```

</details>

## Exercise 3: Lists

Make a bullet list of three things you would buy at a shop. Then make a numbered list of three steps for making tea.

<details>
<summary>Show a solution</summary>

```markdown
- Bread
- Milk
- Apples

1. Boil the water.
2. Add the tea.
3. Wait three minutes.
```

</details>

## Exercise 4: Checkboxes

Write a to-do list with three tasks, where the first one is already done.

<details>
<summary>Show a solution</summary>

```markdown
- [x] Answer the email
- [ ] Do the laundry
- [ ] Call a friend
```

</details>

## Exercise 5: Links and code

Write a sentence with a link to GitHub, and another sentence that shows the file name `notes.md` in code style.

<details>
<summary>Show a solution</summary>

```markdown
Visit [GitHub](https://github.com/) to see more projects.

Save your work in `notes.md`.
```

</details>

## Exercise 6: A small table

Make a table with two columns, **Fruit** and **Colour**, and three rows.

<details>
<summary>Show a solution</summary>

````markdown
| Fruit | Colour |
|---|---|
| Banana | Yellow |
| Apple | Red |
| Plum | Purple |
````

</details>

## Exercise 7: A code block

Show this one line of Python as a code block: `print("Hello")`

<details>
<summary>Show a solution</summary>

````markdown
```python
print("Hello")
```
````

</details>

## Exercise 8: Math (if your tool supports it)

Write the equation E = mc² as display math, using `^` for the power.

<details>
<summary>Show a solution</summary>

```markdown
$$
E = mc^2
$$
```

If you see the dollar signs instead of an equation, your viewer does not support math.

</details>

## Exercise 9: Fix the broken note

This note has five small mistakes. Find and fix them.

````markdown
##My Notes

This is the first idea.
This is the second idea.

** Important: ** check the file `notes.md.

![Chart](/Users/me/Desktop/chart.png)
````

<details>
<summary>Show the mistakes and a solution</summary>

1. `##My Notes` needs a space after the `#` signs.
2. The two ideas need a blank line between them, or they run together.
3. `** Important: **` must not have spaces just inside the stars.
4. The backtick after `notes.md` was never closed.
5. The image path points to one computer. Use a path relative to the note.

````markdown
## My Notes

This is the first idea.

This is the second idea.

**Important:** check the file `notes.md`.

![Chart](figures/chart.png)
````

</details>

## Exercise 10: Put it together

Write a short note called **Weekend Plan** with a heading, a paragraph, a checklist, one bold word, and one link. Choose your own content.

<details>
<summary>Show an example</summary>

```markdown
# Weekend Plan

I want a **relaxed** weekend this time.

- [ ] Go for a walk
- [ ] Read a chapter
- [ ] Try a new recipe from [this site](https://example.com)
```

</details>
