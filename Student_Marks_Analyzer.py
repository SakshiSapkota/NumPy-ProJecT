import numpy as np
Subjects = ["Math", "Science", "English", "Computer"]
# Rows = Students, Columns = Subjects
marks = np.array([
    [88, 92, 79, 93],   # Student 1
    [76, 85, 83, 89],   # Student 2
    [91, 90, 77, 95],   # Student 3
    [70, 65, 80, 72],   # Student 4
    [94, 98, 90, 99]    # Student 5
])
total_per_student = np.sum(marks, axis=1)
average_per_student = np.mean(marks, axis=1)
highest_score = np.max(total_per_student)
lowest_score = np.min(total_per_student)
top_student_index = np.argmax(total_per_student)
students = ["S1", "S2", "S3", "S4", "S5"]

print("Report Card:")
print("Student  |  Total  |  Average")
print("-" * 30)

for i in range(len(students)):
    print(f"{students[i]:<8} |  {total_per_student[i]:<6} |  {average_per_student[i]:.2f}")

print("\nTop Scorer:", students[top_student_index])
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
