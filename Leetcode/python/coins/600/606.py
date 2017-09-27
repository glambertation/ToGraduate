'''
You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".
Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
'''


'''
树的遍历
开始的时候卡在了 括号怎么表示 以及 有点忘了遍历了

其实遍历还是要抽象出来看
t->val
left
right
然后在这个基础上 增加其他逻辑 return就好
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if not left and not right:
            return str(t.val)
        if not left:
            return str(t.val)+"()"+"("+right+")"
        if not right:
            return str(t.val)+"("+left+")"
        return str(t.val)+"("+left+")"+"("+right+")"
        
