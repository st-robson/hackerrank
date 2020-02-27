#!/bin/python3

def miniMaxSum(arr):
    min = 0
    max = 0
    for i in sorted(arr)[0:4]:
       min += i
   
    for i in sorted(arr, reverse=True)[0:4]:
        max += i

    print("%s %s" % (min, max))

if __name__ == "__main__":
    miniMaxSum([1, 3, 5, 7, 9])
