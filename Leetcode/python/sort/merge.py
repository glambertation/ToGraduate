"""
    Merge Sort
    ----------
    Uses divide and conquer to recursively divide and sort the list
    Time Complexity: O(n log n)
    Space Complexity: O(n) Auxiliary
    在原数组上操作 但拷贝出了一份数组，所以空间复杂度是O(n)

"""

import sys
class Solution(object):
    def merging(self, nums, p, q, r):
        left = []
        right = []

        for i in range(p, q+1, 1):
            left.append(nums[i])
        left.append(sys.maxint)
        for i in range(q+1, r+1, 1):
            right.append(nums[i])
        right.append(sys.maxint)

        i, j, m = 0, 0, 0 
        for k in range(p, r+1, 1):
            if left[i] < right[j]:
                nums[m] = left[i]
                m += 1
                i += 1
            else:
                nums[m] = right[j]
                m += 1
                j += 1
    
    def mergesort(self, nums, p, r):
        if p < r:
            q = (p + r)/2
            self.mergesort(nums, p, q)
            self.mergesort(nums, q+1, r)
            self.merging(nums, p, q, r)

    def sortColor(nums):
        n = len(nums)-1
        mergesort(nums, 0, n)



"""
    < copyright nryoung >
    Merge Sort
    ----------
    Uses divide and conquer to recursively divide and sort the list
    Time Complexity: O(n log n)
    Space Complexity: O(n) Auxiliary 新建了数组
    Stable: Yes
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.
"""

class Solution(object):
    def merging(self, left, right):
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result += left[i:]
        result += right[j:]
        print "result:", result
        return result

    def mergesort(self, nums):
        if len(nums) <= 1:
            print "nums:", nums
            return nums
        
        mid = len(nums)//2
        left = self.mergesort(nums[:mid])
        right = self.mergesort(nums[mid:])
        return self.merging(left, right)
