# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: Build an inverted index for efficient data organization. Include preprocessing features for StopWord removal and Stemming, with toggle options. Use advanced data structures for the index and incorporate text normalization techniques. Save the index in a quickly accessible format. The format from the image is a recommended format
# Errors:

import os
import json
import nltk
import math
import requests
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Inverted_Index:
    def __init__(self):
        self.inverted_index = {}
        self.max_freq = {}

    # Adapted from Professor Silveyra
    def parse_HTML(self, html_content):
        # Parse the HTML content
        x = re.findall(">([^<]+)</[^>]+>", html_content)
        #x = [a.strip() for a in x if a!='']
        x = [a for a in x if a!='']
        x = ''.join(x)
        return x
    
    def preprocess_page(self, webpage):
        """
        Preprocesses an email text by removing stopwords and lemmatizing words.

        Parameters:
        - text (str): The input email text.

        Returns:
        - list: A list of preprocessed words.
        """
        parsed_text = self.parse_HTML(webpage)

        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        words = []

        for each_word in parsed_text.split():
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

    def load_Inverted_Index(self, directory):
        for filename in os.listdir(directory):
            with open(os.path.join(directory, filename), 'r', errors='ignore') as file:
                words = self.preprocess_page(file.read())
                self.update_index(filename, words)

        self.set_max_freq()

    def set_max_freq(self):
        for each_key_word in self.inverted_index:
            current_word_dict = self.inverted_index[each_key_word]

            for each_doc in current_word_dict:
                try:
                    if current_word_dict[each_doc] > self.max_freq[each_doc]:
                        self.max_freq[each_doc] = current_word_dict[each_doc]
                except:
                    self.max_freq[each_doc] = current_word_dict[each_doc]
        
        # print max_freq
        # for eachkey in self.max_freq:
        #     print(str(eachkey) + ": ")
        #     print(self.max_freq[eachkey])

    def calc_term_freq(self):
        term = "var"
        document = "9211442309221931223.txt"

        if term in self.inverted_index.keys():
            frequent_num = self.inverted_index.get(term).get(document, 0)
        else:
            frequent_num = 0

        return frequent_num




if __name__ == "__main__":

    Test = Inverted_Index()
    Test.load_Inverted_Index("output/")
    Test.calc_term_freq()

    
