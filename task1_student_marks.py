# Task 1: Create a Dictionary of Student Marks

# Sample dictionary with student names and their marks
student_marks = {
    "Arjun": 85,
    "Priya": 92,
    "Ravi": 76,
    "Neha": 88,
    "Aman": 67
}

# Ask user to input student name
name = input("Enter student name: ")

# Retrieve and display marks
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the records.")
