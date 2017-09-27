"""
    Heap Sort
    ---------
    Uses the max heap data structure implemented in a list.
    Time Complexity: O(n log n)
    Space Complexity: O(1) Auxiliary

    实际建堆的时间复杂度是O(n)
    又本身是在原数组上操作，所以空间复杂度是O(1)
"""


class Solution(object):
    def heap_max(self, nums, i, r):
        left = 2 * i + 1
        right = 2 * i + 2
        large = 0
        if left <= r and nums[i] < nums[left]:
            large = left
        else:
            large = i

        if right <= r and nums[large] < nums[right]:
            large = right

        if large != i:
            nums[i], nums[large] = nums[large], nums[i]
            self.heap_max(nums,large,r)


    def heap_build(self, nums):
        r = len(nums)-1
        for i in range(len(nums)//2, -1, -1):
            self.heap_max(nums, i, r)

    def sortColors(self, nums):
        self.heap_build(nums)
        r = len(nums)-1
        for i in range(len(nums)-1, 0 ,-1):
            nums[0], nums[i] = nums[i], nums[0]
            r=r-1
            self.heap_max(nums, 0, r)

''' python tips '''
'''
range(2, 0, -1) -> output 1
range(2, -1, -1) -> output 1 0

最后一个-1是倒序的意思
''' 
