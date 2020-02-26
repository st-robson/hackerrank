#! /bin/python3

from array import *

def plusMinus(arr):
    divvy = len(arr)
    negatives = array('i',filter(lambda x: x < 0, arr))
    zeros = array('i', filter(lambda x: x == 0, arr))
    positives = array('i',filter(lambda x: x > 0, arr))
    return array('f', [(len(positives)/divvy), (len(negatives)/divvy), (len(zeros)/divvy)])

if __name__ == "__main__":
    print(plusMinus(array('i',[1, 1 ,0 , -1, -1])))
