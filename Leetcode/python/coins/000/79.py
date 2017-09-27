'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
'''

'''
回溯
'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        col = len(board)
        row = len(board[0])
        for c in range(col):
            for r in range(row):
                if self.dfs(board, word,c, r, 0):
                    return True
        return False
    
    def dfs(self, board, word, y, x, i):
        if i == len(word):
            return True
        if y < 0 or x < 0 or y == len(board) or x == len(board[0]):
            return False
        if board[y][x] != word[i]:
            return False
        board[y][x] = '*'
        res = self.dfs(board, word, y+1, x, i+1) or self.dfs(board, word, y-1, x, i+1) or self.dfs(board, word, y, x+1, i+1) or self.dfs(board, word, y, x-1, i+1)
        board[y][x] = word[i]
        return res
                
        
