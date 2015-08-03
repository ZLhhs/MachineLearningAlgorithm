__author__ = 'geteway'
import numpy
import random
import time

def read_data () :
    file_read = open('data2.txt')
    L  = []
    line = file_read.readline()
    while line :
        line = line.split()
        L.append( [float(i) for i in line] )
        line = file_read.readline()
    X = numpy.array(L)
    clean_data(X)
    return X

def clean_data(X) :
    min = numpy.array( [numpy.min( X[:,0:3],0 )] )
    max = numpy.array( [numpy.max( X[:,0:3],0 )] )
    print 'min max :',min,max
    print 'min and max shape:',min.shape,max.shape
    fenzi = X[:,0:3]-numpy.tile(min,(len(X),1))
    fenmu = numpy.tile(max,(len(X),1))-numpy.tile(min,(len(X),1))
    X[:,0:3] = (fenzi)/(fenmu)


def creat_train_test_set (X, K) :
    for i in range(len(X)) :
        j = random.randint(0,len(X)-1)
        #X[i],X[j] = X[j],X[i]  wrong
        #X[[i,j]] = X[[j,i]]   this way~
        temp = X[i]
        X[i] = X[j]
        X[j] = temp
    test_set = X[0:K,:]
    train_set = X[K:,:]
    return train_set,test_set

def get_dis(temp, Xtrain, k) :
    ans = numpy.array( [ (numpy.sum(numpy.abs(temp-Xtrain)**k,1)) ] )
    #print ans.shape
    return ans

def KNN(Xtrain,Xtest,Ytrain,Ytest,K) :
    ans = []
    for x in Xtest :
        temp = numpy.tile( x,(len(Xtrain),1) )
        dis = get_dis(temp, Xtrain, 2)
        hecheng = numpy.vstack( (dis,Ytrain) ).T
        dis_order = hecheng[ hecheng[:,0].argsort()]
        label =  numpy.argmax(numpy.bincount([ int(key) for key in dis_order[0:K,1]] ),0)
        ans.append(label)
    print numpy.sum(ans == Ytest)/float(len(ans))

start = time.clock()
T, K = 200,20
X = read_data()
train_set,test_set = creat_train_test_set(X, T)
print 'train_set test_set:',train_set.shape,test_set.shape
Xtrain,Ytrain,Xtest,Ytest = train_set[:,0:3],numpy.array([train_set[:,3]]),test_set[:,0:3],numpy.array([test_set[:,3]])
print 'Xtrain Xtest Ytrain Ytest:',Xtrain.shape,Xtest.shape,Ytrain.shape,Ytest.shape
KNN(Xtrain,Xtest,Ytrain,Ytest,K)
end = time.clock()
print end-start,'with NumPy'