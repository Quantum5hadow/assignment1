#sandeep
student_number = int(input("Enter student number: "))
student_name = input("Enter student name: ")
marks_subject1 = float(input("Enter marks for subject 1: "))
marks_subject2 = float(input("Enter marks for subject 2: "))
marks_subject3 = float(input("Enter marks for subject 3: "))

total_marks = marks_subject1 + marks_subject2 + marks_subject3

average_marks = total_marks / 3

if average_marks > 75:
    result = "Distinction"
elif average_marks > 60:
    result = "First Class"
elif average_marks > 50:
    result = "Second Class"
elif average_marks > 35:
    result = "Third Class"
else:
    result = "Fail"

print("Student Number:", student_number)
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Result:", result)
