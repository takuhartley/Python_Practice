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

# Check if the string is a valid identifier
txt = "Demo"
x = txt.isidentifier()
print(x)

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"
print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# Check if all the characters in the text are in lower case
txt = "hello world!"
x = txt.islower()
print(x)

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"
print(a.islower())
print(b.islower())
print(c.islower())

txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")

txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",.asw")
print(x)

dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))

dict = {97: "123", 98: "456", 99: "789"}
string = "abc"
print(string.maketrans(dict))

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)

txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e", 5, 10)
print(x)

txt = "banana"
x = txt.rjust(20, "O")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")
print(x)

txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")

txt = "banana,,,,,ssaaww....."
x = txt.rstrip(",.asw")
print(x)

txt = "welcome to the jungle"
x = txt.split()
print(x)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)

txt = "apple#banana#cherry#orange"
# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines(True)
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

txt = "Hello, welcome to my world."
x = txt.startswith("wel", 7, 20)
print(x)