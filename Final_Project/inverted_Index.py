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
from MaxHeap import MaxHeap

class Inverted_Index:
    def __init__(self):
        self.inverted_index = {}
        self.max_freq = {}
        self.total_documents = 0

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
            self.total_documents += 1
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

    def calc_term_freq(self, term, document):
        if term in self.inverted_index.keys():
            frequent_num = self.inverted_index.get(term).get(document, 0)
        else:
            frequent_num = 0

        if frequent_num != 0:
            return frequent_num / self.max_freq.get(document) 
        else:
            return 0 

    def calc_Idf(self, term):
        try:
            df = len(self.inverted_index.get(term))
        except:
            df = 0

        if df != 0:
            return math.log10(self.total_documents/df)
        else:
            return 0
    
    def calc_weight(self, token, document):
        return (self.calc_term_freq(token, document) * self.calc_Idf(token)) + 1

    def get_top_ten_results(self, query, directory):
        # add query to inverted index
        words = self.preprocess_page(query)
        self.update_index(query, words)
        # Store filenames and Cosine similarity
        results_dict = {}

        # calculate the summation of weights for all tokens and add them to `numerator`
        for filename in os.listdir(directory):
            numerator = 0
            dominator = 0
            summation_weight_ij = 0
            summation_weight_iq = 0
            
            for each_token in query.split():
                weight_ij = self.calc_weight(each_token, filename) 
                weight_iq = self.calc_weight(each_token, query)
                numerator += weight_ij * weight_iq
            # calc dominator
            for each_token in query.split():
                weight_ij = self.calc_weight(each_token, filename) 
                weight_iq = self.calc_weight(each_token, query)
                summation_weight_ij += math.pow(weight_ij, 2)
                summation_weight_iq += math.pow(weight_iq, 2)
            # 
            dominator = (math.sqrt(summation_weight_ij) * math.sqrt(summation_weight_iq)) + 1
            # print(numerator/dominator, filename) 
            results_dict[filename] = (numerator/dominator) 

        # Sort the dictionary by values in descending order
        sorted_items = sorted(results_dict.items(), key=lambda x: x[1], reverse=True)
        # Creates a new dictionary from the sorted list
        sorted_results_dict = dict(sorted_items)  
        for x in sorted_results_dict:
            print(x, sorted_results_dict[x])

if __name__ == "__main__":

    Test = Inverted_Index()
    Test.load_Inverted_Index("output/")
    Test.get_top_ten_results("var play count","output/")

    
