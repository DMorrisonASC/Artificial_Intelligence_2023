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
        print("4. Search for bigram")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            find_word1 = str(input("Enter word: ").strip())
            allGrams.print_unigrams(find_word1)
        elif choice == 2:
            first_Word = str(input("Enter 1st word: ").strip())
            sec_Word = str(input("Enter 2nd word: ").strip())
            allGrams.print_bigrams(sec_Word, first_Word)
        elif choice == 3:
            sentence = str(input("Enter a sentence: ").strip())
            allGrams.print_sentence_prob(sentence)

        elif choice == 4:
            first_Word = str(input("Enter 1st word: ").strip())
            sec_Word = str(input("Enter 2nd word: ").strip())
            third_Word = str(input("Enter 3nd word: ").strip())
            allGrams.print_tri_grams(third_Word, sec_Word, first_Word)

        elif choice == 5:
            # Exit the loop
            print("Exiting the program....")
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

