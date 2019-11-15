txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

txt = "banana"
x = txt.center(20)
print(x)

txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

txt = "My name is Ståle"
print(txt.encode)
print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x)
x = txt.endswith("my world.")
print(x)
x = txt.endswith("my world.", 5, 11)
print(x)

txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x)
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.find("e", 5, 10)
print(x)

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'am {age}".format(fname = "Robert", age = 22)
txt2 = "My name is {0}, I'am {1}".format("Robert",22)
txt3 = "My name is {}, I'am {}".format("Robert",22)
print(txt1)
print(txt2)
print(txt3)

point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))

