def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    num = 0
    while(True):
        exception = False
        try:
            num = int(input(prompt))
            assert num >= -10 and num <= 10
        except ValueError:
            print('Error: wrong input')
            exception = True
        except AssertionError:
            print('Error: the value is not within permitted range (min..max)')
            exception = True
        finally:
            if not exception: break
    return num


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
