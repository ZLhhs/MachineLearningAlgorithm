"""
Name   :  NaiveBayes2.py (Use NaiveBayes Algorithm for E-mail classification)
Author :  LiangZHANG
Date   :  2015-8-5
E-mail :  liangzxdu@foxmail.com

Introduction:
"""
import os

path = 'email/spam'
path1 = 'C:\Users\geteway\Desktop\ML\machinelearninginaction\Ch04\email\spam'
path2 = 'C:\Users\geteway\Desktop\ML\machinelearninginaction\Ch04\email\ham'
path3 = 'C:\Users\geteway\Documents\GitHub\MachineLearningAlgorithm\NaiveBayes\data2.txt'
file_output = open(path3,'w')
i=1
for file in os.listdir(path1) :
    file_read = open(path1 +'\\'+ file)

    s = file_read.readlines()
    print i,''.join( s ),'\n**********\n'
    i+=1
    file_output.write( ''.join(s) )

