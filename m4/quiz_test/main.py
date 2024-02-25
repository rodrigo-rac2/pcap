# def f():
#     for n in range(3):
#         yield n

# for i in f():
#     print(i)


###
# f = [ i + i for i in range(5)]
# print   (f)


# ###
# x = lambda a, b: a ** b
# print(x(2, 10))

# numbers = (1, 2, 5, 9, 15)
# def f(num):
#     nums = (1, 5, 17)
#     if num in nums: return True
#     else: return False

# filtered_numbers = filter(f, numbers)
# for num in filtered_numbers:
#     print(num)

# def f(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s

# for x in f(2):
#     print(x, end='')

# my_list = [1, 2, 3]
# foo = tuple(map(lambda x: x ** x, my_list))
# print(foo)  # Output: (1, 4, 27)

# def o(p):
#     def q():
#         return '*' * p
#     return q

# r = o(1)
# s = o(2)

# print(r() + s())

# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         print (c)
#         # yield c

# I()
# # for x in I():
# #     print(x, end='')

# import calendar
# # print(calendar.weekheader(5))
# for weekday in calendar.Calendar().iterweekdays():
#     print(weekday, end=" ")

# from datetime import date

# date1 = date(2020, 1, 1)
# date2 = date(2020, 12, 31)
# print (date2 - date1)

# import os 
# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# os.mkdir('tmp')
# os.chdir('../')
# print (os.getcwd())

# os.mkdir('thumbnails')
# os.chdir('thumbnails')

# sizes = [ 'small', 'medium', 'large']

# for size in sizes:
#     os.mkdir(size)

# print(os.listdir())
# # 
# b = bytearray(3)
# print(b)

# my_tuple = (0, 1, 2, 3, 4, 5, 6)
# foo = list(filter(lambda x: x-0 and x-1, my_tuple))
# print(foo)  # Output: [2, 3, 4, 5, 6]

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0

#         def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s[self.i]
#         self.i += 1
#         return v

# for x in I():
#     print(x, end='')

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException:
#     print("a")
# except Exception:
#     print("b")

# class A:
#     def __init__(self, v):
#         self.__a = v + 1

# a = A(0)
# print(a.__a)  # Output: AttributeError: 'A' object has no attribute '__a'
# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# print(hasattr(A, 'a'))  # Output: False

# try: 
#     raise Exception(1, 2, 3)
# except Exception as e:
#     print(len(e.args)) 

# print(float("1.3"))

# class Class:
#     def __init__(self, val=0):
#         pass

# object = Class(None)
# o = Class(1,2)

# class A:
#     def __init__(self):
#         pass
# a = A(1)
# print(hasattr(a, 'A'))  # Output: error

# class A:
#     def a(self):
#         print('a')
# class B:
#     def a(self):
#         print('b')
# class C(B, A):
#     def c(self):
#         self.a()
# o = C()
# o.c()

# import math
# print(dir(math))

# var = 0
# assert var != 0

# print(var)

# import os
# # os.mkdir('pictures')
# # os.chdir('pictures')

# # print(os.getcwd())
# print(os.uname())

# print("\\\\")
# print(len("\\\\"))

# class A:
#     def __init__(self, v=2):
#         self.v = v

#     def set(self, v=1):
#         self.v += v
#         return self.v

# a = A()
# b = a
# b.set()
# print(a.v)  # Output: 3

# from datetime import datetime

# datetime1 = datetime(2020, 1, 1, 11, 27, 22)
# datetime2 = datetime(2020, 1, 1, 0, 0, 1)

# print(datetime1 - datetime2)  # Output: 11:27:21

# class A:
#     pass
# class B(A):
#     pass
# class C(B):
#     pass
# print(issubclass(A, C)) # Output: False

# from datetime import timedelta

# delta = timedelta(weeks = 1, days = 7, hours = 11)
# print(delta*2) 