def sum(num1, num2, num3):
    return num1 + num2 + num3


user_input = input("insert 2 value ").split("-")
num1 = float(user_input[0])
num2 = float(user_input[1])
num3 = float(user_input[2])

result = sum(num1, num2, num3)
print(f"sum is ", result)

S = "Programming Hero is the best"

words = S.split()
reverse_words = []
for word in words:
    reverse_word = word[::-1]
    reverse_words.append(reverse_word)
print(reverse_words)

s = "x3b4U5i2"

expanded_chars = []

for i in range(0, len(s), 2):
    char = s[i]
    count = int(s[i + 1])
    expanded_chars.extend([char] * count)
print(expanded_chars)
expanded_chars.sort()
sorted_string = ''.join(expanded_chars)
print(sorted_string)

import os
import json


def generate_student_id(filename):
    """Generate a unique student ID based on the existing file."""
    if not os.path.exists(filename):
        return 1
    with open(filename, 'r') as file:
        records = file.readlines()
        if not records:
            return 1
        last_record = records[-1]
        last_id = json.loads(last_record)["student_id"]
        return last_id + 1


def main():
    filename = 'students.txt'

    student_name = input("Enter the student's name: ")
    student_marks = input("Enter the student's marks: ")

    student_marks = int(student_marks)

    student_id = generate_student_id(filename)

    # Prepare the record
    student_record = {
        "student_id": student_id,
        "student_name": student_name,
        "student_marks": student_marks
    }

    # Write to the file
    with open(filename, 'a') as file:
        file.write(json.dumps(student_record) + '\n')

    print(f"Student record saved with ID: {student_id}")


if __name__ == "__main__":
    main()


    class PairFinder:
        def __init__(self, numbers, target):
            self.numbers = numbers
            self.target = target

        def find_pair(self):

            index_map = {}

            for i, number in enumerate(self.numbers):
                complement = self.target - number

                if complement in index_map:
                    # Return the indices of the pair
                    return index_map[complement], i

                index_map[number] = i

            return "No pair found"


    numbers = [10, 20, 10, 40, 50, 60, 70]
    target = 50
    finder = PairFinder(numbers, target)
    result = finder.find_pair()

    if isinstance(result, tuple):
        print(f"Indices: {result[0]}, {result[1]}")
    else:
        print(result)


class Calculator:
    def __init__(self, X, n):
        self.X = X
        self.n = n

    def sum(self):
        return self.X + self.n

    def pow(self):
        return self.X ** self.n


calc = Calculator(3, 4)
print("Sum of X and n:", calc.sum())
print("X raised to the power of n:", calc.pow())

import math


class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_distance(self):
        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        return distance


point_distance = Distance(1, 2, 4, 6)
print("The distance between the points is:", point_distance.calculate_distance())
