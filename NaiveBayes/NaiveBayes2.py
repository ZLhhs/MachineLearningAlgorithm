"""
Name   :  NaiveBayes2.py (Use NaiveBayes Algorithm for E-mail classification)
Author :  LiangZHANG
Date   :  2015-8-5
E-mail :  liangzxdu@foxmail.com

Introduction:
"""
"""
import os


path = 'email/spam'
print path

path1 = 'C:\Users\geteway\Desktop\ML\machinelearninginaction\Ch04\email\spam'
path2 = 'C:\Users\geteway\Desktop\ML\machinelearninginaction\Ch04\email\ham'
print path1,path2
path3 = 'C:\Users\geteway\Documents\GitHub\MachineLearningAlgorithm\NaiveBayes\data2.txt'
file_output = open(path3)
i=1
for file in os.listdir(path1) :
    file_read = open(path1 +'\\'+ file)

    s = file_read.readlines()
    print i,''.join( s ),'\n**********\n'
    i+=1
    file_output.write( ''.join(s) )
"""
import numpy
import os

def Scan_Text () :
    """
    This function scan all the text and split it
    :return:
    """
    L = []
    address = 'data2'
    for folder in os.listdir(address) :
        for Name_List in os.listdir(address+'/'+folder) :
            file_read = open(address+'/'+folder+'/'+Name_List)
            print Name_List
            s = ''
            line = file_read.readline()
            while line :
                s += line
                line = file_read.readline()
            s = Filter(s)#must be filter here,before split
            print type(s.split())
            L += (s.split())
    L.sort()#break
    print L
    L = set(L)
    L = list(L)
    L.sort()
    print L




def Filter ( S ) :
    """
    This function get a string and filter all the numbers,symbols
    and put all the characters in low case then return the list
    :return: A string which has been filtration(without number symbol and upper case)
    """

    S = list(S)# because String is unchangeable,so we use list
    #print S
    for i in range(len(S)) :
        if S[i].isalpha() :
            if S[i].isupper() :
                S[i] = S[i].lower()
        else :
            S[i] = ' '

    S = ''.join(S)
    #print S
    return S

Scan_Text ()

