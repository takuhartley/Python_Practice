# Getting data type
# You can get the data type of any object by using the type() function:

x = 5
print(type(x))

x = "Robert"
print(type(x))

x = 3.14
print(type(x))

x = [1, 2, 3]
print(type(x))

x = ("Crawl", "Walk", "Run")
print(type(x))

x = range(10)
print(type(x))

x = {"name": "Robert", "age": 22}
print(type(x))

x = {"Coffee", "Code", "Repeat"}
print(type(x))

x = frozenset({"Coffee", "Code", "Repeat"})
print(type(x))

x = True
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

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
