'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

'''

''' Tips
那么这道题抽象出来就是
前面为零 自己为零 后面为零 就可以插入了

加上是贪心，所以从头遍历一遍就行了。

为了方便一次遍历 改变了vector大小，push_back了一个数

不改变大小..没想到怎么做

'''

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        flowerbed.append(0)
        pre, nex, count = 0, 0, 0
        for i in range(length):
            nex = flowerbed[i+1]
            if pre== 0 and flowerbed[i] == 0 and nex == 0:
                count += 1
                flowerbed[i] = 1
            pre = flowerbed[i]
        return True if count>=n else False 
            
        
