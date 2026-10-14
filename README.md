# 1. Project Title
**Student Performance Analytics System**  
* **Author:** Santosh Kumar Sharma  
* **Course:** EWB Courses – Python with AI  
* **Submission Date:** October 2026  

---

## 2. Objective
The objective of the **Student Performance Analytics System** is to automate the evaluation and statistical analysis of academic records using Python, NumPy, and Pandas. Manually calculating totals, averages, grades, attendance compliance, and subject-level benchmarks across multiple students is error-prone and time-consuming. This project solves that problem by providing a clean, modular data analysis pipeline that ingests raw CSV records and outputs actionable academic insights.

---

## 3. Technologies Used
* **Python 3.x** (Core programming language, functions, loops, conditional logic)
* **NumPy** (Vectorized numerical calculations: sum, mean, min, max, argmax, argmin, standard deviation)
* **Pandas** (DataFrame ingestion, manipulation, grouping, sorting, and tabular reporting)
* **Git & GitHub** (Version control and project hosting)

---

## 4. Dataset Description
The dataset (`students.csv`) contains **20 realistic student records** across multiple engineering departments (`CSE`, `CSE (AI & DS)`, `IT`, `ECE`).
* **`Student_ID`**: Unique identifier for each student (`S101` to `S120`).
* **`Name`**: Full name of the student.
* **`Department`**: Academic department.
* **`Python_Marks`**, **`Data_Analytics_Marks`**, **`AI_Marks`**, **`DBMS_Marks`**: Marks obtained out of 100 in four core subjects.
* **`Attendance`**: Overall semester attendance percentage.

---

## 5. Implementation
1. **Data Loading**: `load_student_data()` reads `students.csv` into a Pandas DataFrame and validates record counts and schema.
2. **Numerical Processing with NumPy**: `process_student_metrics()` extracts a 2D NumPy matrix of subject scores to compute row-wise `Total_Marks` (`np.sum`) and `Average_Marks` (`np.mean`).
3. **Rule Evaluation via Loops & Functions**: Loops iterate through student records to apply `assign_grade()` (grading scale `A+` to `F`) and `determine_pass_fail()` (requiring average >= 50, minimum 35 in each subject, and attendance >= 70%).
4. **Subject & Class Aggregations**: `analyze_subject_performance()` loops over each subject column to compute mean, max, min, standard deviation, and subject pass percentage. `get_overall_summary()` and `get_top_performers()` identify class leaders and departmental averages.
5. **Output & Export**: `main.py` formats the analysis into readable console tables and exports the enriched dataset to `processed_student_results.csv`.

---

## 6. Key Features
* Automated calculation of student total and average marks using NumPy arrays.
* Custom multi-tier grading system (`A+`, `A`, `B`, `C`, `D`, `F`).
* Multi-condition Pass/Fail verification combining overall average, subject minimums, and attendance thresholds.
* Subject-wise statistical breakdown (Average, Highest, Lowest, Standard Deviation, Pass Rate).
* Identification of Top 5 performers and department-wise performance grouping.
* Automated CSV export of processed results (`processed_student_results.csv`).

---

## 7. Output / Screenshots
Run the program using:
```bash
python main.py