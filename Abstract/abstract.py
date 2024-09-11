import abc

from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age, weight, address, nationality):
        self.name = name,
        self.age = age,
        self.weight = weight,
        self.address = address,
        self.nationality = nationality

    @abstractmethod
    def profession(self):
        print("are you student or doing job?")

    def family(self):
        pass


class Ibrahim(Human):

    def profession(self):
        pass
    def family(self):
        pass


student = Ibrahim("Ibrahim",25,80,'keraniganj',"Bangladeshi")
print(student.name)
