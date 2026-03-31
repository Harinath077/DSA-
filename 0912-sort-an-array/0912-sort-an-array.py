from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """ 
        --> heapify() : process of fixing the Binary Tree to follow the heap property
        """
        def heapify(n,i):
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if( left < n and nums[left] > nums[largest]):
                largest = left
            
            if( right < n and nums[right] > nums[largest]):
                largest = right
            
            # after swapping not vaild ( subtree )
            if(largest != i):
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n,largest)

        n = len(nums)

        # step 1 : build MaxHeap
        for i in range(n//2 - 1, -1, -1):
            heapify(n, i)
        
        # step 2 : extrack the each element and sort
        """ 
        --> Take max put into last pos ( don't touch is sorted)
        --> shrink the heap size
        --> fix Heap  ( heapify )
        """
        for i in range(n - 1, -1, -1):
            # take max put into last postition
            nums[0], nums[i] = nums[i], nums[0]
            # fix the heap
            heapify(i,0)
        
        return nums