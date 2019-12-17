import mymodule as mx
import platform

x = platform.system()
print(x)

x = dir(platform)
print(x)

mx.greeting("Robert")

a = mx.person1["age"]
print(a)