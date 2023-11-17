import os
import json
import math
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
from Learn import preprocess_email


def calculate_spam_probability(email, knowledge_json, total_ham_files, total_spam_files, total_distinct_tokens ):

    words = preprocess_email(email)

    ham_probability_of_file = 0
    spam_probability_of_file = 0

    ham_tokens_num = len(knowledge_json['ham_counter'])
    spam_tokens_num = len(knowledge_json['spam_counter'])

    # ham_prob = ham_counter / (ham_counter + spam_counter)
    # spam_prob = spam_counter / (ham_counter + spam_counter)

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
        return "ham"
    else:
        return "spam"



def get_unique_tokens(ham_json, spam_json):
    keys_ham = set(ham_json.keys())
    keys_spam = set(spam_json.keys())
    unique_token_total = len(keys_ham.symmetric_difference(keys_spam))

    return unique_token_total

def filter(ham_directory, spam_directory, knowledge_file, display_messages):
    # Inital counter of files in a directory
    num_ham_docs = 0
    num_spam_docs = 0

    with open(knowledge_file, 'r') as json_file:
        knowledge = json.load(json_file)

    total_unique_tokens = get_unique_tokens(knowledge['ham_counter'], knowledge['spam_counter'])

    
    # Calculate number of documents in `ham` and `spam` folders
    for filename in os.listdir(ham_directory):
        num_ham_docs += 1

    for filename in os.listdir(spam_directory):
        num_spam_docs += 1

    for filename in os.listdir(ham_directory):
        num_ham_docs += 1

        with open(os.path.join(ham_directory, filename), 'r', errors='ignore') as file:
            message = file.read()

            result = calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens)

            real_label = "Ham"  # Since it is reading from ham directory

            if display_messages:
                print(f"Message {filename}: {result}. Real: {real_label}")

    for filename in os.listdir(spam_directory):
        num_spam_docs += 1
        with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
            
            message = file.read()

            result = calculate_spam_probability(message, knowledge, num_ham_docs, num_spam_docs, total_unique_tokens)
            real_label = "Spam"  # Since it is reading from spam directory

            if display_messages:
                print(f"Message {filename}: {result}. Real: {real_label}")



if __name__ == "__main__":
    # to disable messages turn display to false
    filter("Enron2/ham", "Enron2/spam", "knowledge.json", True)
