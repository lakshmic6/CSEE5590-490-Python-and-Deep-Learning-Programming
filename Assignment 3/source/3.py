from nltk.collocations import ngrams
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from collections import Counter

#Opening the information content record with read mode.
fileopen = open("lem.txt", "r")

#persuing the content text document
contentsoffile = fileopen.read()

# Printing the contents of the file
print("substances of the file:", "\n", contentsoffile)
print("================================================")

#  word lemmatization
lem = WordNetLemmatizer()

# Tokenizing the substance of the record.
wrd1 = word_tokenize(contentsoffile)

print("Lemmatization with verb form of the words:")
for word in wrd1:
    print(lem.lemmatize(word, pos='v'))

print("===================================================")

print("Playing out the biagram of the text:")
cp = word_tokenize(contentsoffile)
lns = []

#Accessing ngram capacity to discover bigrams from the given content.
bgfact = ngrams(cp, 2)
for a in bgfact:
    lns.append(a)
print(lns)

print("=======================================================")

#Utilizing counter capacity to tally the quantity of occurances of every bigram.
wrdcnt1 = Counter(lns)
print(" Calculating the word frequency of Bi-Gram:")
print(wrdcnt1)


print("Finding the top 5 bigrams:")
print("========================================================")
freqc = nltk.FreqDist(lns)
mkd = freqc.most_common(5)

#Printing top five bigrams which are discovered utilizing most_common work.
print(mkd)

with open('lem.txt', 'r') as file:
    length = file.readlines()
fit = ''

for mp in length:
    fit = fit + mp
sen = sent_tokenize(fit)
rep_sent1 = []

for sentences in sen:
    for word, wrd1 in lns:
        for ((cp, mp), l) in mkd:
            if (word, wrd1 == cp, mp):
                rep_sent1.append(sentences)

# best five biagrams
print("\n Condensing the content and discovering the lines with top five bigrams")
print("==========================================================================")
fc = nltk.FreqDist(rep_sent1)
fff = fc.most_common(5)
for ke, val in fff:
    print("\n", ke)
