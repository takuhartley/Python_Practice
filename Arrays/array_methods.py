people = ["Cameron", "Robert", "Alex", "Clifford"]

# Adds an element at the end of the list
people.append("Mark")
print(people)

# Removes all the elements from the list
people = ["Cameron", "Robert", "Alex", "Clifford"]
people.clear()

# Returns a copy of the list
people = ["Cameron", "Robert", "Alex", "Clifford"]
a = people.copy()
print(a)

# Returns the number of elements with the specified value
people = ["Cameron", "Robert", "Alex", "Clifford"]
b = people.count("Ford")
print(b)

# Add the elements of a list (or any iterable), to the end of the current list
people = ['Cameron', 'Robert', 'Alex', 'Clifford']
c = people.extend(people)
print(c)

# Returns the index of the first element with the specified value
people = ["Cameron", "Robert", "Alex", "Clifford"]
d = people.index("Robert")
print(d)

# Adds an element at the specified position
people = ["Cameron", "Robert", "Alex", "Clifford"]
e = people.insert(0, "Mark")
print(e)

# Length of array
people = ["Cameron", "Robert", "Alex", "Clifford"]
f = len(people)
print(f)

# Removes the element at the specified position
people = ["Cameron", "Robert", "Alex", "Clifford"]
people.pop("Cameron")
print(people)

# Removes the first item with the specified value
people = ["Cameron", "Robert", "Alex", "Clifford"]
people.remove("Robert")
print(people)

# Reverses the order of the list
people.reverse()
print(people)

# Sorts the list
people.sort()
print(people)