# Lamdba


def x(a): return a + 10


print(x(5))


def x(a, b): return a * b


print(x(5, 6))


def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def function_one(n):
    return lambda a: a * n


def function_two(n):
    return lambda a: a * n


mydoubler = function_two(2)

print(mydoubler(11))


def function_three(n):
    return lambda a: a * n


mytripler = function_three(3)

print(mytripler(11))


def function_four(n):
    return lambda a: a * n


mydoubler = function_four(2)
mytripler = function_four(3)

print(mydoubler(11))
print(mytripler(11))
