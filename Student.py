from Person import Person

class Student(Person):
    def __init__(self, name, age, height, major):
        super().__init__(name, age, height)
        self.major = major
        print("This time it's a Student object")

# Student instance creation
s1 = Student("Maria", 22, 6, "Computer Science")
print(f"Student Name: {s1.name}")  # Using the inherited property
print(f"Student Major: {s1.major}")