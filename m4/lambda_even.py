any_list = [1, 2, 3, 4, 5, 6]
# even_list = list(map(lambda x: x if x % 2 != 0 else x + 1, any_list))
even_list = list(map(lambda n: n | 1, any_list))

print(even_list)