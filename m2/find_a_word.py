print("Are the characters comprising the first string hidden inside the second string?\n")
word = input("enter the word to look for (X to exit): ")

while(word != 'X'):
    comparison_text = input("enter the string to look into: ")

    last_pos = comparison_text.find(word[0])
    for i in range(1, len(word)):
        pos =  comparison_text.find(word[i], last_pos + 1)
        if pos == -1:
            print("No")
            break
        else: last_pos = pos
    if i == len(word) - 1: print("Yes")

    word = input("enter the word to look for (X to exit): ")
