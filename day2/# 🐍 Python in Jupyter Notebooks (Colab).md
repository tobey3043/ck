# 🐍 Python in Jupyter Notebooks (Colab) Cheat Sheet


A fantastic introduction to Google Colab can be found [here](https://colab.research.google.com/)

📄 1. Code Cells vs Text (Markdown) Cells
- Code Cell → Write and run Python code.
- Text (Markdown) Cell → Write formatted notes, headings, lists, links, images.

👉 Shortcut to change cell type:
- Ctrl + M + Y = Code Cell
- Ctrl + M + M = Text/Markdown Cell


🚀 2. Running Code
	- Run the current cell:
Shift + Enter
	•	Run and insert a new cell below:
Alt + Enter
	•	Run all cells:
From menu: Runtime → Run all

📁 3. Editing Files in Colab
	•	Click files in the File viewer to open and edit.
	•	Edits are saved automatically in the Colab editor.
	•	If Colab opens a Git window on save, you can:
	•	Accept to commit changes to GitHub, or
	•	Close the window to skip committing.

4. Write bash functions in Colab

Bash functions can be run in Colab using the `!` symbol

Basic bas functions:

`! pwd` : print the current working directory
`! cd mydir`:  move into directory `mydir`
`! cd ..` : move one directory up
`! mkdir mydir` : create a directory `mdir`
`! touch myfile` : create a file `myfile`
`! rm myfile`: delete the file `myfile`
`! rm -r mydir` : delete the directory `mydir`


🛠️ 5. Basic Python Syntax

# Variables

```python
name = "Alice"
score = 95

# Functions
def greet(name):
    return f"Hello, {name}!"

# If statements
if score > 90:
    print("Excellent!")

# Loops
for i in range(5):
    print(i)

````


