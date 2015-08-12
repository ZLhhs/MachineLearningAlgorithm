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
            #must be filter here,before split,input a str and output a list
            L += s # use += not the append
            #print "here L=:",L
    L = list(set(L)) # change to set to except the same then back to list
    L.sort()
    #print "this is L:"
    #for key in L :
     #   print key
    return L


def Filter ( S ) :
    """
    This function get a string and filter all the numbers,symbols
    and put all the characters in low case then return a list
    and remove the stop word.
    :return: A list which has been filtration
            (without number,symbol and upper case and remove stop_words)
    """
    S = list(S)# because String is unchangeable,so we use list
    for i in range(len(S)) : # list can change
        if S[i].isalpha() :
            if S[i].isupper() :
                S[i] = S[i].lower()
        else :
            S[i] = ' '
    S = ''.join(S) #from list to str
    S_arr = S.split()
    S_arr = Remove_Stop_Word( S_arr ) # input list and return list
    return S_arr # return a list


def Remove_Stop_Word( S ):
    """
    This function receive a list (just the context of E-mail) and remove the stop_word
    in the list (using stop_words list) then,return the new list (without the stop_word)
    :return:a list without stop_word in it.
    """
    S_arr = S
    #print "before:",S_arr
    stop_words = \
    ["a"  ,"an"   ,"and"  ,"are" ,"as"  ,"at"  ,
     "be" ,"for"  ,"from" ,"has" ,"have","in"  ,
     "is" ,"it"   ,"of"   ,"on"  ,"or"  ,"that",
     "the","there","these","this","to"  ,"up"  ,
     "was","we"   ,"will" ,"with","you" ,"your",
     "am" ,"but"  ,"by"   ,"x"   ,"s"   ,"c"   ]
    #stop_words = []
    for stop_word in stop_words :
        if stop_word in S_arr :
            S_arr = [key for key in S_arr if key!=stop_word]
            #S_arr.remove(key)  # this is wrong and upper line is right!
    #print "after :",S_arr
    return S_arr

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
        #print address+'/'+file
        file_read = open(address+'/'+file)
        flag = file_read.readline().strip() # cut the whitespace at the end or first
        line = ''.join( file_read.readlines() )
        l = Filter(line)  #print line
        #l = line.split()  #print l
        for key in l :
            Matrix_WordY[L.index(key)][int(flag)] += 1
        Matrix_Y[0][int(flag)] += 1
    print Matrix_Y
    print Matrix_WordY
    for i in range(len(L)) :
        print L[i],Matrix_WordY[i][0],Matrix_WordY[i][1]

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

    #Matrix_WordY[:,0] = ( Matrix_WordY[:,0]+1 )/ (count_word0 + count_word) #this is Laplace Smooth
    #Matrix_WordY[:,1] = ( Matrix_WordY[:,1]+1 )/ (count_word1 + count_word)
    Matrix_WordY = numpy.exp( Matrix_WordY )

    print Matrix_WordY
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
        l = Filter(line)
        #l = line.split()
        print l
        P0 = Matrix_Y[0][0] ; P1 = Matrix_Y[0][1]
        for key in l :
            P0 *= Matrix_WordY[L.index(key)][0]
            P1 *= Matrix_WordY[L.index(key)][1]
        print "NO:",P0,"   YES:", P1
        pre_ans = 0 if P0>P1 else 1
        print 'Predicition is :', pre_ans
        print 'The real ans is:', int(flag)
        print
        if int(flag) != pre_ans : # if the predoction is wrong,do this
            print address+'/'+file
            print "\n\n-------The Prediction is wrong!-------\n"
            print l
            for key in l :
                print key,Matrix_WordY[L.index(key)][0],Matrix_WordY[L.index(key)][1]
            count_wrong += 1
            print "-----------------------------------------"
    print "\nThe error rate is :",float(count_wrong)/count_all





L = Scan_Text ()
Matrix_Y, Matrix_WordY = Create_Matrix(L)
Matrix_WordY = Calculate_Probability(L, Matrix_WordY)
Prediction(Matrix_Y, Matrix_WordY)
