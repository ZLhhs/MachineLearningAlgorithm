#This is not NumPy and SciPy
__author__ = 'geteway'
import time
import math

def read_data (D) :
    file_input = open('data1.txt')
    line = file_input.readline()
    while line :
        D.append(line.split())
        line = file_input.readline()

def data_clean(D) :
    for i in range(len(D)) :
        D[i][0] = float(D[i][0])
        D[i][1] = float(D[i][1])
        D[i][2] = float(D[i][2])
        if D[i][3] == 'largeDoses' :
            D[i][3] = 2
        elif D[i][3] == 'smallDoses' :
            D[i][3] = 1
        else :         #didntLike
            D[i][3] = 0
    large0,small0,large1,small1,large2,small2 = D[0][0],D[0][0],D[0][1],D[0][1],D[0][2],D[0][2]
    for i in D :
        if i[0]>large0 :
            large0 = i[0]
        elif i[0]<small0 :
            small0 = i[0]
        if i[1]>large1 :
            large1 = i[1]
        elif i[1]<small1 :
            small1 = i[1]
        if i[2]>large2 :
            large2 = i[2]
        elif i[2]<small2 :
            small2 = i[2]
    for i in range(len(D)) :
        D[i][0] = (D[i][0]-small0)/(large0-small0)
        D[i][1] = (D[i][1]-small1)/(large1-small1)
        D[i][2] = (D[i][2]-small2)/(large2-small2)

def creat_trainSet_testSet(D,train_set,test_set,T) :
    for i in range(len(D)) :
        if i % T == 0 :
            test_set.append(D[i])
        else :
            train_set.append(D[i])

def solve(train_set, test_set, ans, K) :
    for x in test_set :
        dis = []
        for y in train_set :
            dis.append( [get_dis(x,y,2),y[3]] )
        dis.sort()
        ans.append(get_ans(dis, K))

def get_dis(x, y, k) :
    return ( abs(x[0]-y[0])**k + abs(x[1]-y[1])**k + abs(x[1]-y[1])**k )

def get_ans (dis, K) :
    c0,c1,c2 = 0,0,0
    for i in range(K) :
        if dis[i][1] == 0:
            c0+=1
        elif dis[i][1]==1:
            c1+=1
        elif dis[i][1]==2:
            c2+=1
    cc = max(c0,c1,c2)
    if cc == c0 :  return 0
    elif cc == c1: return 1
    else :         return 2

def precision(ans, test_set) :
    assert (len(ans) == len(test_set))
    c = 0
    for i in range(len(ans)) :
        if ans[i] == test_set[i][3] :
            c+=1
    return float(c)/len(ans)

start = time.clock()
D = []
train_set, test_set, ans = [],[],[]

K, T = 20, 5 # the K of the K-NN, T is divide data to train and test
read_data(D)
data_clean(D)
creat_trainSet_testSet(D,train_set,test_set,T)
solve(train_set , test_set, ans, K)
end = time.clock()
print 'train test ans',len(train_set),len(test_set),len(ans)
print precision(ans, test_set)
print end - start
print 'No NumPy'