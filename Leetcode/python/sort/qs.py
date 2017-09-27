"""
    Quick Sort
    ----------
    Uses partitioning to recursively divide and sort the list
    Time Complexity: O(n^2) worst case, O(nlgn) common case
    Space Complexity: O(1) this version
"""

class Solution(Object):
    def partition(self, nums, p, r):
        x = nums[r]
        i = p-1
        for i in range(p, r, 1):
            if nums[i] < x:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i+1

    def qs(self, nums, p ,r):
        if p < r:
            q = partition(nums, p, r)
            qs(nums, p, q-1)
            qs(nums, q+1, r)

    def sortColors(self, nums):
        n = len(nums)-1
        qs(nums, 0, n)


"""
    < copyright nryoung >
    Quick Sort (https://github.com/nryoung/algorithms/blob/master/algorithms/sorting/quick_sort.py)
    ----------
    Uses partitioning to recursively divide and sort the list
    Time Complexity: O(n**2) worst case
    Space Complexity: O(n**2) this version
    Stable: No
    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.
"""
def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.
    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    if len(seq) <= 1:
        return seq
    else:
        pivot = seq[0]
        left, right = [], []
        for x in seq[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return sort(left) + [pivot] + sort(right)

