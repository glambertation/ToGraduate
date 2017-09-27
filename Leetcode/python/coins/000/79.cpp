/*
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

*/

// 回溯
class Solution {
public:
    bool dfs(vector<vector<char>>& board,int y,int x, string word, int i){
        if (i == word.length()) return true;
        if(y<0 || x<0 || y == board.size() || x == board[y].size()) return false;
        if(board[y][x] != word[i]) return false;
        board[y][x] = '*';
        //std::cout<<board[y][x]<<endl;
        bool res = dfs(board, y , x+1, word, i+1) 
            || dfs(board, y, x-1, word, i+1)
            || dfs(board, y+1, x, word, i+1)
            || dfs(board, y-1, x, word, i+1);
        board[y][x] = word[i]  ;
        return res;    
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[i].size();j++){
                if(dfs(board, i, j, word, 0)) return true;
            }
        }
        return false;    
    }
};
