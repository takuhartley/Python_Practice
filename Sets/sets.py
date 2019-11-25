# Set 
# Uordered & unindexed
a = {"Cameron", "Robert", "Alex", "Clifford"}
print(a)

# Access items
for b in a:
  print(b)

# Check to see if certain item is in set
print("Robert" in a) # Returns true

# Adding item to set
a.add("Mark")
print(a)

# Updating set using update()
a.update(["Yumi", "Yuni", "Obi"])
print(a)

# Length of set using len()
print(len(a))

# remove()
a.remove("Obi")
print(a)

# discard()
a.discard("Yuni")
print(a)

# pop()
c = a.pop()
print(c)
print(c)

# clear()
a.clear()
print(a)

a = {"Cameron", "Robert", "Alex", "Clifford"}

# del
del a
print(a)

# union()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# update()
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
