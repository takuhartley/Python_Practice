cars = ["Ford", "Volvo", "BMW"]

# Traverse
for i in cars:
	print(i)

# Insertion
def insert(list, n):
    for i in range(len(list)):
        if list[i] > n:
            index = i
            break
    list = list[:i] + [n] + list[i:]
    return list
list = [1, 2, 4]
n = 3  
print(insert(list, n))

# Deletion
def delete(list, n):
    for i in range(len(list)):
        if list[i] > n:
            index = i
        break
        if list[i] == n:
            del list[i]
    return list

# Search
def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            print(“found it”)
        else:
            print(“not in list)

# Update
def update(list, n, r):
    for i in range(len(list)):
        if list[i] == n:
            list[i] = r
    return list
