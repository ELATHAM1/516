#Project 1, Erika Latham
#CHAPTER 1 EXERCISE 24

print('EXERCISE 24')

import nltk
from nltk.book import text6

mylist = [w for w in set(text6) #set used to exclude duplicates
    if w.endswith('ise') #identify words ending with '-ise'
    or 'z' in w #identify words containing lowercase 'z' anywhere
    or'pt' in w #identify words containing lowercase 'pt' anywhere
    or w.istitle()] #identify words starting with an uppercase letter followed by all lowercase (or by no other letters)

    # The instructions for this exercise weren't clear about whether words should meet all 4 conditions,
    # so I originally tried this with AND as the Boolean operator. However, there were no words that met all 4
    # conditions, so I switched to OR between all expressions, which will  words that meet at least one condition.

    # Using list comprehension instead of a for loop allows all expressions to be written in a single line.
    # It also appends words to the list automatically instead of specifying .append() as an extra step.

print('The list of words meeting at least one condition is', mylist)


# EXERCISE 25

print('EXERCISE 25')

sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore'] #Step 1: define set as the list of words provided

for w in sent:
    if w.startswith('sh'): #Step 2, First task: go through each word in the sent list and print words that start with 'sh'
        print(w, 'starts with "sh"') #clarification added since some words are printed for both Step 2 and Step 3

for w in sent:
    if len(w) > 4: #Step 3, Second task: go through each word in the sent list and print words whose length is greater than 4 letters
        print(w, 'is more than 4 letters long') #clarification added since some words are printed for both Step 2 and Step 3

# Since the instructions only said "Print all words" and not "Print a list of words,"
# I chose to use for loops so one word would be printed at a time.