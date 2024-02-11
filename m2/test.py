# print(float("1, 3"))

# x = '\''
# print(len(x))

try:
    print("1"/0)
except TypeError:
    print("ErrorT")
except ArithmeticError:
    print("ErrorA")
except ZeroDivisionError:
    print("ErrorZ")
except:
    print("Error")