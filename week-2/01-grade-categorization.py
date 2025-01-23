
students = ["Alice", "Bob", "Charlie", "Diana"]
grades = [85, 92, 78, 90]

for i in range(0, len(students)):
    comment = ''

    if grades[i] >= 90:
        comment = 'Excellent'
    elif grades[i] <= 89 and grades[i] >= 80:
        comment = "Extra Good"
    elif grades[i] <= 79 and grades[i] >=70:
        comment = "Very Good"
    elif grades[i] <= 69 and grades[i] >= 60:
        comment = "Good"
    else:
        comment = 'Needs Improvement'

    print(f'{students[i]}: Grade = {grades[i]}. Category = {comment}.')
