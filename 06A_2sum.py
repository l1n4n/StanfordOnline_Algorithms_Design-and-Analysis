# Programming Assignment 6 - Question 1
# Download the following text file: algo1-programming_prob-2sum.txt
# The goal of this problem is to implement a variant of the 2-SUM algorithm
# The file contains 1 million integers, both positive and negative (there might be some repetitions!).This is your array of integers, with the ith row of the file specifying the ith entry of the array.
# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) such that there are distinct numbers x, y in the input file that satisfy x + y = t. 
#######################################################################################

# Instead of using hash table, a faster way is to sort the array first and then use the bisect module to search within a range
# author: NL

import bisect
total = set()
for x in a:
    
    low = bisect.bisect_left(a, - 10000 - x)
    high = bisect.bisect_right(a, 10000 - x)
    for y in a[low: high]:
        if y != x:
            total.add(x + y)
len(total) 
