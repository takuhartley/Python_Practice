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

txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)

x = txt.index("e")
print(x)

x = txt.index("e", 5, 10)
print(x)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Company 12"
x = txt.isalnum()
print(x)

# Checks to see if all the characters in variable are alphabet letters
txt = "CompanyX" # True
x = txt.isalpha()
print(x)

txt = "Company10" # False
x = txt.isalpha()
print(x)

# Check if all the characters in the unicode object are decimals
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x)

a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

# Check if all the characters in the text are digits
txt = "50800"
x = txt.isdigit()
print(x)

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²
print(a.isdigit())
print(b.isdigit())