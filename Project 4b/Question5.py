# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 04:57:36 2018

@author: PeterLee
"""
#this will import from the Testing.py file in the folder.
import Testing as T
import cProfile
import csv
print "Question 5 Tests\n"
print "We are now testing the pen data\n"
iteration = 0
penDataPerf = []
penTotalPerf = []
while iteration < 5:
    penNet, testAccuracy = T.testPenData()
    penDataPerf.append(testAccuracy)
    iteration += 1
print "The Maximum Accuracy of the Pen Data is:", max(penDataPerf)
print "The Average Accuracy of the Pen Data is:", T.average(penDataPerf)
print "The Standard Deviation Accuracy of the Pen Data is:", T.stDeviation(penDataPerf)
print "\n"
penTotalPerf.append(max(penDataPerf))
penTotalPerf.append(T.average(penDataPerf))
penTotalPerf.append(T.stDeviation(penDataPerf))
with open("Question5Pen1.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(penTotalPerf)

print "We are now testing the Car data\n"
iteration = 0
carDataPerf = []
carTotalPerf = []
while iteration < 5:
    carNet, testAccuracy = T.testCarData()
    carDataPerf.append(testAccuracy)
    iteration += 1

print "The Maximum Accuracy of the Car Data is:", max(carDataPerf)
print "The Average Accuracy of the Car Data is:", T.average(carDataPerf)
print "The Standard Deviation Accuracy of the Car Data is:", T.stDeviation(carDataPerf)
print "\n"
carTotalPerf.append(max(carDataPerf))
carTotalPerf.append(T.average(carDataPerf))
carTotalPerf.append(T.stDeviation(carDataPerf))

with open("Question5Car.csv",'wb') as resultFile:
    wr = csv.writer(resultFile, dialect='excel')
    wr.writerows(carTotalPerf)