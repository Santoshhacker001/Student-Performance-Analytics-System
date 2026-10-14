import numpy as np
import pandas as pd

SUBJECT_COLS = ['Python_Marks', 'Data_Analytics_Marks', 'AI_Marks', 'DBMS_Marks']


def load_student_data(filepath):
    """Loads the CSV dataset into a Pandas DataFrame."""
    return pd.read_csv(filepath)


def assign_grade(avg_marks):
    """Assigns a letter grade based on average marks."""
    if avg_marks >= 90:
        return 'A+'
    elif avg_marks >= 80:
        return 'A'
    elif avg_marks >= 70:
        return 'B'
    elif avg_marks >= 60:
        return 'C'
    elif avg_marks >= 50:
        return 'D'
    else:
        return 'F'


def determine_pass_fail(row):
    """
    Determines Pass/Fail status.
    Rule: Student must have Average_Marks >= 50, at least 35 marks in every individual subject,
    and Attendance >= 70%.
    """
    min_subject_score = np.min([row[col] for col in SUBJECT_COLS])
    if row['Average_Marks'] >= 50 and min_subject_score >= 35 and row['Attendance'] >= 70:
        return 'Pass'
    return 'Fail'


def process_student_metrics(df):
    """
    Uses NumPy operations, loops, and reusable functions to calculate total marks,
    average marks, grades, and pass/fail status for each student.
    """
    # Extract 2D NumPy array of subject marks
    marks_matrix = df[SUBJECT_COLS].to_numpy()

    # NumPy vectorized calculations across columns (axis=1)
    df['Total_Marks'] = np.sum(marks_matrix, axis=1)
    df['Average_Marks'] = np.round(np.mean(marks_matrix, axis=1), 2)

    # Use explicit loop as required by guidelines to assign grades and status
    grades = []
    statuses = []

    for index, row in df.iterrows():
        grades.append(assign_grade(row['Average_Marks']))
        statuses.append(determine_pass_fail(row))

    df['Grade'] = grades
    df['Status'] = statuses

    return df


def analyze_subject_performance(df):
    """
    Iterates through subjects using a loop and computes highest, lowest,
    average, and pass percentage using NumPy.
    """
    subject_stats = []

    for subject in SUBJECT_COLS:
        scores = df[subject].to_numpy()
        clean_name = subject.replace('_Marks', '').replace('_', ' ')

        subject_stats.append({
            'Subject': clean_name,
            'Average': np.round(np.mean(scores), 2),
            'Highest': np.max(scores),
            'Lowest': np.min(scores),
            'Std_Dev': np.round(np.std(scores), 2),
            'Subject_Pass_%': np.round((np.sum(scores >= 35) / len(scores)) * 100, 1)
        })

    return pd.DataFrame(subject_stats)


def get_overall_summary(df):
    """Computes class-level performance statistics using NumPy and Pandas."""
    avg_array = df['Average_Marks'].to_numpy()
    best_idx = np.argmax(avg_array)
    lowest_idx = np.argmin(avg_array)

    pass_count = int((df['Status'] == 'Pass').sum())
    fail_count = int((df['Status'] == 'Fail').sum())
    total_students = len(df)

    return {
        'total_students': total_students,
        'class_average': np.round(np.mean(avg_array), 2),
        'highest_avg': np.max(avg_array),
        'highest_student': df.loc[best_idx, 'Name'],
        'highest_student_id': df.loc[best_idx, 'Student_ID'],
        'lowest_avg': np.min(avg_array),
        'lowest_student': df.loc[lowest_idx, 'Name'],
        'lowest_student_id': df.loc[lowest_idx, 'Student_ID'],
        'pass_count': pass_count,
        'fail_count': fail_count,
        'pass_percentage': np.round((pass_count / total_students) * 100, 2)
    }


def get_top_performers(df, top_n=5):
    """Filters and sorts the DataFrame to return the top N performing students."""
    return df.sort_values(by='Total_Marks', ascending=False).head(top_n)