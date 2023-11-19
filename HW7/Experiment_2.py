# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 
# Instructor: Professor Silveyra
# Description: 
# Errors:
import os
import json
import random
import numpy as np
from Learn import Learn
from Filter import Filter

class K_folds:
    def __init__(self):
        self.all_emails = []

    def create_data(self):
        folder_nums = [1, 2, 3]
        folder_index = 1
        ham_directory = "Enron{}/ham".format(folder_nums[folder_index])
        spam_directory = "Enron{}/spam".format(folder_nums[folder_index])

        for filename in os.listdir(ham_directory):
            with open(os.path.join(ham_directory, filename), 'r', errors='ignore') as file:
                message = file.read()
                real_label = "Ham"  # Since it is reading from ham directory
                self.all_emails.append({"text": message, "label": real_label, "filename": filename})

        for filename in os.listdir(spam_directory):
            with open(os.path.join(spam_directory, filename), 'r', errors='ignore') as file:
                message = file.read()
                real_label = "Spam"  # Since it is reading from spam directory
                self.all_emails.append({"text": message, "label": real_label, "filename": filename})

        random.shuffle(self.all_emails)

    def perform_cross_validation(self, k):
        sub_folds = np.array_split(self.all_emails, k)

        learn = Learn()
        filter = Filter()
        learn.learn_dataset_V2(sub_folds[0], "knowledge.json")
        filter.filter_files_V2(sub_folds[1], "knowledge.json", False, 1)




    
    

if __name__ == "__main__":
    test = K_folds()
    test.create_data()
    test.perform_cross_validation(3)