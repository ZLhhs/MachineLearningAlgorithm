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

def Read_Data () :
    """
    This function is read data from data1.txt then return it
    :return:
    """
    file_read = open('data1.txt')
    L = []
    line = file_read.readline().split()
    
    print line,type(line)

Read_Data()