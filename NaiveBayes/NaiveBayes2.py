"""
Name   :  NaiveBayes2.py (Use NaiveBayes Algorithm for E-mail classification)
Author :  LiangZHANG
Date   :  2015-8-5
E-mail :  liangzxdu@foxmail.com

Introduction:
"""

import numpy
import os

def Scan_Text () :
    """
    This function scan all the text and split it
    :return: A sorted dictionary with all the words(from text) in it
    """
    L = [];  address = 'data2';
    for folder in os.listdir(address) :
        for Name_List in os.listdir(address+'/'+folder) :
            file_read = open(address+'/'+folder+'/'+Name_List)
            #print Name_List
            s = ''.join( file_read.readlines() )
            # read_lines() return a list with string in it (a line a string constitute a list)
            s = Filter(s)
            #must be filter here,before split,input a str and output a str
            L += (s.split()) # use += not the append
    L = list(set(L)) # change to set to except the same then back to list
    L.sort()
    print L
    return L



def Filter ( S ) :
    """
    This function get a string and filter all the numbers,symbols
    and put all the characters in low case then return a string
    :return: A string which has been filtration(without number,symbol and upper case)
    """
    S = list(S)# because String is unchangeable,so we use list
    for i in range(len(S)) : # list can change
        if S[i].isalpha() :
            if S[i].isupper() :
                S[i] = S[i].lower()
        else :
            S[i] = ' '
    S = ''.join(S) #from list to str
    return S # return a str


def Create_Matrix (L) :
    """
    This function create the count matrix.size:len(L)*2 and 1*2,
    one is the y count matrix and one is the word-y count matrix.
    from the train set just scan the text and count,then return 2 matrix
    :return:2 matrix,y count matrix and word-y count matrix
    """
    Matrix_Y     = numpy.zeros( shape = (1, 2) )
    Matrix_WordY = numpy.zeros( shape = (len(L), 2) )
    address = 'data2/TrainSet'
    for file in os.listdir( address ) :
        print address+'/'+file
        file_read = open(address+'/'+file)
        flag = file_read.readline().strip() # cut the whitespace at the end or first
        line = ''.join( file_read.readlines() )
        line = Filter(line)  #print line
        l = line.split()  #print l
        for key in l :
            Matrix_WordY[L.index(key)][int(flag)] += 1
        Matrix_Y[0][int(flag)] += 1
    print Matrix_Y
    print Matrix_WordY
    return Matrix_Y, Matrix_WordY

def Calculate_Probability (L, Matrix_WordY) :
    """
    This function calculate the probability from the two count matrix
    ( Matrix_Y and Matrix_WordY ) by divide the sum of each other
    also we use Laplace smooth and exp/log to except the 0
    then return two probability matrix
    :return:2 probability matrix: Matrix_Y and Matrix_WordY
    """
    count_word = len(L)
    count_word0 = numpy.sum( Matrix_WordY[:,0] )
    count_word1 = numpy.sum( Matrix_WordY[:,1] )
    #print count_word,count_word0,count_word1
    Matrix_WordY[:, 0] /= count_word0
    Matrix_WordY[:, 1] /= count_word1
    print Matrix_WordY
    # without Laplace smooth and exp/log -------
    return Matrix_WordY

def Prediction (Matrix_Y, Matrix_WordY) :
    """
    This function read the test set and use NaiveBayes Algorithm to classification E-mail
    first process the E-mail text,then calculate the probability of P(spam|X) and P(ham|X)
    compare with the answer and get the accuracy
    :return: NULL
    """
    address = 'data2/TestSet'; count_wrong = 0; count_all = 0;
    for file in os.listdir(address) :
        count_all += 1
        file_read = open(address+'/'+file)
        flag = file_read.readline().strip()
        line = ''.join( file_read.readlines() )
        line = Filter(line)
        l = line.split()
        print l
        P0 = Matrix_Y[0][0] ; P1 = Matrix_Y[0][1]
        print P0, P1
        for key in l :
            P0 *= Matrix_WordY[L.index(key)][0]
            P1 *= Matrix_WordY[L.index(key)][1]
        print P0, P1
        pre_ans = 0 if P0>P1 else 1
        print 'predicition is :', pre_ans
        print 'real ans is:', int(flag)
        if int(flag)!=pre_ans : # predoction is wrong
            print line
            count_wrong += 1
    print float(count_wrong)/count_all





L = Scan_Text ()
Matrix_Y, Matrix_WordY = Create_Matrix(L)
Matrix_WordY = Calculate_Probability(L, Matrix_WordY)
Prediction(Matrix_Y, Matrix_WordY)