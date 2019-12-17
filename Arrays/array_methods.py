cars = ["Honda", "Subaru", "Toyota", "Nissan"]

# Adds an element at the end of the list
cars.append("Ford")
print(cars)

# Removes all the elements from the list
cars.clear()

# Returns a copy of the list
f = cars.copy()
print(f)

# Returns the number of elements with the specified value
g = cars.count("Ford")
print(g)

# Add the elements of a list (or any iterable), to the end of the current list
people = ['Cameron', 'Robert', 'Alex', 'Clifford']
h = people.extend(cars)
print(h)

# Returns the index of the first element with the specified value
i = cars.index("Honda")
print(i)

# Adds an element at the specified position
j = people.insert(1, "Mark")
print(j)

# Length of array
k = len(cars)
print(k)

# Removes the element at the specified position
cars.pop()

# Removes the first item with the specified value
cars.remove()
cars.remove("Honda")
print(cars)

# Reverses the order of the list
cars.reverse()
print(cars)

# Sorts the list
cars.sort()
print(cars)