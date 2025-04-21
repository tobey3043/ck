# Instructions group project (Day2)

# 🧪 Mini Project: Analyzing Study Habits and Performance

## 🧩 Scenario

You are given a dataset named `student_habits_performance.csv`. Your task is to **analyze the association between hours studied per day and exam score** and create a short, reproducible report using good research software engineering practices.

---

## 📁 Step 1: Create a Project Folder Structure

Organize your project like this:

student-habits-project/
├── data/
│   ├── raw/              # Original dataset goes here (unchanged)
│   └── clean/            # Cleaned/processed data
├── src/                  # Python scripts (e.g., cleaning, analysis, plotting)
├── results/              # Output files like figures or tables
├── report/               # Markdown summary and written interpretation
├── .gitignore            # Files/folders to ignore in version control
├── environment.yml       # Conda environment (optional)
├── README.md             # Project overview and how to run it

> 📌 **Tip**: Never modify the raw data directly. Always save processed data to `data/clean/`.

---

## 🧬 Step 2 : Initialize Version Control with Git

This step is certainly necessary when you work with code, but for this exercise you can skip it if you don't feel comfortable. enough with git.

1. Open your terminal:
   ```bash
   cd student-habits-project
   git init

## Create a README.md for your project.



# Ignore raw data and system files
create a .gitignore file. 

Make sure that the .gitignore ignores the data folder and system files (they might vary from machine to machine).

An example could look like:
data/raw/
__pycache__/
*.pyc
.venv/
.DS_Store


# Commit your code regularly with meaningful messages
git add .
git commit -m "Initial commit: project structure"

## Step 3: Clean the Data
	•	Create src/clean_data.py. This file should contain ONE function.
	•	Load the dataset from data/raw/student_habits_performance.csv
	•	Handle missing values or incorrect entries. For example, drop all rows with Nans in it.
	•	Save the cleaned version to data/clean/cleaned_data.csv

💡 Use clear function names and docstrings to describe your process.

📊 Step 4: Analyze Gender Differences
	•	Create src/analyze.py
	•	Use pandas to compare study habits between men and women:
	•	Study hours
	•	Focus levels
	•	Scores or performance

Write one function per analysis step.

🖼️ Step 5: Create a Plot
	•	Use matplotlib or seaborn
	•	Save your figure to results/study_habits_by_gender.png
	•	Include axis labels, a title, and a legend if needed

✍️ Add a docstring to your plotting function and comment the main steps (e.g., load data, create figure, save figure).

📝 Step 6: Write a Summary Report

Create a file:
report/gender_differences_summary.md

Write your report in markdown. Link your figure into the report. (can be very short, but make sure to link the figure)

⚙️ Step 7:  Document your environment. 

Create a Conda Environment or a venv
	1.	Create an environment.yml file:

name: student-env
dependencies:
  - python=3.11
  - pandas
  - matplotlib
  - seaborn

conda env create -f environment.yml
conda activate student-env

   2. Create a venv requirement.txt

✅ Step 8: Final Checklist
	•	Project uses a clean and modular folder structure
	•	Raw data is preserved and not modified
	•	All code is annotated with comments and has proper docstrings
	•	Scripts are organized in src/ and functions are clearly named
	•	Git tracks your changes with meaningful commit messages
	•	Raw data is excluded from version control using .gitignore
	•	A figure is saved to results/ with labels and titles
	•	A short Markdown summary is written in report/