# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 11/12/2023 
# Instructor: Professor Silveyra
# Description: The purpose of this assignment is to help you learn about spam filters and naive Bayesian learning.
# Errors:
# Helpful sources: https://pieriantraining.com/iterate-over-files-in-directory-using-python/ , 
# https://www.machinelearningplus.com/nlp/lemmatization-examples-python/, 
import os
import json
import nltk
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class Learn:
    def __init__(self):
        pass

    def preprocess_email(self, text):
        stop_words = set(stopwords.words('english'))
        lemmatizer = WordNetLemmatizer()
        words = []
        for each_word in text.split():
            if each_word.isalpha():
                if each_word.lower() not in stop_words:
                    lem_word = lemmatizer.lemmatize(each_word.lower())
                    words.append(lem_word)

        return words

    def learn_dataset(self, ham_directory, spam_directory, output_file):
        ham_counter = {}
        spam_counter = {}

        # Find each files in `.\enron1\ham`
        for filename in os.listdir(ham_directory):
            with open(os.path.join(ham_directory, filename), 'r', errors='ignore') as file:
                words = self.preprocess_email(file.read())
                for each_word in words:
                    try:
                        ham_counter[each_word] += 1
                    except:
                        ham_counter[each_word] = 1

        for filename in os.listdir(spam_directory):
            with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
                words = self.preprocess_email(file.read())
                for each_word in words:
                    try:
                        spam_counter[each_word] += 1
                    except:
                        spam_counter[each_word] = 1


        knowledge = {
            'ham_counter': ham_counter,
            'spam_counter': spam_counter,
        }

        with open(output_file, 'w') as json_file:
            json.dump(knowledge, json_file)
    
    def learn_dataset_V2(self, a_fold, output_file):
        ham_counter = {}
        spam_counter = {}

        # Find each files in `.\enron1\ham`
        for each_dict in a_fold:
            message = each_dict["text"]
            label = each_dict["label"]

            words = self.preprocess_email(message)

            if label == "Ham":
                for each_word in words:
                    try:
                        ham_counter[each_word] += 1
                    except:
                        ham_counter[each_word] = 1
            
            elif label == "Spam":
                for each_word in words:
                    try:
                        spam_counter[each_word] += 1
                    except:
                        spam_counter[each_word] = 1               

        knowledge = {
            'ham_counter': ham_counter,
            'spam_counter': spam_counter,
        }

        with open(output_file, 'w') as json_file:
            json.dump(knowledge, json_file)

if __name__ == "__main__":
    test = Learn()
    test.learn_dataset("Enron1/ham", "Enron1/spam", "knowledge.json")
