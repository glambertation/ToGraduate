'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

BST
左子树 < 根节点 < 右子树
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, head, tail):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        slow = head
        fast = head
        if head == tail:
            return None
        
        while slow != tail and fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next
            fast = fast.next
            
        root = TreeNode(slow.val)
        root.left = self.dfs(head, slow)
        root.right = self.dfs(slow.next, tail)
        return root
    
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        return self.dfs(head, None)
    
