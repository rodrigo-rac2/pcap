from collections import Counter

word = input("Check if two strings are anagrams\n\nenter the first text (X to exit): ")

while(source_text != 'X'):
    comparison_text = input("enter the second text: ")
    source_counter_dict = Counter(source_text.lower())
    comparison_counter_dict = Counter(comparison_text.lower())

    if source_counter_dict == comparison_counter_dict: print("Anagrams")
    else: print("Not anagrams")

    source_text = input("enter the first text (X to exit): ")
