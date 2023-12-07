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
from collections import Counter

class Inverted_Index:
    def __init__(self):
        self.inverted_index = {}
        self.query_index = {}
        self.max_freq = {}
        self.total_documents = 0

    # Adapted from Professor Silveyra
    def parse_HTML(self, html_content):
        # Parse the HTML content
        x = re.findall(">([^<]+)</[^>]+>", html_content)
        x = [a for a in x if a != '']
        x = ' '.join(x)

        return x

    # def preprocess_email(self, text, version):
    #     """
    #     Preprocesses an email text based on the specified version.

    #     Parameters:
    #     - text (str): The input email text.
    #     - version (int): The version of preprocessing to apply.

    #     Returns:
    #     - list: A list of preprocessed words.
    #     """
    #     # Remove removing stopwords and lemmatization
    #     if (version == 1):
    #         stop_words = set(stopwords.words('english'))
    #         lemmatizer = WordNetLemmatizer()
    #         words = []
    #         for each_word in text.split():
    #             if each_word.isalpha():
    #                 if each_word.lower() not in stop_words:
    #                     lem_word = lemmatizer.lemmatize(each_word.lower())
    #                     words.append(lem_word)
    #         return words
    #     # Only removing stopwords
    #     elif (version == 2):
    #         stop_words = set(stopwords.words('english'))
    #         words = []
    #         for each_word in text.split():
    #             if each_word.isalpha():
    #                 if each_word.lower() not in stop_words:
    #                     words.append(each_word.lower())
    #         return words
    #     # Only lemmatization
    #     elif (version == 3):
    #         lemmatizer = WordNetLemmatizer()
    #         words = []
    #         for each_word in text.split():
    #             if each_word.isalpha():
    #                 lem_word = lemmatizer.lemmatize(each_word.lower())
    #                 words.append(lem_word)
    #         return words
        
    #     # No improvements
    #     elif (version == 4):
    #         words = []
    #         for each_word in text.split():
    #             if each_word.isalpha():
    #                 words.append(each_word.lower())
    #         return words
        
    #     # Error checking
    #     else:
    #         print("Check `preprocess_email()` method!")
    
    def preprocess_page(self, webpage):
        """
        Preprocesses an email text by removing stopwords and lemmatizing words.

        Parameters:
        - text (str): The input email text.

        Returns:
        - list: A list of preprocessed words.
        """
        # parsed_text = self.parse_HTML(webpage)
        parsed_text = webpage

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
                content = file.read()
                words = self.preprocess_page(content)
                words = content.split()
                self.update_index(filename, words)

        self.set_max_freq()
        # self.printInvertedIndex()

    def set_max_freq(self):
        for each_key_word in self.inverted_index:
            current_word_dict = self.inverted_index[each_key_word]

            for each_doc in current_word_dict:
                try:
                    if current_word_dict[each_doc] > self.max_freq[each_doc]:
                        self.max_freq[each_doc] = current_word_dict[each_doc]
                except:
                    self.max_freq[each_doc] = current_word_dict[each_doc]

    def calc_term_freq(self, term, document):
        if term in self.inverted_index.keys():
            frequent_num = self.inverted_index.get(term).get(document, 0)
        else:
            frequent_num = 0
        # print(frequent_num / self.max_freq.get(document))
        return frequent_num / self.max_freq.get(document) 

    def calc_Idf(self, term):
        cur_index = self.inverted_index.get(term, 0)

        if cur_index != 0:
            df = len(cur_index)
        else:
            df = 0

        # print(math.log10(self.total_documents/(df + 1)))
        return math.log10(self.total_documents/(df + 1)) + 1

    def printInvertedIndex(self):
        for x in self.inverted_index:
            print(x, self.inverted_index.get(x))
    
    def calc_weight(self, token, document):
        # print((self.calc_term_freq(token, document) * self.calc_Idf(token)) + 1)
        return (self.calc_term_freq(token, document) * self.calc_Idf(token))

    def calc_weight_query(self, token, document):
        words_query = document
        max_query_freq = Counter(words_query).most_common(3).pop()[1]

        tf = words_query.count(token) / max_query_freq
        idf = self.calc_Idf(token)

        return (tf * idf)

    def get_url(self, file_path):
        try:
            with open(file_path, 'r') as file:
                # Get first line of the file which should have a url
                first_line = file.readline().strip()

                match = re.search(r'(https?://\S+)', first_line)
                
                if match:
                    return match.group(0)
                else:
                    raise ValueError("No URL!")
        except Exception as e:
            # print(f"An error occurred: {e}")
            pass

    def get_top_ten_results(self, query, directory):
        self.load_Inverted_Index(directory)
        # Store filenames and Cosine similarity
        results_dict = {}
        #
        query_list = self.preprocess_page(query)
        # calculate the summation of weights for all tokens and add them to `numerator`
        for textName in os.listdir(directory):
            numerator = 0
            dominator = 0
            summation_weight_ij = 0
            summation_weight_iq = 0
            
            for each_token in query_list:
                weight_ij = self.calc_weight(each_token, textName) 
                weight_iq = self.calc_weight_query(each_token, query_list)
                numerator += weight_ij * weight_iq
                # print(weight_ij)
            # calc dominator
            for each_token in query_list:
                weight_ij = self.calc_weight(each_token, textName) 
                weight_iq = self.calc_weight_query(each_token, query_list)
                summation_weight_ij += math.pow(weight_ij, 2)
                summation_weight_iq += math.pow(weight_iq, 2)
            # 
            dominator = (math.sqrt(summation_weight_ij) * math.sqrt(summation_weight_iq)) + 1
            # print(numerator/dominator, filename) 
            results_dict[textName] = (numerator/dominator)

        # Sort the dictionary by values in descending order
        sorted_items = sorted(results_dict.items(), key=lambda x: x[1], reverse=True)
        # Creates a new dictionary from the sorted list
        sorted_results_dict = dict(sorted_items)  
        # print top ten results
        print("Top 10 results:")
        for rank, name in enumerate(sorted_results_dict):
            filepath = directory + name
            print(sorted_results_dict[name], end=" ")
            print(str(rank + 1) + ": " + name + ". Url: " + str(self.get_url(filepath)))
            if rank + 1 == 10:
                return

if __name__ == "__main__":

    # Test = Inverted_Index()
    # Test.load_Inverted_Index("crandocs/")
    # Test.get_top_ten_results("what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft .","crandocs/")

    Test = Inverted_Index()
    Test.load_Inverted_Index("crandocs/")
    Test.get_top_ten_results("what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft .","crandocs/")    
    # Test.get_top_ten_results("what similarity laws must be obeyed when constructing aeroelastic models of heated high speed aircraft .","crandocs/")    
