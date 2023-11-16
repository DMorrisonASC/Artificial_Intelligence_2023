import os
import json
import nltk
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def preprocess_email(text):
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    words = []
    for each_word in text.split():
        if each_word.isalpha():
            if each_word.lower() not in stop_words:
                lem_word = lemmatizer.lemmatize(each_word.lower())
                words.append(lem_word)
    # print(words)
    return words

def learn(ham_directory, spam_directory, output_file):
    ham_counter = {}
    spam_counter = {}

    # Find each files in `.\enron1\ham`
    for filename in os.listdir(ham_directory):
        with open(os.path.join(ham_directory, filename), 'r', errors='ignore') as file:
            words = preprocess_email(file.read())
            for each_word in words:
                try:
                    ham_counter[each_word] += 1
                except:
                    ham_counter[each_word] = 1

    for filename in os.listdir(spam_directory):
        with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
            words = preprocess_email(file.read())
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
    # f = open("pg236.txt", "r", encoding='utf-8-sig')
    # preprocess_email(f.read())
    learn("Enron1/ham", "Enron1/spam", "knowledge.json")