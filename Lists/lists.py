thislist = ["apple", "strawberry", "banana"]
print(thislist)

thislist = ["apple", "strawberry", "banana"]
print(thislist[1])

thislist = ["apple", "strawberry", "banana"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "strawberry", "banana"]
thislist[1] = "blackcurrant"
print(thislist)

# Looping through a list
thislist = ["apple", "strawberry", "banana"]
for x in thislist:
    print(x)

# Check if item exists
thislist = ["apple", "strawberry", "banana"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

# List length
thislist = ["apple", "strawberry", "banana"]
print(len(thislist))

# Adding items to list
thislist = ["apple", "strawberry", "banana"]
thislist.append("orange")
print(thislist)

# To add to a specific index use the insert() method
thislist = ["apple", "strawberry", "banana"]
thislist.insert(1, "orange")
print(thislist)

# Remove item
thislist = ["apple", "strawberry", "banana"]
thislist.remove("banana")
print(thislist)

# Using pop()
thislist = ["apple", "strawberry", "banana"]
thislist.pop()
print(thislist)

# Using del
thislist = ["apple", "strawberry", "banana"]
del thislist[0]
print(thislist)

# Using clear()
thislist = ["apple", "strawberry", "banana"]
thislist.clear()
print(thislist)

# Using copy()
thislist = ["apple", "strawberry", "banana"]
mylist = thislist.copy()
print(mylist)

# Using list()
thislist = ["apple", "strawberry", "banana"]
mylist = list(thislist)
print(mylist)

# Joing two list()
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Using extend
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# The list contructor
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)
