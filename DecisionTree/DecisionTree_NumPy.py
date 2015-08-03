__author__ = 'geteway'
import time
import numpy

def split_With_label(M, i):
    # M is X+Y and cut the 1'st cross
    #split the M by i'th label and return a list
    L, begin  = [], 0
    print 'in split before:',M,i
    M = M[ M[:,i].argsort() ]
    print 'in split after:',M
    count = numpy.bincount( M[:,i] )
    print count
    for value in count :
        L.append( M[begin:begin+value,:] )
        begin += value
    print 'L=:',L
    return L

def read_data () :
    X = []
    print 'X:',X,type(X)
    file_read = open('data2.txt')
    line = file_read.readline()
    while line :
        X.append( [int (v) for v in line.split()] )
        line = file_read.readline()
    X = numpy.array(X)
    return X[:,0:-1], numpy.array( [X[:,-1]] ).T

def creat_decision_tree (Xtrain, Ytrain, Tree) :
    print 'Tree:',Tree
    # can change Xtrain or Ytrain?
    ans = []
    print 'in creat:',Xtrain.shape,Ytrain.shape
    if all_right(Ytrain[1::,:]) : # cut the 1'st cross of Y
        return # only work for all zero and all one
    for i in range( Xtrain.shape[1] ) :
        #print 'in creat,ith zengyi is :',get_zengyi(Xtrain, Ytrain, i)
        ans.append( [ get_zengyi(Xtrain, Ytrain, i) , Xtrain[0][i]] )# add the label
    ans.sort()
    print ans
    split_label = ans[-1][1]
    print split_label
    for j in range(Xtrain.shape[1]) :
        if Xtrain[0][j] == split_label :
            print Xtrain[0][j],j
            break
    print j  # use column i to cut the MAT
    Tree[str(split_label)] = {}
    L = split_With_label( numpy.hstack((Xtrain[1:,:],Ytrain[1:,:])) , j)
    #print L
    for i in range(len(L)) :
        if all_right(L[i][:,-1]): #ok
            print 'in the all right............:',i,L[i]
            Tree[str(split_label)][L[i][0][j]] = {str(L[i][0][-1])}
        else :                           #0 to j
            Tree[str(split_label)][L[i][0][0]] = {}
            tempTree = Tree[str(split_label)][L[i][0][0]]
            tt1 = Xtrain[0,:]
            tt2 = L[i][:,0:-1]
            temp1 = numpy.vstack((tt1, tt2))
            #print numpy.array([Ytrain[0,:]]),numpy.array([L[i][:,-1]]).T
            tt1 = numpy.array([Ytrain[0,:]])
            tt2 = numpy.array([L[i][:,-1]]).T
            temp2 = numpy.vstack((tt1 , tt2))
            #print 'for temp:',temp1,temp2,L[i]
            temp1 = numpy.delete(temp1, numpy.s_[j], 1)
            #print 'temp1 = ',temp1
            creat_decision_tree(temp1 , temp2, tempTree)
        #break
        print L
    print 'Tree:',Tree



def get_zengyi(Xtrain, Ytrain, i):
    x,y =0,0
    x = shang(Ytrain[1:,:] )
    # vstack is down and hstack is in the right
    L = split_With_label( numpy.hstack((Xtrain[1:,:],Ytrain[1:,:])),i )
    for value in L :
        temp1 = float(value.shape[0])/(len(Ytrain)-1)
        temp2 = shang(numpy.array([value[:,-1]]).T)
        y += (temp1 * temp2)
    return x - y

def get_jini():
    pass

def shang(Ytrain):
    #Ytrain is cut the 1'st cross
    s = Ytrain.shape[0]
    c = numpy.bincount( Ytrain[:,0] )
    ans = 0
    for value in c :
        if value == 0:
            print 'value is zero!'
            continue
        ans += (-(float(value)/s*numpy.log(float(value)/s)))
    return ans

def all_right (Ytrain) :
    #onlg work for all zero and all one
    print 'in all_right,Y=:',Ytrain
    if numpy.sum(Ytrain) == len(Ytrain):
        return True
    elif numpy.sum(Ytrain) == 0:
        return True
    return False

start = time.clock()
Tree = {} #have a try
Xtrain, Ytrain = read_data()# The first cross is label not the data
print 'Xtrain,Ytrain:',Xtrain,Ytrain,Xtrain.shape,Ytrain.shape
creat_decision_tree(Xtrain, Ytrain, Tree)
#print split_With_label(numpy.hstack( (Xtrain[1:,:],Ytrain[1:,:]) ), 0)
print time.clock() - start