# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 05:09:43 2018

@author: PeterLee
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 04:57:36 2018

@author: PeterLee
"""
#this will import from the Testing.py file in the folder.
import Testing as T
import csv

print "We are now testing the Car data\n"
iteration = 0
carDataPerformance = []
hiddenLayerSize = 5
while hiddenLayerSize <= 40:
    totalPerformanceCar = []
    iteration = 0
    hiddenLayerPerformance = []
    while iteration < 5:
        carNet, testAccuracy = T.testCarData([hiddenLayerSize])
        hiddenLayerPerformance.append(testAccuracy)
        iteration += 1
    
    print "Hidden layer size:", hiddenLayerSize
    print "The Maximum Accuracy of the Pen Data is:", max(hiddenLayerPerformance)
    print "The Average Accuracy of the Pen Data is:", T.average(hiddenLayerPerformance)
    print "The Standard Deviation Accuracy of the Pen Data is:", T.stDeviation(hiddenLayerPerformance)
    print "\n"
    totalPerformanceCar.append(hiddenLayerSize)
    totalPerformanceCar.append(max(hiddenLayerPerformance))
    totalPerformanceCar.append(T.average(hiddenLayerPerformance))
    totalPerformanceCar.append(T.stDeviation(hiddenLayerPerformance))
    carDataPerformance.append(totalPerformanceCar)
    hiddenLayerSize += 5
with open("carDataPerformance1.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(carDataPerformance)

