def average (grades):
    aver = sum(grades) / len(grades)
    print(f"average of student grades: {aver}")


my_students = {
    'name': 'Herabor',
    'grades': [70, 70, 90, 90]
}


average(my_students['grades'])