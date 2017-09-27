'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

前序中序确定一棵树
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
    
    def dfs(self, preorder, inorder, ps, pe, ist, ie):
        print ps, pe, ist, ie
        if pe < ps or ie < ist:
            return None
        root = TreeNode(preorder[ps])
        pos = 0
        for i in range(ist, ie+1, 1):
            if root.val == inorder[i]:
                pos = i
                break
        num = pos - ist
        root.left = self.dfs(preorder, inorder, ps + 1, ps + num, ist, pos - 1)
        root.right = self.dfs(preorder, inorder, ps + num +1, pe, pos + 1 , ie)
        return root
        
