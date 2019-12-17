mytuple = ("Cameron", "Robert", "Alex", "Clifford")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

for x in mytuple:
    print(x)

mystr = "Real"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

for x in mystr:
  print(x)

