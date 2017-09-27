'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

'''
'''
1.可以建堆，然后pop k次

2.可以二分，最小值是左上matrix【0】【0】，最大值是右下matrix【n-1】【n-1】
取这个中间值 作为mid
算一下mid是第几大的数
然后再和k比较
然后这里再二分
'''

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        start = matrix[0][0]
        end = matrix[-1][-1]
        mid = 0
        
        while start < end:
            mid = start + (end - start)/2
            count = 0
            for i in range(len(matrix)):
                j = len(matrix[i]) - 1
                while j >= 0 and matrix[i][j] > mid :
                    j -= 1
                count += j + 1
            if count < k:
                start = mid +1
            else:
                end = mid
        return start
