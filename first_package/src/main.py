from sys import path

path.append('../module')

from module import sum, prod


zero_list = [0 for i in range(5)]
one_list = [1 for i in range(5)]

print(sum(zero_list), prod(one_list))