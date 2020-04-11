# Inheritance enable us to define a class that takes all the functionality from parent class and allows us to add more.
# Inheritance is a powerful feature in object oriented programming.It refers to defining a new
# class with little or no modification to an existing class.The new class is called derived ( or child)
# class and the one from which it inherits is called the base ( or parent) class.

class Mammal:
    def __init__(self, name):
        self.name = name

    def walk(self):
        print(f"{self.name} can walks")


class Cat(Mammal):
    def bark(self):
        print("Dogs bark")


class Dog(Mammal):
    def be_annoying(self):
        print("Cats are be annoying")


cat = Cat("cat")
cat.walk()
dog = Dog("Dog")
dog.walk()
