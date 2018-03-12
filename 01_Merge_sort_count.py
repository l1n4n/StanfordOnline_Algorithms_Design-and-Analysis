# Programming Question 1
# Download the text file here. (Right click and select "Save As...")
# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
# Your task is to compute the number of inversions in the file given.
#################################################################################################

# Piggybacking on merge sort algorithm to count the number of inversions
# author: NL

def merge_count(arr):
    if len(arr) <= 1:        
        return arr, 0
    else:
        cut = len(arr)//2
        left = arr[:cut]
        right = arr[cut:]
        left_sorted, l = merge_count(left)
        right_sorted, r = merge_count(right)
        # inductive step
        current = 0
        i = 0
        j = 0
        result = []
        while i < len(left_sorted) and j < len(right_sorted):
            if left_sorted[i] <= right_sorted[j]:                
                result.append(left_sorted[i])
                i += 1
            else:                
                result.append(right_sorted[j])
                j += 1
                current += len(left_sorted) - i
        while i < len(left_sorted):
            result.append(left_sorted[i])
            i += 1
        while j < len(right_sorted):
            result.append(right_sorted[j])
            j += 1
        
        return current + l + r