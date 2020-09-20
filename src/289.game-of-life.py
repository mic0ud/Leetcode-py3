#
# @lc app=leetcode id=289 lang=python3
#
# [289] Game of Life
#
# https://leetcode.com/problems/game-of-life/description/
#
# algorithms
# Medium (49.30%)
# Likes:    1248
# Dislikes: 226
# Total Accepted:    142.2K
# Total Submissions: 287.4K
# Testcase Example:  '[[0,1,0],[0,0,1],[1,1,1],[0,0,0]]'
#
# According to the Wikipedia's article: "The Game of Life, also known simply as
# Life, is a cellular automaton devised by the British mathematician John
# Horton Conway in 1970."
# 
# Given a board with m by n cells, each cell has an initial state live (1) or
# dead (0). Each cell interacts with its eight neighbors (horizontal, vertical,
# diagonal) using the following four rules (taken from the above Wikipedia
# article):
# 
# 
# Any live cell with fewer than two live neighbors dies, as if caused by
# under-population.
# Any live cell with two or three live neighbors lives on to the next
# generation.
# Any live cell with more than three live neighbors dies, as if by
# over-population..
# Any dead cell with exactly three live neighbors becomes a live cell, as if by
# reproduction.
# 
# 
# Write a function to compute the next state (after one update) of the board
# given its current state. The next state is created by applying the above
# rules simultaneously to every cell in the current state, where births and
# deaths occur simultaneously.
# 
# Example:
# 
# 
# Input: 
# [
# [0,1,0],
# [0,0,1],
# [1,1,1],
# [0,0,0]
# ]
# Output: 
# [
# [0,0,0],
# [1,0,1],
# [0,1,1],
# [0,1,0]
# ]
# 
# 
# Follow up:
# 
# 
# Could you solve it in-place? Remember that the board needs to be updated at
# the same time: You cannot update some cells first and then use their updated
# values to update other cells.
# In this question, we represent the board using a 2D array. In principle, the
# board is infinite, which would cause problems when the active area encroaches
# the border of the array. How would you address these problems?


# @lc code=start
class Solution:
    def gameOfLife(self, board: [[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(i,j) -> int:
            res = 0
            neighbors = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
            for p,q in neighbors:
                if 0 <= p < m and 0 <= q < n and board[p][q] == 1:
                    res += 1
            return res
            
        m, n = len(board), len(board[0])
        cache = {} # {(i,j): 0, (i+1,j):1}
        for i in range(m+n-1):
            for j in range(i+1):
                row = min(j,m-1)
                col = i-row
                if col < n:
                    ones, tmp = count(row,col), 0
                    if board[row][col] == 1:
                        if ones == 2 or ones == 3:
                            tmp = 1
                    else:
                        if ones == 3:
                            tmp = 1
                    cache[(row,col)] = tmp
            for c in list(cache.keys()):
                if c[0]+c[1] + 2 < i:
                    board[c[0]][c[1]] = cache[c]
                    cache.pop(c)
        for c in cache.keys():
            board[c[0]][c[1]] = cache[c]
        return
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
