import time


class School:
    def __init__(self, name, address, school_type, principal=""):
        self.name = name,
        self.address = address,
        self.principal = principal,
        self.type = school_type
        self.grades = []

    def add_class(self, name, teacher):
        new_class = Class(name, teacher)
        self.grades.append(new_class)

    def remove_class(self, name):
        id = 0
        for i, grade in enumerate(self.grades):
            if grade.name == name:
                idx = i
            del self.grades[id]



class Class:
    def __init__(self, name, teacher):
        self.students = [],
        self.name = name,
        self.teacher = teacher

    def __repr__(self) -> str:
        return f'{self.name} of Teacher is {self.teacher}'

    def __del__(self):
        return f'Deleting {self.name} of Teacher is {self.teacher}'


school_1 = School("Milon Academy", "Chandora,Gazipur", "KinderGarden", "Rofiqul Islam Rupa Master")
school_1.add_class("Class 5", "Anichul Islam")
# school_1.remove_class("Class 5")

print(school_1.name)
print(school_1.grades)
time.sleep(10)
