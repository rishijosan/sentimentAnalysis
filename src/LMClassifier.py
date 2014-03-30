#===============================================================================
# HW1
# CSE 628: Natural Language Processing
# Stony Brook University
# March 8, 2014
#===============================================================================

import math
import nltk
import nltk.data
from  nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader
import time
import os



# Corpus Location
posTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/pos/'
negTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/neg/'

# Create Plain Text Corpus
posCorpus = PlaintextCorpusReader(posTrainCorpus, '.*')
negCorpus = PlaintextCorpusReader(negTrainCorpus, '.*')

#GetBigrams
posBigrams = nltk.bigrams(posCorpus.words())
negBigrams = nltk.bigrams(negCorpus.words())

#Get no. of words per corpus
posWordLen = len(posCorpus.words())
negWordLen = len(negCorpus.words())

start = time.time()

#Creates frequency distribution for words in corpus
posFreqDist = FreqDist()
for word in posCorpus.words():
    posFreqDist.inc(word)

negFreqDist = FreqDist()
for word in negCorpus.words():
    negFreqDist.inc(word)
 
#Frequency Distributions with Laplace Smoothing 
global posLapFreq
posLapFreq = nltk.probability.LaplaceProbDist(posFreqDist) 
global negLapFreq
negLapFreq = nltk.probability.LaplaceProbDist(negFreqDist)


#FreqDist for Bigrams
global posBiFreq
posBiFreq = nltk.probability.LaplaceProbDist(nltk.FreqDist(posBigrams))
global negBiFreq
negBiFreq = nltk.probability.LaplaceProbDist(nltk.FreqDist(negBigrams))


# Function to calculate Perplexity, pass a list of words and a Laplace Prob Dist, return a float value
def perplex(testSet, freqDist):

    prob = 0
    for word in testSet:
            prob += math.log(float(1)/freqDist.prob(word))
            
    return math.pow(prob, float(1)/len(testSet))



# Functions which return if document is Negative or Positive, pass a list of words, get string 
def perp(ws):
    pos = perplex(ws, posLapFreq)
    #print pos 
    neg =  perplex(ws, negLapFreq)
    #print neg 
    if pos < neg:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'
    
    
def perpBi(ws):
    pos = perplex(ws, posBiFreq)
    #print pos 
    neg =  perplex(ws, negBiFreq)
    #print neg 
    if pos < neg:
        return 'POSITIVE'
    else:
        return 'NEGATIVE'





posTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/pos/'
negTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/neg/'   

      
    
# Create Test Corpora
posTest = PlaintextCorpusReader(posTestCorpus, '.*')
negTest = PlaintextCorpusReader(negTestCorpus, '.*')

#List to store result
res= list()

#For each test file classify
for testFile in negTest.fileids():
    wordSet =  negTest.words(testFile)
    res.append(perp(wordSet)) 


# Function to create dictionary of word frequencies manually
#===============================================================================
# def freqWords(corpus):
#    newDict = dict()
#    
#    for word in corpus.words():
#        freq = newDict.get(word)
#        if (freq == None):
#            newDict[word] = 1
#        else:
#            newDict[word] = freq + 1
#            
#    return newDict
# 
# 
# 
# posDict = freqWords(posCorpus)
# negDict = freqWords(negCorpus)
# 
# for item in posDict.items():
#    posProb[item[0]] =  math.log(item[1]) - math.log(posWordLen)
#===============================================================================


#Testing Perplexity
#===============================================================================
# wordSet =  negCorpus.words('cv019_16117.txt')
# print perp(wordSet)
# print perpBi(nltk.bigrams(wordSet))
#===============================================================================
   






