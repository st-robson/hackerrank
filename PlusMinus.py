#! /bin/python3

from array import *
import math

def plusMinus(arr):
    divvy = len(arr)
    negatives = array('i',filter(lambda x: x < 0, arr))
    zeros = array('i', filter(lambda x: x == 0, arr))
    positives = array('i',filter(lambda x: x > 0, arr))
    print(round((len(positives)/divvy), 6)) 
    print(round((len(negatives)/divvy), 6)) 
    print(round((len(zeros)/divvy), 6)) 

if __name__ == "__main__":
    plusMinus(array('i',[1, 1 ,0 , -1, -1]))
