 
<div align="center">

# 📊 Survey Feedback Analyzer

### *A Python-Based Text Feedback Cleaning and Insights Project*

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Project-Data%20Analysis-purple?style=for-the-badge" alt="Data Analysis"/>
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge" alt="Project Status"/>
</p>

</div>

---

## 📝 Project Overview

The **Survey Feedback Analyzer** is a Python project designed to analyze customer survey feedback and extract useful insights from text data.

The project uses a dictionary of lists to store survey responses, cleans text feedback, counts specific words, calculates average ratings, identifies the longest comment, and extracts unique words.

It demonstrates fundamental Python programming concepts used in data analysis, including loops, conditional statements, functions, string manipulation, lists, dictionaries, sets, and sorting.

---

## 🎯 Problem Statement

In data-driven domains, analyzing textual feedback is essential for understanding customer experiences, identifying service issues, and improving service quality.

This project develops a simple feedback analysis tool that processes survey responses and ratings to generate meaningful summaries and word-level insights.

---

## 🛠️ Technologies Used

<div align="center">

| Technology | Purpose |
|:---:|---|
| 🐍 Python | Core programming language |
| Lists & Dictionaries | Store survey data |
| Loops & Conditions | Process and analyze feedback |
| String Methods | Clean text data |
| User-Defined Functions | Count feedback containing specific words |
| Sets | Identify unique words |
| `zip()` & `sorted()` | Sort feedback by rating |

</div>

---

## 📌 Project Objectives

<div style="background-color:#EAF2F8; color:#1B2631; padding:16px; border-radius:10px;">

- Store survey responses in a structured dictionary.
- Allow users to add new feedback entries.
- Validate ratings between 1 and 5.
- Clean text by removing specified punctuation and extra spaces.
- Count feedback entries containing selected words.
- Calculate the average survey rating.
- Identify the feedback with the longest comment.
- Extract unique words from all feedback entries.
- Sort feedback entries by rating in descending order.

</div>

---

## ⚙️ Project Implementation

### 📥 Step 1: Preloaded Feedbacks

- Created a dictionary named `feedback_data`.
- Stored serial numbers, names, feedback comments, and ratings.
- Initialized the dataset with 10 feedback entries.

### ✍️ Step 2: Add More Feedbacks

- Asked the user how many new feedback entries to add.
- Collected the name, written feedback, and rating.
- Validated ratings to ensure they are between 1 and 5.
- Generated serial numbers automatically.
- Appended the new entries to the dictionary.

### 🧹 Step 3: Text Cleaning

Applied the following cleaning operations:

- Removed `.`, `,`, `!`, and `?`.
- Removed leading and trailing spaces.
- Replaced multiple spaces with a single space.
- Converted feedback text to lowercase.

### 🔁 Step 4: Word Count Insights

Created the function `count_word_in_feedbacks(word)` to count how many feedback entries contain a specified word.

The function analyzes these words:

- `good`
- `poor`
- `excellent`

### 📊 Step 5: Final Summary and Insights

The program generates the following results:

- Final cleaned feedback dictionary.
- Total number of feedback entries.
- Average rating.
- Longest feedback comment and its word count.
- List of unique words used across all feedback.
- Feedback entries sorted by rating from highest to lowest.

---

## 🧠 Python Concepts Practiced

<div align="center">

<img src="https://img.shields.io/badge/Variables-3776AB?style=flat-square" alt="Variables"/>
<img src="https://img.shields.io/badge/Lists%20%26%20Dictionaries-3776AB?style=flat-square" alt="Lists and Dictionaries"/>
<img src="https://img.shields.io/badge/For%20Loops-6A5ACD?style=flat-square" alt="For Loops"/>
<img src="https://img.shields.io/badge/While%20Loops-6A5ACD?style=flat-square" alt="While Loops"/>
<img src="https://img.shields.io/badge/Functions-008080?style=flat-square" alt="Functions"/>
<img src="https://img.shields.io/badge/String%20Methods-E67E22?style=flat-square" alt="String Methods"/>
<img src="https://img.shields.io/badge/Sets-16A085?style=flat-square" alt="Sets"/>
<img src="https://img.shields.io/badge/Sorting-8E44AD?style=flat-square" alt="Sorting"/>

</div>

---

## ▶️ How to Run the Project

**Prerequisites:** Python 3 installed on your system.

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Open the project folder.

```bash
cd Survey-Feedback-Analyzer
```

**Step 3:** Run the Python program.

```bash
python survey_feedback_analyzer.py
```

**Step 4:** Enter the requested inputs, including the number of new feedback entries, names, comments, and ratings.

**Note:** Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL and use the actual Python filename if it differs.

---

## 📂 Project Structure

```text
Survey-Feedback-Analyzer/
│
├── Data.py
└── README.md
```

---

## 🌟 Key Learning Outcomes

<div style="background-color:#E8F8F5; color:#145A32; padding:16px; border-radius:10px;">

- Practiced core Python programming through a practical project.
- Learned to clean and standardize text data.
- Applied functions to reusable feedback analysis.
- Used lists, dictionaries, and sets to manage data.
- Extracted basic insights from customer comments and ratings.
- Practiced sorting structured data using Python built-in functions.

</div>

---

## 🔮 Future Improvements

- Export cleaned feedback to CSV or Excel.
- Visualize rating distributions using charts.
- Add sentiment classification for positive and negative feedback.
- Build an interactive dashboard for survey insights.

---

<div align="center">

### 💡 Turning Text Feedback into Meaningful Insights

*Built with Python as a hands-on data analysis learning project.*

</div>
