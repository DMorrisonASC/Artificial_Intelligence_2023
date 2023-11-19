# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 11/12/2023
# Instructor: Professor Silveyra
# Description: The purpose of this assignment is to help you learn about spam filters and naive Bayesian learning.
# Errors:
# Helpful sources: https://pieriantraining.com/iterate-over-files-in-directory-using-python/ , 
# https://www.machinelearningplus.com/nlp/lemmatization-examples-python/, 

import os
import json
import math
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter

class Filter:
    def __init__(self):
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0
        self.folder_name = ""

    def preprocess_email(self, text, version):
        # Remove removing stopwords and lemmatization
        if (version == 1):
            stop_words = set(stopwords.words('english'))
            lemmatizer = WordNetLemmatizer()
            words = []
            for each_word in text.split():
                if each_word.isalpha():
                    if each_word.lower() not in stop_words:
                        lem_word = lemmatizer.lemmatize(each_word.lower())
                        words.append(lem_word)
            return words
        # Only removing stopwords
        elif (version == 2):
            stop_words = set(stopwords.words('english'))
            words = []
            for each_word in text.split():
                if each_word.isalpha():
                    if each_word.lower() not in stop_words:
                        words.append(each_word.lower())
            return words
        # Only lemmatization
        elif (version == 3):
            lemmatizer = WordNetLemmatizer()
            words = []
            for each_word in text.split():
                if each_word.isalpha():
                    lem_word = lemmatizer.lemmatize(each_word.lower())
                    words.append(lem_word)
            return words
        
        # No improvements
        elif (version == 4):
            words = []
            for each_word in text.split():
                if each_word.isalpha():
                    words.append(each_word.lower())
            return words
        
        # Error checking
        else:
            print("Check `preprocess_email()` method!")

    def calculate_spam_probability(self, email, knowledge_json, total_ham_files, total_spam_files, total_distinct_tokens, version):

        words = self.preprocess_email(email, version)

        ham_probability_of_file = 0
        spam_probability_of_file = 0

        ham_tokens_num = len(knowledge_json['ham_counter'])
        spam_tokens_num = len(knowledge_json['spam_counter'])

        ham_doc_prob = total_ham_files / (total_ham_files + total_spam_files)
        spam_doc_prob = total_spam_files / (total_ham_files + total_spam_files)

        ham_probability_of_file = ham_doc_prob
        spam_probability_of_file = spam_doc_prob

        for word in words:
            try:
                formula_ham = ( knowledge_json['ham_counter'][word] + 1) / (ham_tokens_num + total_distinct_tokens)
            except:
                formula_ham = (0 + 1) / (ham_tokens_num + total_distinct_tokens)
            word_prob = math.log10( formula_ham  )
            ham_probability_of_file += word_prob

        for word in words:
            try:
                formula_spam = ( knowledge_json['spam_counter'][word] + 1 ) / (spam_tokens_num + total_distinct_tokens)
            except:
                formula_spam = ( 0 + 1 ) / (spam_tokens_num + total_distinct_tokens)
            word_prob = math.log10( formula_spam  )
            spam_probability_of_file += word_prob
        
        if ham_probability_of_file > spam_probability_of_file:
            return "Ham"
        else:
            return "Spam"

    def get_unique_tokens(self, ham_json, spam_json):

        keys_ham = set(ham_json.keys())
        keys_spam = set(spam_json.keys())
        unique_token_total = len(keys_ham.symmetric_difference(keys_spam))

        return unique_token_total

    def filter_files(self, ham_directory, spam_directory, knowledge_file, display_messages, version):
        # Inital counter of files in a directory
        num_ham_docs = 0
        num_spam_docs = 0
        # Get name of enron folder
        match = re.search(r'Enron(\d+)/', ham_directory)
    
        if match:
            # Extract the matched word and number
            self.folder_name = match.group(0)
            print(self.folder_name)
        else:
            print("Error: Folder not found")

        with open(knowledge_file, 'r') as json_file:
            knowledge = json.load(json_file)

        total_unique_tokens = self.get_unique_tokens(knowledge['ham_counter'], knowledge['spam_counter'])

        
        # Calculate number of documents in `ham` and `spam` folders
        for filename in os.listdir(ham_directory):
            num_ham_docs += 1

        for filename in os.listdir(spam_directory):
            num_spam_docs += 1

        for filename in os.listdir(ham_directory):

            with open(os.path.join(ham_directory, filename), 'r', errors='ignore') as file:
                message = file.read()

                result = self.calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens, version)

                real_label = "Ham"  # Since it is reading from ham directory

                if display_messages:
                    print(f"Message {filename}: {result}. Real: {real_label}")

                self.add_result(result, real_label)

        for filename in os.listdir(spam_directory):

            with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
                
                message = file.read()

                result = self.calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens, version)
                real_label = "Spam"  # Since it is reading from spam directory

                if display_messages:
                    print(f"Message {filename}: {result}. Real: {real_label}")

                self.add_result(result, real_label)
        self.report_stats()
        # The very last method to run
        self.report_stats

    def filter_files_V2(self, a_fold, knowledge_file, display_messages, version):
        # Inital counter of files in a directory
        num_ham_docs = 0
        num_spam_docs = 0

        with open(knowledge_file, 'r') as json_file:
            knowledge = json.load(json_file)

        total_unique_tokens = self.get_unique_tokens(knowledge['ham_counter'], knowledge['spam_counter'])

        # Calculate number of documents in `ham` and `spam` folders
        for each_dict in a_fold:
            label = each_dict["label"]

            if label == "Ham":
                num_ham_docs += 1
            elif label == "Spam":
                num_spam_docs += 1

        for each_dict in a_fold:
            message = each_dict["text"]
            label = each_dict["label"]
            filename = each_dict["filename"]

            if label == "Ham":
                result = self.calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens, version)

                if display_messages:
                    print(f"Message {filename}: {result}. Real: {label}")

                self.add_result(result, label)
            
            elif label == "Spam":
                result = self.calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens, version)
        
                if display_messages:
                    print(f"Message {filename}: {result}. Real: {label}")

                self.add_result(result, label)

            else:
                print("Error")

            

        # for filename in os.listdir(spam_directory):
        #     num_spam_docs += 1
        #     with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
                
        #         message = file.read()

        #         result = self.calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens, version)
        #         real_label = "Spam"  # Since it is reading from spam directory

        #         if display_messages:
        #             print(f"Message {filename}: {result}. Real: {real_label}")

        #         self.add_result(result, real_label)

        self.report_stats()
        # The very last method to run
        self.report_stats

    def add_result(self, prediction, real):
        if (prediction == "Spam" and real == "Spam"):
            self.tp += 1 # True Positive
        elif (prediction == "Spam" and real == "Ham"):
            self.fp += 1 # False positive
        elif (prediction == "Ham" and real == "Ham"):
            self.tn += 1 # True negative
        elif (prediction == "Ham" and real == "Spam"):
            self.fn += 1 # False negative
        else:
            print("Check the input of `add_result()`!!")
    
    def reset_outcomes(self):
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0

    def report_stats(self):
        # Accuracy Stats
        accuracy = (self.tp + self.tn) / (self.tp + self.fp + self.fn + self.tn)
        precision = self.tp / (self.tp + self.fp)
        recall = self.tp / (self.tp + self.fn)

        print("{} stats\n---------\nAccuracy: {}\nPrecision: {}\nRecall: {}".format(self.folder_name, accuracy, precision, recall))

if __name__ == "__main__":
    # to disable messages turn display to false and vice versa
    test = Filter()
    print("\nStatistics when remove removing stopwords and lemmatization")
    test.filter_files("Enron2/ham", "Enron2/spam", "knowledge.json", False, 1)
    print("\nStatistics when remove removing stopwords")
    test.filter_files("Enron2/ham", "Enron2/spam", "knowledge.json", False, 2)
    print("\nStatistics when using lemmatization")
    test.filter_files("Enron2/ham", "Enron2/spam", "knowledge.json", False, 3)
    print("\nStatistics with not improvements")
    test.filter_files("Enron2/ham", "Enron2/spam", "knowledge.json", False, 4)
