# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 9/15/2023
# Instructor: Professor Silveyra
# Description: Part 3 of HW 2
# Errors:
 
import random
import math

# 1
catList = [ "Cat Number:" + str(i) for i in range(500)]
print(catList)

# 2
hunToOneList = [ i for i in range(100, 0, -1)]
print(hunToOneList)

# 3
listInList = [[i for i in range(0, 10001) if math.sqrt(i).is_integer()] for i in range(100)]
print(listInList)

# 4
sentence = "Today is Monday and it is not very hot"
sen_length = [len(i) for i in sentence.split()]
print(sen_length)