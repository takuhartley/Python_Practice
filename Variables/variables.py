# Can be a number
a = 1
print(a)
b = 2
print(b)

# Can be a string
c = "Hello World!"
print(c)

# Can reassign variables
c = "Robert"
print(c)

"""
Rules for Python Variables
A variable must start with a letter or underscore character
Variable name cannot stop with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (money, Money and MONEY are three different variables)
"""

# Assign value to multiple variables
a, b, c, d = "Red", "Blue", "Green", "Yellow"
print(a)
print(b)
print(c)
print(d)

# Can assign multiple variables in one line
a = b = c = "Fam"
print(a)
print(b)
print(c)

# Outputting variables
x = "You're "
y = "the best."
print(x + y)

z = x + y
print(z)

"""
You cannot add together two variables
which are two different type
"""

# Global variables

x = "DJ KHALID"

def DJKHALID():
  print("I'm " + x)

DJKHALID()

"""
If you create a variable with the same name inside a function, 
this variable will be local, 
and can only be used inside the function.
The global variable with the same name will remain as it was, 
global and with the original value.
"""