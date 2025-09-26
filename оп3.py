students = []

while True:
    name = input("Введіть ім'я студента: ")
    if name == "stop":
        break
    grade = input("Введіть оцінку студента: ")
    if grade == "stop":
        break

    try:
       grade = int(grade)
    except ValueError:
       print("Оцінка повинна бути числом!")
       continue

    students.append({"name": name, "grade": grade})

print("Список студентів:")
for student in students:
    print(f"{student['name']} - {student['grade']}")

avg = sum(student["grade"] for student in students) / len(students)

print(f"Середня оцінка: {avg}")

excellent = []
for student in students:
    if student['grade'] >=10 and student['grade'] <=12:
       excellent.append(student)

print(f"Відмінники: {len(excellent)}")
for student in excellent:
    print(f"{student['name']} - {student['grade']}")

well = []
for student in students:
    if student['grade'] >= 7 and student['grade'] <= 9:
        well.append(student)

print(f"Добрі студенти: {len(well)}")
for student in well:
    print(f"{student['name']} - {student['grade']}")

notbad = []
for student in students:
    if student['grade'] >=4 and student['grade'] <=6:
       notbad.append(student)

print(f"Середні студенти: {len(notbad)}")
for student in notbad:
    print(f"{student['name']} - {student['grade']}")

unsubmitted = []
for student in students:
    if student['grade'] >=1 and student['grade'] <=3:
       unsubmitted.append(student)

print(f"Студенти з низькими оцінками: {len(unsubmitted)}")
for student in unsubmitted:
    print(f"{student['name']} - {student['grade']}")
