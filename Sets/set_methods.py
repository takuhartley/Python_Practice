# add()
people = {"Cameron", "Robert", "Alex", "Clifford"}
people.add("Mark")
print(people)

people.clear()
print(people)

people = {"Cameron", "Robert", "Alex", "Clifford"}
a = people.copy()
print(a)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)