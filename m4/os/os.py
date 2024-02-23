import os
print(os.name)
print(os.uname())

try:
    os.mkdir("my_first_directory")
except FileExistsError:
    print("Directory already exists")

print(os.listdir())

try:
    os.makedirs("my_first_directory/my_second_directory")
    os.chdir("my_first_directory")
except FileExistsError:
    print("Directory already exists")

print(os.getcwd())
print(os.listdir())
os.chdir("my_second_directory")
print(os.getcwd())
print(os.listdir())

os.chdir("../..")
os.removedirs("my_first_directory/my_second_directory")

returned_value = os.system("mkdir my_first_directory")
print(returned_value)