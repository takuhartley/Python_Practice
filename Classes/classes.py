class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PersonIntroduction(self):
        print("Hello my name is " + self.name)

    def PersonAgeIntroduction(self):
        print("My age is " + str(self.age))

p1 = Person("Robert", 22)
p1.PersonIntroduction()
p1.PersonAgeIntroduction()
