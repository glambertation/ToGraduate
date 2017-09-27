''' 
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

'''
链表加法 转化成list/stack pop出来相加
每次节点都插在后面 :
res = ListNode(0)
res.next = root
root = res

'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ll1, ll2 = [], []
        while l1:
            ll1.append(l1.val)
            l1 = l1.next  
        while l2:
            ll2.append(l2.val)
            l2 = l2.next
        
        root = ListNode(0)
        reset = root
        carry = 0
        while ll1 or ll2 or carry:
            num = (ll1.pop() if ll1 else 0) + (ll2.pop() if ll2 else 0) + carry
            carry = num /10
            root.val = num % 10
            res = ListNode(0)
            res.next = root
            root = res

        return root.next
            
