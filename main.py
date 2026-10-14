from functions import (
    load_student_data,
    process_student_metrics,
    analyze_subject_performance,
    get_overall_summary,
    get_top_performers
)


def main():
    print("=" * 85)
    print("                 STUDENT PERFORMANCE ANALYTICS SYSTEM                 ")
    print("=" * 85)

    # Step 1 & 2: Load and inspect dataset
    filepath = "students.csv"
    df = load_student_data(filepath)

    print(f"\n[1] DATASET OVERVIEW")
    print(f"Total Student Records Loaded : {df.shape[0]}")
    print(f"Total Attributes/Columns     : {df.shape[1]}")
    print(f"Columns                      : {', '.join(df.columns)}")

    # Step 3: Process totals, averages, grades, and pass/fail status
    df = process_student_metrics(df)

    print("\n" + "-" * 85)
    print("[2] COMPLETE STUDENT PERFORMANCE REPORT")
    print("-" * 85)
    display_cols = [
        'Student_ID', 'Name', 'Department',
        'Total_Marks', 'Average_Marks', 'Attendance', 'Grade', 'Status'
    ]
    print(df[display_cols].to_string(index=False))

    # Step 4: Overall Class Summary & Key Questions
    summary = get_overall_summary(df)
    subject_df = analyze_subject_performance(df)
    best_subject_row = subject_df.loc[subject_df['Average'].idxmax()]

    print("\n" + "-" * 85)
    print("[3] OVERALL CLASS PERFORMANCE & PRACTICAL QUESTIONS")
    print("-" * 85)
    print(f"• Overall Class Average      : {summary['class_average']}%")
    print(f"• Highest Scoring Student    : {summary['highest_student']} ({summary['highest_student_id']}) with {summary['highest_avg']}%")
    print(f"• Lowest Scoring Student     : {summary['lowest_student']} ({summary['lowest_student_id']}) with {summary['lowest_avg']}%")
    print(f"• Best Performing Subject    : {best_subject_row['Subject']} (Average: {best_subject_row['Average']})")
    print(f"• Pass / Fail Breakdown      : {summary['pass_count']} Passed | {summary['fail_count']} Failed ({summary['pass_percentage']}% Pass Rate)")

    # Subject-wise Breakdown
    print("\n" + "-" * 85)
    print("[4] SUBJECT-WISE PERFORMANCE ANALYSIS")
    print("-" * 85)
    print(subject_df.to_string(index=False))

    # Top 5 Performers
    top_students = get_top_performers(df, top_n=5)
    print("\n" + "-" * 85)
    print("[5] TOP 5 PERFORMING STUDENTS")
    print("-" * 85)
    top_cols = ['Student_ID', 'Name', 'Department', 'Total_Marks', 'Average_Marks', 'Grade']
    print(top_students[top_cols].to_string(index=False))

    # Grade & Department Distribution
    print("\n" + "-" * 85)
    print("[6] DEPARTMENT-WISE AVERAGE PERFORMANCE")
    print("-" * 85)
    dept_summary = df.groupby('Department')[['Total_Marks', 'Average_Marks', 'Attendance']].mean().round(2)
    print(dept_summary.to_string())

    print("\n" + "=" * 85)
    print("Analysis Complete! Processed records saved to 'processed_student_results.csv'.")
    print("=" * 85)

    # Export processed results for verification
    df.to_csv("processed_student_results.csv", index=False)


if __name__ == "__main__":
    main()