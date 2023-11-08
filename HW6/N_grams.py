# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: Implement a program that counts the unigrams and bigrams of a text file using Python.
# Errors:

import re

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
        try:
            self.unigram[word] += 1
        except KeyError:
            self.unigram[word] = 1

    def add_bigrams(self, word1, word2):
        combination = word1 + " " + word2
        try:
            self.bigram[combination] += 1
        except KeyError:
            self.bigram[combination] = 1 

    
    def print_unigrams(self, word): 
        print('"{}" appears {} time(s)'.format(word, self.unigram.get(word, 0)))
        print('"{}" appears {} time(s) at the beginning of a sentence'.format(word, self.bigram.get("</s><s>" + " " + word, 0)))
        print('"{}" appears {} time(s) at the ending of a sentence'.format(word, self.bigram.get(word + " " + "</s><s>", 0)))
        for key in self.bigram.keys():
            if word + " " in key or " " + word in key:
                print('"{}" appears {} time(s)'.format(key, self.bigram.get(key, 0)))

    def print_bigrams(self, current_word, prev_word):
        combin = prev_word + " " + current_word
        print('"{}" occurs {} time(s)'.format(combin, self.bigram.get(combin, 0)))
    
        # prob = (self.unigram.get(current_word, 1 / len(self.unigram)) + self.unigram.get(prev_word, 1 / len(self.unigram))) / self.unigram.get(prev_word, 1 / len(self.unigram))
        prob = (self.bigram.get(combin, 2 / len(self.unigram))) / self.unigram.get(prev_word, 1 / len(self.unigram))
        print('Probability of {} is {:%}'.format(combin, prob))
        
        return prob

    def print_sentence_prob(self, sentence):
        # for eachWord in range(sentence):
        #     pass
        pattern = r'\.(?:\s|\\)' # a regex expression that finds any expression of a puncation mark followed by a space or new line
        sentence_convert = re.sub(pattern, " </s><s> ", sentence)
        # print(sentence_convert) # Print converted line

        totalprob = 1

        for index in range(len(sentence_convert.split())):
            pair = sentence_convert.split()[index - 1] + " " + sentence_convert.split()[index - 1]
            if index != 0: 
                prob = (self.bigram.get(pair, 1 / len(self.bigram))) / self.unigram.get(index-1, 1 / len(self.unigram))
                totalprob = totalprob * prob
        
        print('Probability of "{}" is {:%}'.format(sentence, totalprob))


    # def replace_spec_chars(self, word):
    #     hex_code = 0
    #     for char in word:
    #         if char == "." :
    #         pass

if __name__ == '__main__':
    allGrams =  N_grams()
    allGrams.load_file("pg236.txt")
    allGrams.print_unigrams("Theaaaa")
    allGrams.print_bigrams("deal", "good")
    allGrams.print_sentence_prob("I love carts. I love plants.")


