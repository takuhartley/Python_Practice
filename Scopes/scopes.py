def myfunc():
    x = 300
    print(x)


myfunc()


def myfunctwo():
    x = 300

    def myinnerfunc():
        print(x)
    myinnerfunc()


myfunctwo()

x = 300


def myfuncthree():
    print(x)


myfuncthree()

print(x)


def myfuncfour():
    global x
    x = 300


myfuncfour()

print(x)

x = 300


def myfuncfive():
    global x
    x = 200


myfuncfive()

print(x)
