"""
Author :  LiangZHANG
Date   :  2015-8-13
E-mail :  Liangzxdu@foxmail.com

Introduction: This program is using the Logistic Regression algorithm to predication.
              We use Gradient descent algorithm to find the best Theta(all ones at first)
              then using Theta to prediction. N is the times for iteration,
              alpha is the speed for learning algorithm,lam is the parameter for regularization
              J is the (value for) cost function.
              At first,we only use batch gradient descent to optimization theta and
              the regularization is closed.then we will try random gradient descent
              to let algorithm become fast and open the regularization.
"""

import numpy
import matplotlib.pyplot

def Read_Data () :
    """
    This function is reading data from the data directory(just in this project and named "data")
    From string -> list -> numpy.array,then return the Xtrain, Ytrain, Xtest, Ytest matrix.
    :return:4 matrix(numpy.array),there are Xtrain, Ytrain, Xtest, Ytest
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
    """
    This is used to initialized theta,and at first Theta is all ones.
    :return:the Theta which has been initialized to all ones matrix( Xtrain.shape[1]*1 )
    """
    theta = numpy.ones( (Xtrain.shape[1] ,1) ) # always  be ones
    #theta = numpy.random.rand( Xtrain.shape[1] ,1 )
    # all zeros or all ones
    return theta


def Batch_Gradient_Descent (N, Xtrain, Ytrain, alpha, theta, lam) :
    """
    This function is learning the best theta using batch gradient descent
    N is the number of iteration,Xtrain and Ytrain are both the train data,
    alpha is the speed of learning algorithm,lam is control regularization
    :return:The best theta we have find~
    """
    mtrain, mtest = Xtrain.shape[0], Xtest.shape[0];
    count_I, count_Jtrain, count_Jtest = [], [], [];
    count_accuracy_train, count_accuracy_test = [], [];
    count_f_train, count_f_test = [], [];
    print "------- Before Batch_Gradient_Descent -------"
    print "The parameter is: N=",N,"alpha=",alpha,"lam=",lam
    #print "Xtrain:",Xtrain.shape,"Ytrain:", Ytrain.shape,"theta:", theta.shape
    for i in range(N) :

        t = lam * theta
        t[0][0] = 0  # t is for regularization
        temp = numpy.dot( Xtrain.T, (sigmoid(Xtrain ,theta)-Ytrain) ) + t

        theta = theta - alpha/mtrain*( temp )  # gradient descent

        Jtrain = getCost(Xtrain, Ytrain, theta, mtrain) + regularization(lam, mtrain, theta)
        Jtest  = getCost(Xtest , Ytest , theta, mtest ) + regularization(lam, mtest, theta)
        accuracy_train, f_train = Predicition(Xtrain, Ytrain, theta)
        accuracy_test , f_test  = Predicition(Xtest , Ytest , theta)
        print "i = ",i,"Jtrain = ",Jtrain,"Jtest = ",Jtest,"accuracyTrain=",accuracy_train,"accuracyTest=",accuracy_test,"Ftrain",f_train,"Ftest",f_test
        if i % 1 == 0:
            count_I.append(i)
            count_Jtrain.append(Jtrain[0][0])
            count_Jtest.append(Jtest[0][0])
            count_accuracy_train.append(100*accuracy_train)
            count_accuracy_test.append(100*accuracy_test)
            count_f_train.append(100*f_train)
            count_f_test.append( 100*f_test )

    return theta, count_I, count_Jtrain, count_Jtest, count_accuracy_train, count_accuracy_test, count_f_train, count_f_test

def sigmoid(Xtrain, theta) :
    """
    Just the calculate the sigmoid function: y = 1/( 1+exp(-x) ), x=Xtrain*theta
    """
    #print "in sigmoid:",Xtrain.shape,theta.shape
    #print "the type:Xtrain:",type(Xtrain[1][1]),"",type(theta[1][0])
    temp = -numpy.dot(Xtrain, theta)
    return 1.0/(1+numpy.exp(temp))

def getCost(Xtrain, Ytrain, theta, m) :
    """
    Calculate the value of cost function,you can find the formula of J(cost function)
    in folder 'design_photo' in this project.
    return the value of J(the cost function)
    """
    J = numpy.dot( numpy.dot((Ytrain-1).T, Xtrain), theta)
    Z = numpy.dot( Xtrain, theta )
    #print "J shape:",J.shape,"Z shape:",Z.shape
    for line in Z :
        J -= numpy.log(1+numpy.exp(-line))
    return -J/m

def regularization(lam, m, theta) :
    """
    lam/2m * ( theta*theta - theta[0]**2 )
    """
    temp = lam/(2.0*m)
    temp *= (numpy.dot(theta.T, theta)-theta[0][0]**2)
    return temp


def Predicition (X, Y, theta) :
    """
    use theta which we have learned before to prediction in the test dataset.
    just calculate Xtest*theta, if the value is >0 then return 1 else return 0,
    at least,we calculate the accuracy.
    """
    #print "In predicition:",Xtest.shape,Ytest.shape,theta.shape
    pre = numpy.array([[ 1 if key>0 else 0 for key in numpy.dot(X, theta) ]]).T
    pre_matrix =  numpy.hstack( [Y, pre]) # real - pre
    count_tp, count_fn, count_fp = 0, 0, 0
    for key in (pre_matrix) :
        if key[0]==1 and key[1]==1 :
            count_tp += 1
        elif key[0]==1 and key[1]==0 :
            count_fn += 1
        elif key[0]==0 and key[1]==1 :
            count_fp += 1
    p = float(count_tp)/(count_tp+count_fp)
    r = float(count_tp)/(count_tp+count_fn)
    return numpy.sum((pre == Y))/float(X.shape[0]),2.0*p*r/(p+r)



Xtrain, Ytrain, Xtest, Ytest = Read_Data()
N = 250000; alpha = 0.0004; lam = 400; # some control parameter
theta = Initialization( Xtrain )
theta, count_I, count_Jtrain, count_Jtest, count_accuracy_train, count_accuracy_test, count_f_train, count_f_test = Batch_Gradient_Descent(N, Xtrain, Ytrain, alpha, theta, lam)
print "end, max accuracy = 761194029%"

p1, = matplotlib.pyplot.plot(count_I, count_Jtrain)
p2, = matplotlib.pyplot.plot(count_I, count_Jtest )
p3, = matplotlib.pyplot.plot(count_I, count_accuracy_train)
p4, = matplotlib.pyplot.plot(count_I, count_accuracy_test)
p5, = matplotlib.pyplot.plot(count_I, count_f_train)
p6, = matplotlib.pyplot.plot(count_I, count_f_test)
matplotlib.pyplot.ylabel('Cost')
matplotlib.pyplot.xlabel('Iterations')
matplotlib.pyplot.title('Different iterations for LR cost and accuracy:N=%d,alpha=%f,lambda=%f' %(N,alpha,lam))
matplotlib.pyplot.legend([p1, p2, p3, p4, p5, p6], ["Jtrain", "Jtest", "accuracyTrain", "accuracyTest", "FTrain", "FTest"])
matplotlib.pyplot.show()