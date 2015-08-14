"""
Author :  LiangZHANG
Date   :  2015-8-13
E-mail :  Liangzxdu@foxmail.com

Introduction: This program is using the Logistic Regression algorithm to predication
"""

import numpy
import matplotlib.pyplot

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
    train = train.astype(numpy.float)
    print train,train.shape
    Xtrain = train[ :,:-1 ]
    Xtrain = numpy.hstack( [ numpy.ones(shape=(Xtrain.shape[0],1)), Xtrain] )
    Ytrain = numpy.array ( [train[ :,-1 ]] ).T
    print Xtrain,Xtrain.shape,Ytrain.shape
    file_read.close()

    file_read = open(address2)
    l = file_read.readlines()
    l = [ key.split() for key in l ]
    test = numpy.array( l )
    test = test.astype(numpy.float)
    Xtest = test[ :,:-1 ]
    Xtest = numpy.hstack( [numpy.ones( shape=(Xtest.shape[0], 1) ), Xtest] )
    Ytest = numpy.array( [test[ :, -1]] ).T
    print Xtest.shape,Ytest.shape
    return Xtrain,Ytrain,Xtest,Ytest


def Initialization ( Xtrain ) :
    theta = numpy.ones( (Xtrain.shape[1] ,1) )
    theta = numpy.random.rand( Xtrain.shape[1] ,1 )
    # all zeros or all ones
    return theta


def Batch_Gradient_Descent (N, Xtrain, Ytrain, alpha, theta, lam) :
    """

    :return:
    """
    m = Xtrain.shape[0]; count_I = []; count_J = [];
    print "------- Before Batch_Gradient_Descent -------"
    print "The parameter is: N=",N,"alpha=",alpha,"lam=",lam
    print "Xtrain:",Xtrain.shape,"Ytrain:", Ytrain.shape,"theta:", theta.shape
    for i in range(N) :
        temp = numpy.dot( Xtrain.T, (sigmoid(Xtrain ,theta)-Ytrain) )
        theta = theta - alpha/m*( temp )
        J = getCost(Xtrain, Ytrain, theta, m)
        print "i = ",i,"J = ",J
        count_I.append(i)
        count_J.append(J[0][0])
        #break
    print "count_I:",count_I
    print "count_J:",count_J
    #count_I = [1,2,3]
    #count_J = [1,4,9]
    matplotlib.pyplot.plot(count_I, count_J)
    matplotlib.pyplot.show()
    return theta

def sigmoid(Xtrain, theta) :
    #print "in sigmoid:",Xtrain.shape,theta.shape
    #print "the type:Xtrain:",type(Xtrain[1][1]),"",type(theta[1][0])
    temp = -numpy.dot(Xtrain, theta)
    return 1.0/(1+numpy.exp(temp))

def getCost(Xtrain, Ytrain, theta, m) :
    J = numpy.dot( numpy.dot((Ytrain-1).T, Xtrain), theta)
    Z = numpy.dot( Xtrain, theta )
    #print "J shape:",J.shape,"Z shape:",Z.shape
    for line in Z :
        J -= numpy.log(1+numpy.exp(-line))
    return -J/m

def Predicition (Xtest, Ytest, theta) :
    """
    """
    print "In predicition:",Xtest.shape,Ytest.shape,theta.shape
    pre = numpy.array([[ 1 if x>0 else 0 for x in numpy.dot(Xtest, theta) ]]).T
    print pre
    print Ytest
    print numpy.sum((pre == Ytest))/float(Xtest.shape[0])




Xtrain, Ytrain, Xtest, Ytest = Read_Data()
N = 35000; alpha = 0.0003; lam = 0; #contral
theta = Initialization( Xtrain )
theta = Batch_Gradient_Descent(N, Xtrain, Ytrain, alpha, theta, lam)
Predicition(Xtest, Ytest, theta)
print "end~"