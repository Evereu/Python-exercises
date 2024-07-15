class Student:

    def __init__(self, name, last_name):
        self.grade_list = []
        self.name = name
        self.last_name = last_name

    def avg_grade(self):
        if len(self.grade_list) == 0:
            return 0
        else:
            return sum(self.grade_list) / len(self.grade_list)

    def add_grade(self, grade):
        self.grade_list.append(grade)

    def __add__(self, other):
        return self.grade_list.append(other)

    def __str__(self):
        return f"Student: {self.name} {self.last_name}, średnia ocen: {self.avg_grade()}"


student = Student("Jan", "Kowalski")
student.add_grade(2.5)
student.add_grade(4.0)
print(student)

student + 5.0
print(student)
