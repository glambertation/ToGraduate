'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

nlgn
'''

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        res = collections.Counter()
        for i, x in enumerate(nums):
            if x not in res :
                res[x] = i
            elif abs(i - res[x]) <= k:
                return True
            else:
                res[x] = i
        return False
