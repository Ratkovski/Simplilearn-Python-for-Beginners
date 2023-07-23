import os
import time

epc = time.time()
print(epc)
localtime = time.localtime(epc)
print(localtime)
print(localtime.tm_year)
print(time.ctime(epc))


def current_directory():
    cwd = os.getcwd()
    print(cwd)


def file_path(filename):
    path = os.path.abspath(filename)
    print(path)


current_directory()
filename = "sample.txt"
file_path(filename)

# import smtplib
#
# smtObj = smtplib.SMTP('smtp.gmail.com', 587)
# smtObj.ehlo()
# smtObj.starttls()
# smtObj.login()

from os import path


def createFile(dest):
    if not (path.isfile(dest)):
        f = open(dest, 'w')
        f.write("Welcome to python scripting")


dest = "D:\PYTHON\Simplilearn-Python-for-Beginners\scripting\sample.txt"
createFile(dest)
print("Created")


def funcl(*args):
    for i in args:
        print(i)


funcl(10, 20, 30, 40)


def funcl2(**kwargs):
    for i in kwargs.items():
        print(i)


funcl2(a=10, b=20, c=30, d=40)


def funcl3():
    x = 10

    def funcl4(x):
        return x + 1

    return funcl4(x)


result = funcl3()
print(result)


def funcl5(called_func):
    print("This is a the first function")

    def nested_func(called_func):
        print("This is the nested function")
        called_func()

    return nested_func(called_func)


#@funcl5
def outer_func():
    print("This is the outer function")

obj = funcl5(outer_func)
#outer_func()

# Factory

B = type("BaseClass", (object,), {})
C1 = type("C1", (B,), {'val': 5})
C2 = type("C2", (B,), {'val': 10})


def ClassCreator(bool):
    if bool:
        return C1()
    else:
        return C2()


print(ClassCreator(True).val)
print(ClassCreator(False).val)
