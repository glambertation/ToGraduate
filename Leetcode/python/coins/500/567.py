'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
'''

'''
tips 滑动窗口
'''
v1

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        
        mp = [0]*26
        for x in A:
            mp[x] += 1
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(s1)]] -= 1
            if mp == window:
                return True
        return False

v2

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1, c2 = collections.Counter(s1), collections.Counter(s2[0:(len(s1)-1)])
        
        for i in range(len(s2)-len(s1)+1):
            c2[s2[i+len(s1)-1]] += 1
            if not (c1 -c2):
                return True
            c2[s2[i]] -= 1
        return False
