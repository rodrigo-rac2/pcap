# def print_function(args, fun):
#     for x in args:
#         print('f(', x,')=', fun(x), sep='')


# # def poly(x):
# #     return 2 * x**2 - 4 * x + 2


# # print_function([x for x in range(-2, 3)], poly)

# print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)



list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()
