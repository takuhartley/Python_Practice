# Lamdba


def function_one(a): return a + 10


print(function_one(5))


def function_two(a, b): return a * b


print(function_two(5, 6))


def function_three(a, b, c): return a + b + c


print(function_three(5, 6, 2))


def function_four(n):
    return lambda a: a * n


def function_five(n):
    return lambda a: a * n


mydoubler = function_five(2)

print(mydoubler(11))


def function_six(n):
    return lambda a: a * n


mytripler = function_six(3)

print(mytripler(11))


def function_seven(n):
    return lambda a: a * n


mydoubler = function_seven(2)
mytripler = function_seven(3)

print(mydoubler(11))
print(mytripler(11))