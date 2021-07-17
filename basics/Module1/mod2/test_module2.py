import sys
import inspect


# module2.py
def mod2_test1():
    print ("Module2 -> Test1")
    print("Path : ", inspect.getfile(inspect.currentframe()))


def mod2_test2():
    print ("Module2 -> Test2")
    print("Path : ", inspect.getfile(inspect.currentframe()))
