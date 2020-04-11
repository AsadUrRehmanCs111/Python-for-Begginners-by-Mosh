class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(10, 20)
# point1.x = 10
# point1.y = 20
print(point1.x)
point1.x = 19
print(point1.x)

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi {self.name}")


person1 = Person('Asad Ur Rehman')
person1.talk()
person2 = Person("Ali Ahmad")
person2.talk()
