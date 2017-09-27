'''

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

'''

'''什么鬼..'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        buckets = {}
        for i, v in enumerate(nums):
            bucketNum, offset = (v / t, 1) if t else (v, 0)
            for idx in xrange(bucketNum - offset, bucketNum + offset +1):
                if idx in buckets and abs(buckets[idx] - nums[i]) <= t:
                    return True
                
            buckets[bucketNum] = nums[i]
            if len(buckets) > k:
                del buckets[nums[i - k]/t if t else nums[i - k]]
        return False
    
        
