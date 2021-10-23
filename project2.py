import nltk
from nltk import *

#CHAPTER 2 EXERCISE 18
# Write a program to print the 50 most frequent bigrams (pairs of adjacent
# words) of a text, omitting bigrams that contain stopwords.

from nltk.book import text2

mytext = [w.lower() for w in text2]
#converts everything to lowercase since all words in stopwords are lowercased

stopwords = nltk.corpus.stopwords.words('english')

allbigrams = bigrams(mytext)

nonstopbigrams = [b for b in allbigrams if b[0] not in stopwords and b[1] not in stopwords]
# check both elements of every bigram in allbigrams against the list of stopwords
# b[0] indicates the first element, b[1] indicates the second
# if neither element is in stopwords, add that bigram to the nonstopbigrams list

bigramfreq = FreqDist(nonstopbigrams)
print('The 50 most frequest bigrams with punctuation included are:', bigramfreq.most_common(50))

#This way will exclude punctuation so we can see bigrams where both elements are actual words
#I've commented it out because if both sets of code are active, the second FreqDist comes out empty

# punctuation = ['.', '?', '"', '."', ',"', ',', "'", '-', '!', ';', ':']
# #I'm sure there's a way to generate thish punctuation list with regex but we haven't talked about
# #how to integrate it into python code yet

# allstops = stopwords + punctuation

# interestingbigrams = [p for p in allbigrams if p[0] not in allstops and p[1] not in allstops]
# intbigramfreq = FreqDist(interestingbigrams)
# print('The 50 most frequest bigrams with punctuation excluded are:', intbigramfreq.most_common(50))



#CHAPTER 2 EXERCISE 19
#Write a program to create a table of word frequencies by genre, like the
#one given in 1 for modals. Choose your own words and try to find words
#whose presence (or absence) is typical of a genre. Discuss your findings.

from nltk.corpus import brown

freqbygenre = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['adventure', 'editorial', 'mystery', 'news', 'religion', 'romance']
interestingwords = ['dark', 'jungle', 'Lord', 'President', 'alibi', 'strange','foreign', 'passion']

print('The frequencies of interesting words by genre are:')
freqbygenre.tabulate(conditions=genres, samples=interestingwords)
