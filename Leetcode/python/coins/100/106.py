'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

后续中序确定一颗树

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.dfs(postorder, inorder, 0, len(postorder)-1, 0, len(inorder)-1)
    
    def dfs(self, postorder, inorder, ps, pe, ist, ie):
        if pe < ps or ie < ist:
            return None
        root = TreeNode(postorder[pe])
        pos = 0
        for i in range(ist, ie+1, 1):
            if inorder[i] == root.val:
                pos = i
                break
        num = pos - ist
        
        root.left = self.dfs(postorder, inorder, ps, ps + num - 1, ist, pos - 1)
        root.right = self.dfs(postorder, inorder, ps + num, pe - 1, pos + 1, ie)
        
        return root
        
        
