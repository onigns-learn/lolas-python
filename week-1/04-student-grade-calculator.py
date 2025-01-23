
students_names = ["Alice", "Bob", "Charlie", "Lola", "John", "Abdul"]
total_score = [0 for x in range(0, len(students_names))]
average_score = [0 for x in range(0, len(students_names))]

# Ask the user to input scores for each student
# range(0, 3) ===== [0, 1, 2]
for ind in range(0, len(students_names)):
    student = students_names[ind]

    print(f"Enter the scores for {student}:")
    math = int(input("Math: "))
    science = int(input("Science: "))
    english = int(input("English: "))

    total_score[ind] = math + science + english
    average_score[ind] = total_score[ind] / 3

  #  [student] = [math, science, english]

for ind in range(0, len(students_names)):
    print(f'Student: {students_names[ind]}')
    print(f'Total Socre: {total_score[ind]}')
    print(f'Average Score: {average_score[ind]}')
    print('')