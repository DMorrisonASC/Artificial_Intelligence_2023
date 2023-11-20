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
        folder_nums = [1, 2, 3, 4, 5]

        for i in folder_nums:

            ham_directory = "Enron{}/ham".format(i)
            spam_directory = "Enron{}/spam".format(i)

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
        #
        sum_acc = 0
        sum_prec = 0
        sum_recall = 0

        learn = Learn()
        filter = Filter()

        print("Total folds/value of k: ", str(k))
        for i in range(k):
            print("Training set is section " + str(i) )
            learn.learn_dataset_V2(sub_folds[i], "knowledge.json")

            temp1 = 0
            temp2 = 0
            temp3 = 0
            
            for j in range(k):
                if j != i:
                    print("section " + str(j) + " results:" )
                    all_statistics = filter.filter_files_V2(sub_folds[j], "knowledge.json", False, 1)
                    temp1 += all_statistics[0]
                    temp2 += all_statistics[1]
                    temp3 += all_statistics[2]
                
            sum_acc += (temp1 / (k-1))
            sum_prec += (temp2 / (k-1))
            sum_recall += (temp3 / (k-1))

        
        print(sum_acc/k)
        print(sum_prec/k)
        print(sum_recall/k)
        print("\nStatistic for {}-fold(s):\nAvg accurary: {}.\nAvg precision: {}\nAvg recall: {}".format(k, sum_acc/k, sum_prec/k, sum_recall/k))
        print()

if __name__ == "__main__":
    test = K_folds()
    test.create_data()
    test.perform_cross_validation(2)
    test.perform_cross_validation(3)
    test.perform_cross_validation(4)
    test.perform_cross_validation(5)
