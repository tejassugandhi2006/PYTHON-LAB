# Base class

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):

    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def display_student(self):
        self.display_person()
        print(f"Course: {self.course}")


name = input("Enter name: ")
age = int(input("Enter age: "))
course = input("Enter course: ")

student = Student(name, age, course)

print("\n--- Student Details ---")

student.display_student()
