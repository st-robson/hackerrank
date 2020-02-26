#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    for x in range(n):
        step = "#"*(x + 1)     
        print(step.rjust(n))

if __name__ == "__main__":
    staircase(6)
