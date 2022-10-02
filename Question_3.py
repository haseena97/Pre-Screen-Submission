import pandas as pd
import numpy as np
# cleaning data 
import re
# for division
from operator import truediv
# to multiply all element in the list
from functools import reduce

# put the text line by line into list
with open('C:/Users/Acer/Downloads/pre-screen/text/poco.txt', 'r') as f:
    lines_list = [] # buant container kosong
    for line in f:
        lines_list.append(line.strip()) # line.strip utk buang semua whitespace
        # masukkan dalam container kosong tu
        
# Removing unwanted symbols if exists
def cleaning_text(i):
    i = re.sub("[^A-Za-z" "]+"," ",i).lower() #buang punctuation
    i = re.sub("[0-9" "]+"," ",i)
    w = []
    for word in i.split(" "):
        if len(word)>3: # remove joint word
            w.append(word)
    return (" ".join(w))

lines_list2 = [cleaning_text(item) for item in  lines_list]

# Q1: count probability of the word 'data' occuring in each line
# count occurrence of 'data' in each line
nm = 'data'
occurences = [item.count(nm) for item in  lines_list2]
count = sum(occurences)
print(occurences) # This will print out all occurences of input string
print('count = ', count) 
# count total words in each line
total_word = []
for x,word in enumerate(lines_list2):
    num = (len(word.split()))
    total_word.append(num)
# probability of word 'data' occuring in each line
prob = list(map(truediv, occurences, total_word))
print ("The probability of of the word “data” occurring for each line is : " + str(prob))

#result = reduce((lambda x, y: x * y), prob)
#print ("The probability of of the word “data” occurring in every line is : ", result)

# Q2: Frequency distribution of unique words
import nltk
# join into paragraph
paragraph = " ".join(lines_list2)
nltk.download('punkt')
words = nltk.tokenize.word_tokenize(paragraph)
fdist1 = nltk.FreqDist(words)
filtered_word_freq = dict((word, freq) for word, freq in fdist1.items() if not word.isdigit())
print(filtered_word_freq)
# frequency distribution of words
import matplotlib.pyplot as plt
plt.barh([ str(i) for i in filtered_word_freq.keys()], filtered_word_freq.values(), color='g')

# Q3: probability of 'analytics' occurring given 'data'occurred in paragraph
# Bayes theorem --> conditional probability
paragraph = str.split(paragraph)
tot_word = 0
count_d = 0
count_a = 0
for lines in  paragraph:
    tot_word = tot_word + 1
    if lines == 'data':
        count_d = count_d + 1
    if lines == 'analytics':
        count_a = count_a + 1
prob_data = count_d / tot_word
prob_analytics = count_a / tot_word
print('P(analytics_given_data):',(prob_data*prob_analytics)/prob_data)

