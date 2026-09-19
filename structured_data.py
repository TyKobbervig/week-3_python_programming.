import csv

# List to store student records
students = []

# Read data from CSV file
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append({
            "Name": row["Name"],
            "Grade": int(row["Grade"])
        })

# Display all students
print("Student Grades:")
for student in students:
    print(f"{student['Name']}: {student['Grade']}")

# Find average grade
total = sum(student["Grade"] for student in students)
average = total / len(students)

print(f"\nAverage Grade: {average:.2f}")

# Filter students with grades 80 or higher
print("\nStudents with grades 80 or higher:")
for student in students:
    if student["Grade"] >= 80:
        print(student["Name"])