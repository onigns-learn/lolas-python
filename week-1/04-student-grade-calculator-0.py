
students_names = ["Alice", "Bob", "Charlie"]
math_scores = [0,0,0]
science_score = [0,0,0]
english_scores = [0,0,0]


# Ask the user to input scores for each student
# range(0, 3) ===== [0, 1, 2]
for ind in range(0, len(students_names)):
    student = students_names[ind]

    print(f"Enter the scores for {student}:")
    math = int(input("Math: "))
    science = int(input("Science: "))
    english = int(input("English: "))

    math_scores[ind] = math
    science_score[ind] = science
    english_scores[ind] = english
    

  #  [student] = [math, science, english]

total_score = [0,0,0]
average_score = [0,0,0]

for ind in range(0, len(students_names)):
    total_score[ind] = math_scores[ind] + english_scores[ind] + science_score[ind]
    average_score[ind] = total_score[ind] / 3


for ind in range(0, len(students_names)):
    print(f'Student: {students_names[ind]}')
    print(f'Total Socre: {total_score[ind]}')
    print(f'Average Score: {average_score[ind]}')
    print('')