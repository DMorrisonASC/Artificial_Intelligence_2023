# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:

from N_grams import N_grams

class Tester:
    while True:
        try:
            fileName = input('Enter your filename:')
            allGrams =  N_grams()
            allGrams.load_file(fileName)
            break
        except:
            print("This file does not exist! Try again.")
            continue


    choice = 0

    while choice != 4:
        print("Options:")
        print("1. Search for unigram")
        print("2. Search for bigram")
        print("3. Sentence probability")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            # Perform action 1
            find_word1 = input("Enter word: ").strip()
            allGrams.print_unigrams(find_word)
        elif choice == 2:
            # Perform action 2
            first_Word = input("Enter 1st word: ").strip()
            sec_Word = input("Enter 2nd word: ").strip()
            allGrams.bigram(sec_Word, first_Word)
        elif choice == 3:
            # Perform action 3
            print("Action 3 performed.")
        elif choice == 4:
            # Exit the loop
            print("Exiting the program.")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

