#!/bin/python3
from array import *


def aVeryBigSum(arr):
   sum = 0
   for x in arr:
       sum = sum + x 
   return sum 

if __name__ == "__main__":
    arr = array('i', [1, 1, 1])
    print("A soma dos elementos do array eh %s" % aVeryBigSum(arr))
    