# Programming Assignment 6 - Question 2
# Download the following text file: Median.txt
# The goal of this problem is to implement the "Median Maintenance" algorithm
# In the box below you should type the sum of these 10000 medians, modulo 10000
#################################################################################

# Using two heaps to maintain the median
# python's heapq module implements the min heap
# two ways to implement the max heap: 1) from scrach 2) piggyback on the heapq module. Here I use 1). 
# author: NL

class max_heap:
    def __init__(self):
        self.heaplist = [0] # 0 is a placeholder, not part of the heap; it is more convenient to calculate the indices
        self.size = 0
        
    def insert(self, item):
        self.heaplist.append(item)
        self.size += 1
        self.percUp(self.size)
        
    def percUp(self, i):
        while i // 2 > 0:
            if self.heaplist[i] > self.heaplist[i // 2]: # child is larger than its parent
                self.heaplist[i], self.heaplist[i // 2]  = self.heaplist[i // 2], self.heaplist[i]
            i = i // 2
            
    def delMax(self):
        """delete the max and return it, maintaining the heap order
        """
        max_item = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size]
        self.size -= 1
        del self.heaplist[-1]
        self.percDown(1)
        return max_item
        
    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.max_child(i)
            if self.heaplist[i] < self.heaplist[mc]:
                self.heaplist[i], self.heaplist[mc] = self.heaplist[mc], self.heaplist[i]
            i = mc
            
    def max_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heaplist[i * 2] > self.heaplist[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def build_max_Heap(self, alist):
        i = len(alist) // 2
        self.size = len(alist)
        self.heaplist = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

#############################################################################################################
import heapq
# the main process of output the median
# stream = list of integers

initial = stream.pop(0)
# initialize heap_low using my implement max_heap.heapify([stream.pop(0)])
heap_low = max_heap()
heap_low.insert(initial)

# initialize heap_high using python's built-in heapq.heapify([])
heap_hi = []
heapq.heapify(heap_hi)
# initialize median_list = [stream.pop(0)] # the first one has to be added, otherwise there is nothing to be compared with
median_list = [initial]
# while len(stream) > 0, pop(0), insert it to the proper heap, keep two heaps differ less than 1 in size, find the median, append the median to the median_list
while len(stream) > 0:    
    # proper heap? 
    # new = stream.pop(0), if new < heap_low[0], insert it to heap_low
    new = stream.pop(0)
    if new < heap_low.heaplist[1]:
        heap_low.insert(new)

    # if new >= heap_low[0], insert it to heap_hi
    if new >= heap_low.heaplist[1]:
        heapq.heappush(heap_hi, new)

    # keep size balanced?
    # if len(heap_low) > len(heap_hi) + 1
    if heap_low.size > len(heap_hi) + 1:

        # pop the max of heap_low, insert it to heap_high
        n = heap_low.delMax()
        heapq.heappush(heap_hi, n)

    # if len(heap_high) > len(heap_low) + 1
    if len(heap_hi) > heap_low.size + 1:

        # pop the min of heap_high, insert it to heap_low
        m = heapq.heappop(heap_hi)
        heap_low.insert(m)

    #find the median?
    # if len(heap_low) < len(heap_hi), median_list.append(heap_hi[0])
    if heap_low.size < len(heap_hi):
        median_list.append(heap_hi[0])

    # if len(heap_low) >= len(heap_hi), median_list.append(heap_low[0])
    else:
        median_list.append(heap_low.heaplist[1])


(sum(median_list)) % 10000