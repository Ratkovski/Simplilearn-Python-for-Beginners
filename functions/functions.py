# a function is a set of code that performs some task
def welcome():
    print("Good Morning")


def add(a, b):
    print(id(a), id(b))
    a = 2
    b = 3
    total = a + b
    print("a:%d    b:%d" % (a, b))
    print("the sum is %", total)


add(a=10, b=20)
x = 2
y = 3
print(id(x), id(y))
add(x, y)


def add(*a):
    total = 0
    for i in a:
        total = total + i
    print("the sum is ", total)


add(10, 20, 30, 50)
add(1)


def add(lst):
    lst[2] = 0


lst = [0, 1, 2]
print(lst)
add(lst)
print(lst)


def add(x, y):
    total = x + y
    return total


result = add(10, 20)
print("the sum is ", result)
