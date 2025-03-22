class Person:
    def __init__(self, name, age, height):
        self.__name = name
        self.__age = age
        self.__height = height
        self.public_prop = "I'm public"

        print("Constructing the Person object")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def __del__(self):
        print("The garbage collector is automatically destroying the Person object")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

p1 = Person("Mark", 20, 6)
print(p1.public_prop)

try:
    print(p1.__name)  # Should cause an AttributeError
except AttributeError:
    print("AttributeError: Cannot access private attribute directly.")

print(p1.get_name())
p1.set_name("Anna")
print(p1.get_name())

# Using magic getter and setter
print(p1.name)
p1.name = "John"
print(p1.name)