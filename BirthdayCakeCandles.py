#!/bin/python3

def birthdayCakeCandles(ar):
   tallestCandle = sorted(ar, reverse=True)[0:1][0]
   return len(list(filter(lambda x: x == tallestCandle, ar)))

if __name__ == "__main__":
   print(birthdayCakeCandles([3, 2, 1, 3]))
