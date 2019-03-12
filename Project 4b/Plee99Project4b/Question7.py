# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:12:14 2018

@author: PeterLee
"""
from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt
import Testing as T
import csv


train = []
train.append(([0,0],[0]))
train.append(([1,0],[1]))
train.append(([0,1],[1]))
train.append(([1,1],[0]))

#test = []
#test.append(([1,0],[1]))
#test.append(([0,1],[1]))
test = train
XORData = (train, test)
totalPerformance = []
for i in range(0,3):
    iteration = 0;
    hiddenLayerIteration = []
    hiddenLayerPerformance = []
    while iteration < 5:
        Xornet, testAccuracy = buildNeuralNet(XORData, maxItr = 5000, hiddenLayerList = [i])
        hiddenLayerIteration.append(testAccuracy)
        iteration += 1
    print "The Maximum Accuracy of the Pen Data is:", max(hiddenLayerIteration)
    print "The Average Accuracy of the Pen Data is:", T.average(hiddenLayerIteration)
    print "The Standard Deviation Accuracy of the Pen Data is:", T.stDeviation(hiddenLayerIteration)
    print "\n"
    hiddenLayerPerformance.append(i)
    hiddenLayerPerformance.append(max(hiddenLayerIteration))
    hiddenLayerPerformance.append(T.average(hiddenLayerIteration))
    hiddenLayerPerformance.append(T.stDeviation(hiddenLayerIteration))
    totalPerformance.append(hiddenLayerPerformance);
with open("XorData.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(totalPerformance)