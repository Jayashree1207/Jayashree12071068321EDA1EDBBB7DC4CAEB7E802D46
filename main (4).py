class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return "{} has a grade of {}".format(self.name, self.grade)



students_list = []

x = int(input("How many students are there? "))

while x != 0:
    name = input("Enter the name: ")
    grade = input("Enter the grade: ")
    students_list.append(Student(name, grade))
    x-=1

for i in students_list:
    print(i)
