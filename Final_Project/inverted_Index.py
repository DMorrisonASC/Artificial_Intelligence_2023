# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: Build an inverted index for efficient data organization. Include preprocessing features for StopWord removal and Stemming, with toggle options. Use advanced data structures for the index and incorporate text normalization techniques. Save the index in a quickly accessible format. The format from the image is a recommended format
# Errors:

import os
import json
import nltk
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Inverted_Index:
    def __init__(self):
        self.inverted_index = {}
    
    def preprocess_page(self, text):
        """
        Preprocesses an email text by removing stopwords and lemmatizing words.

        Parameters:
        - text (str): The input email text.

        Returns:
        - list: A list of preprocessed words.
        """
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        words = []
        for each_word in text.split():
            if each_word.isalpha():
                if each_word.lower() not in stop_words:
                    lem_word = lemmatizer.lemmatize(each_word.lower())
                    words.append(lem_word)
        return words

    def update_index(self, file_name, words):
        for each_word in words:
            # Test if `each_word` exists as a key in dictionary. If key is present, increment. If not, create a new key
            if each_word in self.inverted_index.keys():
                if file_name in self.inverted_index[each_word].keys():
                    current_key = self.inverted_index[each_word]
                    current_key[file_name] += 1
                else:
                    current_key = self.inverted_index[each_word]
                    current_key[file_name] = 1
            else:
                self.inverted_index[each_word] = {file_name: 1}
        
        for eachkey in self.inverted_index:
            print(str(eachkey) + ": ")
            print(self.inverted_index[eachkey])

    def load_Inverted_Index(self, directory):
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'r', errors='ignore') as file:
                words = self.preprocess_page(file.read())
                self.update_index(filename, words)



if __name__ == "__main__":

    Test = Inverted_Index()
    Test.load_Inverted_Index("output/")

    
