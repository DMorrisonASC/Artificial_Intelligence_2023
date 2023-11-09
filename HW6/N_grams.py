# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: Implement a program that counts the unigrams and bigrams of a text file using Python. Improvements:
# 1) Originally: `prob = (self.bigram.get(combin, 2 / len(self.unigram))) / self.unigram.get(prev_word, 1 / len(self.unigram))`
# Updated: `prob = (self.bigram.get(combin, 0)) +  1 / (self.unigram.get(prev_word, 0) + abs(len(self.unigram)))` in `print_bigrams()`
# 2) Imported `math` library
# 3) Originally: `prob = (self.bigram.get(pair, 1)) / self.unigram.get(index-1, 1)` in `print_sentence_prob()` method
# Updated: `log_prob = math.log10(self.bigram.get(pair, 1)) +  1 / (self.unigram.get(index -1, 1) + abs(len(self.unigram)))`
# Errors: Original version's probilities may not have  been calculated properly.

import re
import math

class N_grams:
    def __init__(self):
        self.unigram = dict()
        self.bigram = dict()

    def load_file(self, fileName):
        f = open(fileName, "r", encoding='utf-8-sig')
        for eachLine in f:
            pattern = r'\.(?:\s|\\)' # a regex expression that finds any expression of a puncation mark followed by a space or new line
            line_convert = re.sub(pattern, " </s><s> ", eachLine)
            # print(line_convert) # Print converted line
            # Add uni-grams
            for eachWord in line_convert.split():
                self.add_unigrams(str(eachWord))
            # Add bi-grams
            for i in range(len(line_convert.split())):
                try:
                    self.add_bigrams(line_convert.split()[i],  line_convert.split()[i+1])
                except:
                    pass

    def add_unigrams(self, word):
        # Create a new uni-gram key in dictionary if it doesn't exist. If it does exist, increment by 1
        try:
            self.unigram[word] += 1
        except KeyError:
            self.unigram[word] = 1

    def add_bigrams(self, word1, word2):
        # Create a new bi-gram key in dictionary if it doesn't exist. If it does exist, increment by 1
        combination = word1 + " " + word2
        try:
            self.bigram[combination] += 1
        except KeyError:
            self.bigram[combination] = 1 

    def print_unigrams(self, word): 
        print('"{}" appears {} time(s)'.format(word, self.unigram.get(word, 0)))
        print('"{}" appears {} time(s) at the beginning of a sentence'.format(word, self.bigram.get("</s><s>" + " " + word, 0)))
        print('"{}" appears {} time(s) at the ending of a sentence'.format(word, self.bigram.get(word + " " + "</s><s>", 0)))
        
        for key in self.bigram.keys(): # Find all keys that have `word` as a seperate word
            if word + " " in key or " " + word in key:
                print('"{}" appears {} time(s)'.format(key, self.bigram.get(key, 0)))

    def print_bigrams(self, current_word, prev_word):
        combin = prev_word + " " + current_word
        print('"{}" occurs {} time(s)'.format(combin, self.bigram.get(combin, 0)))
        # Calculate probability of a bi-gram

        # prob = (self.bigram.get(combin, 2 / len(self.unigram))) / self.unigram.get(prev_word, 1 / len(self.unigram))
        # Improvement 1
        prob = (self.bigram.get(combin, 0)) +  1 / (self.unigram.get(prev_word, 0) + abs(len(self.unigram)))
        print('Probability of {} is {}'.format(combin, prob))
        
        return prob

    def print_sentence_prob(self, sentence):
        pattern = r'\.(?:\s|\\)' # a regex expression that finds any expression of a puncation mark followed by a space or new line
        sentence_convert = re.sub(pattern, " </s><s> ", sentence)

        totalprob = 0
        # Calculate probability of a bi-gram
        for index in range(len(sentence_convert.split())):
            pair = sentence_convert.split()[index - 1] + " " + sentence_convert.split()[index]
            print(pair)
            if index > 0: 
                log_prob = math.log10(self.bigram.get(pair, 1)) +  1 / (self.unigram.get(index -1, 1) + abs(len(self.unigram)))
                totalprob = totalprob + log_prob
        print('Probability of "{}" is {}'.format(sentence, totalprob))

if __name__ == '__main__':
    allGrams =  N_grams()
    allGrams.load_file("pg236.txt")
    allGrams.print_unigrams("good")
    allGrams.print_bigrams("deal", "good")
    allGrams.print_sentence_prob("Good deal")
