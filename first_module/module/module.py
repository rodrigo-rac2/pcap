#!/usr/bin/env python3 

"""First module to demonstrate the use of global variables and functions."""

__counter = 0


def sum(l):
    global __counter
    __counter += 1
    s = 0
    for element in l:
        s += element
    return s


def prod(l):
    global __counter
    __counter += 1
    p = 1
    for element in l:
        p *= element
    return p


if __name__ == "__main__": 
    print("I prefer to be a module, but I can do some tests for now.")
    test_list = [x+1 for x in range(5)]
    print(sum(test_list) == 15)
    print(prod(test_list) == 120)
