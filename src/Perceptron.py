#===============================================================================
# Author : Rishi Josan
# CSE 628: Natural Language Processing
# Stony Brook University
# March 8, 2014
#===============================================================================

import math
import nltk
import nltk.data
from  nltk.probability import FreqDist
from nltk.corpus import PlaintextCorpusReader


weigthVector = dict()
featureVectors = dict()

# Corpus Location
posTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/train/pos/'
negTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/train/neg/'

    
# Create Plain Text Corpus
posCorpus = PlaintextCorpusReader(posTrainCorpus, '.*')
negCorpus = PlaintextCorpusReader(negTrainCorpus, '.*')

#Create a categorized corpus
#===============================================================================
# catCorpus = nltk.corpus.CategorizedPlaintextCorpusReader('/media/sf_G_DRIVE/nlp/txt_sentoken/' , r'.*\.txt', cat_pattern=r'(\w+)/*')
# catCorpus.words(catCorpus.fileids('pos'))
#===============================================================================


#Get Corpora File IDs
posFiles = dict.fromkeys(posCorpus.fileids())
negFiles = dict.fromkeys(negCorpus.fileids())


# Initialize weight Vector to Zero
for word in posCorpus.words():
    weigthVector[word] = 0       
for word in negCorpus.words():
    weigthVector[word] = 0
 

# Create Feature Vector : Word Frequency
for trFile in posCorpus.fileids():
    fileFreqDist = FreqDist()
    fileFreqDist = nltk.FreqDist(posCorpus.words(trFile))
    featureVectors[trFile] = fileFreqDist
    
for trFile in negCorpus.fileids():
    fileFreqDist = FreqDist()
    fileFreqDist = nltk.FreqDist(negCorpus.words(trFile))
    featureVectors[trFile] = fileFreqDist
    
    
#Create Feature Vector : Word Presence
    

# Train: Converges in 37 iterations :)
for x in xrange(20):
    
    for item in featureVectors.items():
        freq = item[1] #Freq Distriibution
        tempCount = 0
        
        for word in freq.keys():
            tempCount += weigthVector[word] * freq.freq(word)
            
        if tempCount == 0:
            for word in freq.keys():
                weigthVector[word] = freq.freq(word)
        elif tempCount > 0 and negFiles.has_key(item[0]):
            # Predicted +ve but actually negative
            for word in freq.keys():
                weigthVector[word] = weigthVector[word] - freq.freq(word)
        elif tempCount < 0 and posFiles.has_key(item[0]):
            # Predicted -ve but actually positive
            for word in freq.keys():
                weigthVector[word] = weigthVector[word] + freq.freq(word)

      

###########################------------------------Testing--------------------------------------------################################## 
        
   
   
posTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/pos/'
negTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/neg/'     
        
        
# Create Feature Vector : Word Frequency
def corpusFeatureVectors(corpus):
    featVect = dict()
    for trFile in corpus.fileids():
        fileFreqDist = FreqDist()
        fileFreqDist = nltk.FreqDist(corpus.words(trFile))
        featVect[trFile] = fileFreqDist
    return featVect


def testCorpus(corpus, features):  
    for testFile in corpus.fileids():        
        ff = features.get(testFile)
        cc = 0
        
        for word in ff.keys():
            if weigthVector.has_key(word):
                cc += weigthVector[word] * ff.freq(word)
            
        if cc>0:
            print testFile + ' POSITIVE'
        elif cc<0:
            print testFile + ' NEGATIVE'
        else:
            print 'CC is 0'

         
    
# Create Test Corpora
posTest = PlaintextCorpusReader(posTestCorpus, '.*')
negTest = PlaintextCorpusReader(negTestCorpus, '.*')

posFeat = corpusFeatureVectors(posTest)
negFeat = corpusFeatureVectors(negTest)

testCorpus(negTest, negFeat)


        

