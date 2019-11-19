x = 4
y = 4
z = x == y
a = x != y
print(z)
print(a)

b = x > y
print(b)

b = x >= y
print(b)

c = x < y
print(c)

c = x <= y
print(c)

# Logical Operators
x = 5
print(x > 3 and x < 10)

x = 5
print(x > 3 or x < 4)

x = 5
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
print(x is not y)
print(x != y)

x = ["apple", "banana"]
print("banana" in x)

x = ["apple", "banana"]
print("pineapple" not in x)