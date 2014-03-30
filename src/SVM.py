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
from collections import OrderedDict
import numpy as np
from sklearn import svm



# Corpus Location
posTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/neg'
negTrainCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/pos'

    
# Create Plain Text Corpus
posCorpus = PlaintextCorpusReader(posTrainCorpus, '.*')
negCorpus = PlaintextCorpusReader(negTrainCorpus, '.*')

#Create Frequency Distribution from both Positive and Negative Corpora
trainFreq = nltk.FreqDist(posCorpus.words() + negCorpus.words())

#No of Features
noFeat = len(trainFreq)
#noFeat=1000

#Get Keys to maintain Order
#CHANGED! Top Thousand words only
#trainKeys = trainFreq.keys()[0:1000]
trainKeys = trainFreq.keys()

#Create OrderedDict for features: Use this as sample for all files
ordFeat = OrderedDict()
for key in trainFreq.keys():
    ordFeat.update( {key: trainFreq.freq(key)} )




def featureList(corpus):
    featList = []
    for trFile in corpus.fileids():
        listItem = [0]*noFeat
        fileFreqDist = FreqDist()
        fileFreqDist = nltk.FreqDist(corpus.words(trFile))
        
        i =0
        for key in trainKeys:
            if fileFreqDist.has_key(key):
                listItem[i] = fileFreqDist.get(key)
            i=i+1
            
        featList.append(listItem)
        
    return featList

posFeatList = featureList(posCorpus)
negFeatList = featureList(negCorpus)
featList = posFeatList + negFeatList

noPos = len(posCorpus.fileids())
noNeg = len(negCorpus.fileids())

labels = []

for j in range(noPos):
    labels.append(1)
for k in range(noNeg):
    labels.append(0)


    
#Create numpy Array for word frequencies : Feature Vector
trainFreqArr = np.array(featList)
trainLabels = np.array(labels)


#Fit SVM
#docClassifier = svm.SVC()
docClassifier = svm.LinearSVC()
#docClassifier = svm.LinearSVC(loss='l2', penalty='l1', dual=False)
docClassifier.fit(trainFreqArr, trainLabels) 

###########################------------------------Testing--------------------------------------------################################## 
        
   
posTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/pos/'
negTestCorpus = '/media/sf_G_DRIVE/nlp/txt_sentoken/test/neg/' 


# Create Test Corpora
posTest = PlaintextCorpusReader(posTestCorpus, '.*')
negTest = PlaintextCorpusReader(negTestCorpus, '.*')

posTestFeatList = featureList(posTest)
negTestFeatList = featureList(negTest)

posTestarr = np.array(posTestFeatList)
negTestarr = np.array(negTestFeatList)

#print docClassifier.predict(negTestarr)

# list for output
opt = list() 

# array to temp store result of prediction
arr = []

# prediction result stored in array which is the converted to list and added to opt list
opt = np.array(docClassifier.predict(negTestarr)).tolist() + np.array(docClassifier.predict(posTestarr)).tolist()
