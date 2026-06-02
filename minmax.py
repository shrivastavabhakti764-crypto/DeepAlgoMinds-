#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.

    
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sum = 0
    min_val = arr[0]
    max_val = arr [0]
    for i in arr:
        min_val= min(i,min_val)
        max_val = max(i,max_val)
        sum = sum + i
    print (sum - max_val , sum-min_val)     
        
    
       
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)