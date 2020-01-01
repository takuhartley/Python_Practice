theList = ["Mark", "Yumi", "Cameron", "Robert", "Alexander", "Clifford", "Obi"]
print(theList)
print(theList[1])
print(theList[-1])
print(theList[2:5])
print(theList[-4:-1])

theList[1] = "Obi"
print(theList)

# Looping through a list
for x in theList:
    print(x)

# Check if item exists
if "Robert" in theList:
    print("Yes, 'Robert' is in the list.")

# List length
print(len(theList))

# Adding items to list
theList.append("John")
print(theList)

# To add to a specific index use the insert() method
theList.insert(1, "Bitch")
print(theList)

# Remove item
theList.remove("Cameron")
print(theList)

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
