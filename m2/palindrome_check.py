s = input("enter the text to check if it's a palindrome (X to exit): ")

while(s != 'X'):
    if s.replace(" ", "").lower() == s[::-1].replace(" ", "").lower() : print("It's a palindrome")
    else: print("It's not a palindrome")
    s = input("enter the text to check if it's a palindrome (X to exit): ")
