import os

def find(path, dir):
    os.chdir(path)
    directories = os.listdir()
    if dir in directories:
        print(f"{os.getcwd()}/{dir}")
    for directory in directories:
        find(directory, dir)
        os.chdir("..")


if __name__ == "__main__":
    find('./tree', 'python')
else: 
    print('imported')