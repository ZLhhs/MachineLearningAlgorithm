"""
Name   : NaiveBayes1.py (A NaiveBayes algorithm just for practice)
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
    This function read data from data1.txt then return it
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
    C_Y  = numpy.array([numpy.bincount( Data[:,-1] )]).shape[1]
    C_X1 = numpy.array([numpy.bincount( Data[:, 0] )]).shape[1]
    C_X2 = numpy.array([numpy.bincount( Data[:, 1] )]).shape[1]
    return C_Y,C_X1,C_X2

def Creat_Matrix (Data, Count_Y, Count_X1, Count_X2) :
    """
    This function use Data to creat 3 Matrix:Matrix_Y, Matrix_X1Y, Matrix_X2Y
    first creat 3 zero matrix,then scan the Data and count the number for every matrix
    :return:3 matrix,they are Matrix_Y(1*2), Matrix_X1Y(3*2), Matrix_X2Y(3*2)
    """
    Matrix_Y   = numpy.zeros( shape = (1,Count_Y) ) # creat zero matrix
    Matrix_X1Y = numpy.zeros( shape = (Count_X1,Count_Y) )
    Matrix_X2Y = numpy.zeros( shape = (Count_X2,Count_Y) )
    for key in Data : # count the number
        Matrix_Y[0][key[-1]] += 1
        Matrix_X1Y[key[0]][key[-1]] += 1
        Matrix_X2Y[key[1]][key[-1]] += 1
    #print Matrix_Y,Matrix_X1Y,Matrix_X2Y
    return Matrix_Y,Matrix_X1Y,Matrix_X2Y

def Calculate_Probability (Matrix_Y, Matrix_X1Y, Matrix_X2Y) :
    """
    This function is used to calculate the probability just divide by the sum of Y(Matrix_Y)
    :return:3 matrix : Matrix_Y, Matrix_X1Y, MatrixX2Y,
            all is use probablity to replace the count
    """
    Matrix_X1Y[:,0] = numpy.exp( Matrix_X1Y[:,0] / Matrix_Y[0][0] )
    Matrix_X2Y[:,0] = numpy.exp( Matrix_X2Y[:,0] / Matrix_Y[0][0] )
    Matrix_X1Y[:,1] = numpy.exp( Matrix_X1Y[:,1] / Matrix_Y[0][1] )
    Matrix_X2Y[:,1] = numpy.exp( Matrix_X2Y[:,1] / Matrix_Y[0][1] )
    # Here we use exp to avoid underflow to zero
    # Matrix_Y = Matrix_Y / numpy.sum(Matrix_Y)
    print '3 matrix is :\n',Matrix_Y
    print Matrix_X1Y
    print Matrix_X2Y
    return Matrix_Y, Matrix_X1Y, Matrix_X2Y

def Calculate_Probability_Laplace_Pmooth (Matrix_Y, Matrix_X1Y, Matrix_X2Y, Count_X1, Count_X2) :
    """
    This function is used to calculate the probability by the Laplace smooth
    compare with just divide by the sum of Y( Function Calculate_Probability() )
    :return:3 matrix : Matrix_Y, Matrix_X1Y, MatrixX2Y,
            all is use probablity to replace the count
    """
    Matrix_X1Y += 1  # <---  Laplace smooth
    Matrix_X2Y += 1
    Matrix_X1Y[:,0] = numpy.exp( Matrix_X1Y[:,0] / (Matrix_Y[0][0]+Count_X1) )
    Matrix_X2Y[:,0] = numpy.exp( Matrix_X2Y[:,0] / (Matrix_Y[0][0]+Count_X2) )
    Matrix_X1Y[:,1] = numpy.exp( Matrix_X1Y[:,1] / (Matrix_Y[0][1]+Count_X1) )
    Matrix_X2Y[:,1] = numpy.exp( Matrix_X2Y[:,1] / (Matrix_Y[0][1]+Count_X2) )
    # Here we use exp to avoid underflow to zero;
    # add count_X is to Laplace smooth
    Matrix_Y += 1 # add one to Matrix_Y at least
    print '3 matrix is :\n',Matrix_Y
    print Matrix_X1Y
    print Matrix_X2Y
    return Matrix_Y, Matrix_X1Y, Matrix_X2Y

def Prediction (Matrix_Y, Matrix_X1Y, Matrix_X2Y, test_case) :
    """
    This function prediction the test_case use NaiveBayes Algorithm
    and just return the label which one is bigger
    :return: the label test_case should be(use NaiveBayes Algorithm)
    """
    Py0 = Matrix_Y[0][0] * Matrix_X1Y[test_case[0]][0] * Matrix_X2Y[test_case[1]][0]
    Py1 = Matrix_Y[0][1] * Matrix_X1Y[test_case[0]][1] * Matrix_X2Y[test_case[1]][1]
    # Naive Bayes Algorithm
    print 'here the Py0,Py1 = ',Py0,Py1
    return 0 if Py0 > Py1 else 1


Data = Read_Data()
print 'Data:\n',Data,type(Data)
Count_Y, Count_X1, Count_X2 = Count_Data( Data )
#print Count_Y,Count_X1,Count_X2
Matrix_Y,Matrix_X1Y,Matrix_X2Y = Creat_Matrix(Data, Count_Y, Count_X1, Count_X2)
#Matrix_Y,Matrix_X1Y,Matrix_X2Y = Calculate_Probability (Matrix_Y, Matrix_X1Y, Matrix_X2Y)
Matrix_Y,Matrix_X1Y,Matrix_X2Y = Calculate_Probability_Laplace_Pmooth (Matrix_Y, Matrix_X1Y, Matrix_X2Y, Count_X1, Count_X2)
test_case = [1,1] # user can change the test_case if necessary
print '\nfor test_case',test_case,',our prediction is :',\
    Prediction (Matrix_Y, Matrix_X1Y, Matrix_X2Y, test_case)