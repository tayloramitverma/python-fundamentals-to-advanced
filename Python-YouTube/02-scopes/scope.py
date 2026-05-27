username = "tayloramitverma"

def func1():
    # username = "Amit"
    print(username)

func1()
print(username)


x = 99

def func2(y):
    z = x + y
    print(z)

func2(1)


def func3():
    global x
    x = 12

func3()
print(x)

