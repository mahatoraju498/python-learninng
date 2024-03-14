#Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name is {self.name} and age is {self.age}"


p1 = Person("Jon", 30)
print(p1.get_details())