"""
Author :  LiangZHANG
Date   :  2015-8-13
E-mail :  Liangzxdu@foxmail.com

Introduction: This program is using the Logistic Regression algorithm to predication
"""

import numpy


def Read_Data () :
    """

    :return:
    """
    address1 = "data/train.txt"
    address2 = "data/test.txt"
    file_read = open(address1)
    l = file_read.readlines()
    l = [ key.split() for key in l ]
    train = numpy.array ( l )
    Xtrain = train[ :,:-1 ]
    Ytrain = numpy.array ( [train[ :,-1 ]] ).T
    print train,train.shape
    print Xtrain.shape,Ytrain.shape
    file_read.close()

    file_read = open(address2)
    l = file_read.readlines()
    l = [ key.split() for key in l ]
    test = numpy.array( l )
    Xtest = test[ :,:-1 ]
    Ytest = numpy.array( [test[ :, -1]] ).T
    print Xtest.shape,Ytest.shape
    return Xtrain,Ytrain,Xtest,Xtest


def Initialization () :
    theta = numpy.zeros( (2 ,2) )
    print theta



Read_Data()
Initialization()

