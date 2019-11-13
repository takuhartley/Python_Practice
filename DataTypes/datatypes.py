# Getting data type
# You can get the data type of any object by using the type() function:

a = 5
print(type(a))
b = "Robert"
print(type(b))
c = 3.14
print(type(c))
d = [1,2,3]
print(type(d))
e = ("Crawl", "Walk", "Run")
print(type(e))
f = range(10)
print(type(f))
g = {"name" : "Robert", "age" : 22}
print(type(g))
h = {"Coffee", "Code", "Repeat"}
print(type(h))
i = frozenset({"Coffee", "Code", "Repeat"})
print(type(i))
j = True
print(type(j))
k = b"Hello"
print(type(k))
l = bytearray(5)
print(type(l))
m = memoryview(bytes(5))
print(type(m))

# Setting a specific data type
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)	
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))	
x = range(6)
x = dict(name="John", age=36)
x = set(("apple", "banana", "cherry"))	
x = frozenset(("apple", "banana", "cherry"))	
x = bool(5)
x = bytes(5)	
x = bytearray(5)	
x = memoryview(bytes(5))