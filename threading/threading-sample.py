from threading import *
import time


# Process in an executable instance of a computer program


# a thread is a sequence of instructions in a program that can be executed independently of the remaining program

def show():
    print("This is a child thread")


t = Thread(target=show())
t.start()
print("This is parent thread")


class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("This is a child thread")


t = MyThread()
t.start()
for i in range(5):
    print("\n This is a main thread")


class Demo:
    def show(self):
        for i in range(5):
            print("This is a child thread")


obj = Demo()
t = Thread(target=obj.show())
t.start()
for i in range(5):
    print("This is the parent thread")


# Context Switching
# Storing the state of a process or thread and resuming its execution at a later time is called context switching
# Multithreading
# A model where multiple threads within  a process execute independently while sharing the same resources
# is called multithreading


class Demo2():
    def num(self):
        for i in range(1, 6):
            print("The number is", i)
            time.sleep(1)

    def double(self):
        for i in range(1, 6):
            print("The double of the number is", 2 * i)
            time.sleep(1)

    def square(self):
        for i in range(1, 6):
            print("The square of the number is", i*i)
            time.sleep(1)

obj=Demo2()
t1=Thread(target=obj.num)
t2=Thread(target=obj.double)
t3=Thread(target=obj.square)

t1.start()
time.sleep(0.2)
t2.start()
time.sleep(0.2)
t3.start()

t1.join()
t2.join()
t3.join()

print("This is the main thread")
