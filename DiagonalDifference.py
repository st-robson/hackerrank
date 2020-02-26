#! /bin/python
from array import *

def diagonalDifference(arr):
    result = 0
    lineSize = len(arr[0])
    i = 0
    for x in range(lineSize):
        j = (lineSize - i) - 1
        result += arr[i] [x] - arr[i] [j]
        i += 1
    
    if result < 0:
        return result * -1
    else:
        return result

if __name__ == "__main__":
    inputArray = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    computedResult = diagonalDifference(inputArray)
    print("Result: %s" % computedResult)