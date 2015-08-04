__author__ = 'geteway'
"""
Name   : NaiveBayes1.py (A NaiveBayes algorithm for practice)
Author : LiangZHANG
Date   : 2015-8-4
E-mail : liangzxdu@foxmail.com

Introduction : This program is about the NaiveBayes algorithm for a simple example.
               The example is coming from 'data1.txt'(in this project)
               You can find more information about this program in 'NaiveBayes1_doc'(also in this project)
               And this program is based on Numpy
"""
import numpy
import time



def Read_Data () :
    """
    This function is read data from data1.txt then return it
    :return: A 2-D matrix with the type of numpy.ndarray
    """
    file_read = open('data1.txt')
    L = []
    line = file_read.readline().split()
    while line :  # always read until the file is empty.
        L.append([int(key) for key in line  ])
        line = file_read.readline().split()
    return numpy.array(L)  # change from list to 2D matrix and return it.


def Count_Data ( Data ) :
    """
    This function is used to count the diffient member in x1,x2 and y
    then return C_Y, C_X1, C_X2
    :return:Three int numbers:
            C_Y  is the count of different member of Y
            C_X1 is the count of different member of x1
            C_X2 is the count of different member of x2
    """
    #print type(numpy.array([numpy.bincount( Data[:,-1] )]))
    #print numpy.array([numpy.bincount( Data[:,-1] )]).shape
    C_Y  = numpy.array([numpy.bincount( Data[:,-1] )]).shape[1]
    C_X1 = numpy.array([numpy.bincount( Data[:, 0] )]).shape[1]
    C_X2 = numpy.array([numpy.bincount( Data[:, 1] )]).shape[1]
    return C_Y,C_X1,C_X2

Data = Read_Data()
print Data,type(Data)
Count_Y, Count_X1, Count_X2 = Count_Data( Data )
print Count_Y,Count_X1,Count_X2