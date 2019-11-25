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