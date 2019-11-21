thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Looping through a list
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Check if item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# List length
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# Adding items to list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To add to a specific index use the insert() method
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Remove item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Using pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# Using del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Using clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Using copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Using list()
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# Joing two list()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)