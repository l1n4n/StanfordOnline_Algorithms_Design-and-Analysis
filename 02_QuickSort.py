# Programming Assignment 2
# GENERAL DIRECTIONS:
# Download the following text file (right click and select "Save As..."): QuickSort.txt
# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order. The integer in the row of the file gives you the  entry of an input array.
# Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.

# Programming Assignment 2 - Question 1
# For the first part of the programming assignment, you should always use the first element of the array as the pivot element.
# Programming Assignment 2 - Question 2
# Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element. 
# Programming Assignment 2 - Question 3
# Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.
#####################################################################################################

# Quick Sort algorithm with different choices of pivot
# author: NL
def quick_sort(arr, l, r, how):
    """how: how to choose the pivot
    1: always choose the first
    2: always choose the last
    3: always choose the median of the three[first, middle, last]
    """
    if r - l > 1:        
                  
        if how == 2:            
            arr[l], arr[r - 1] = arr[r - 1], arr[l]
        elif how == 3:
            m = median(arr, l, r)            
            arr[m], arr[l] = arr[l], arr[m]
        elif how != 1 and how != 2 and how != 3:
            raise ValueError('not valid value for how to choose pivot')
            
        p = partition(arr, l, r)
        left = quick_sort(arr, l, p-1, how)
        right = quick_sort(arr, p, r, how)
        # current comparision is the length of the input array(r-l) -1
        return left + right + (r-l-1)
    else:
        # the base case/ the leaves of the tree
        # only one or zero item left, so no comparison
        return 0
    
def partition(arr, l, r):
    """
    l: the starting point
    r: the end point
    return the index of the item that has been the pivot, this item is in its right place
    """
    
    pivot = arr[l]
    i = l + 1
    for j in range(l + 1, r):
        if arr[j] < arr[l]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[l], arr[i - 1] = arr[i - 1], arr[l]
    return i
   
    
def median(arr, l, r):
    """return the index of the median among the first, the last, and the middle item of an arr;
    if there are 2k items in the array, the middle one is the kth one 
    """
    # the middle index, e.g. 2,3,4,5,6,7, l = 2, r = 8, the middle 4 = (2 + 8 - 1) // 2
    m = (r + l - 1)//2
    i = r - 1
    if arr[l] <= arr[m] <= arr[r-1] or arr[r-1] <= arr[m] <= arr[l]:
        i = m
    elif arr[m] <= arr[l] <= arr[r-1] or arr[r-1] <= arr[l] <= arr[m]:
        i = l
    return i