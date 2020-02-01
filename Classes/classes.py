class Person:
    def __init__(self, fname, lname, age):
        self.first_name = fname
        self.last_name = lname
        self.age = age

    def PersonIntroduction(self):
        print("Hello my name is " + self.first_name)
rich br
    def PersonAgeIntroduction(self):
        print("My age is " + str(self.age))


p1 = Person("Robert", "Hartley", 22)
p1.PersonIntroduction()
p1.PersonAgeIntroduction()


class Student(Person):
    pass


x = Student("Cameron", "Hartley", 24)
x.PersonIntroduction()