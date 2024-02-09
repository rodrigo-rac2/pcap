from collections import Counter

date = input("Check the digit of life for a date\n\nenter the date in the format YYYYMMDD (X to exit): ")

while(date != 'X'):
    date_sum = 0
    for char in date:
        if char.isdigit() == False:
            print("Invalid date")
            break
        date_sum += int(char)
    while date_sum > 9:
        part_sum = str(date_sum)
        date_sum = 0
        for ch in part_sum:
            date_sum += int(ch)
    print(date_sum)

    date = input("enter the date in the format YYYYMMDD (X to exit): ")
