#class God:
#     def __init__(self, n, s, a, m, h):
#         self.name = n
#         self.strength = s
#         self.abilities = a
#         self.mortal = m
#         self.health = h

#     def isMortal(self):
#         self.mortal = False

# class Demon:
#     def __init__(self, n, s, a, m, h):
#         self.name = n
#         self.strength = s
#         self.abilities = a
#         self.mortal = m
#         self.health = h

#     def isMortal(self):
#         self.mortal = False

class Hero:
    def __init__(self, n, s, a, h):
        self.name = n
        self.strength = s
        self.abilities = a
        self.mortal = True
        self.health = h

    def whatsmyname(self):
        print("My name is " + self.name)

h1 = Hero("Elon", 75, "Super Strength", 100)
h1.whatsmyname()
print(h1.strength)
print(h1.abilities)
print(h1.mortal)
print(h1.health)