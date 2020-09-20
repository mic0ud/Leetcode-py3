#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (48.04%)
# Likes:    740
# Dislikes: 164
# Total Accepted:    39.5K
# Total Submissions: 81.7K
# Testcase Example:  '3\n2\n0\n0'
#
# On an NxN chessboard, a knight starts at the r-th row and c-th column and
# attempts to make exactly K moves. The rows and columns are 0 indexed, so the
# top-left square is (0, 0), and the bottom-right square is (N-1, N-1).
# 
# A chess knight has 8 possible moves it can make, as illustrated below. Each
# move is two squares in a cardinal direction, then one square in an orthogonal
# direction.
# 
# 
# 
# 
# 
# 
# 
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
# 
# The knight continues moving until it has made exactly K moves or has moved
# off the chessboard. Return the probability that the knight remains on the
# board after it has stopped moving.
# 
# 
# 
# Example:
# 
# 
# Input: 3, 2, 0, 0
# Output: 0.0625
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
# 
# 
# 
# 
# Note:
# 
# 
# N will be between 1 and 25.
# K will be between 0 and 100.
# The knight always initially starts on the board.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        if K == 0:
            return 1
        dp = [[[0 for _ in range(K+1)] for _ in range(N)] for _ in range(N)]
        moves = [[[] for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                moves[i][j] = self.next_moves(i,j,N)
                dp[i][j][1] = len(moves[i][j])/8
        for k in range(2, K+1):
            for i in range(N):
                for j in range(N):   
                    next_ = moves[i][j]
                    for p,q in next_:     
                        dp[i][j][k] += (1/8)*dp[p][q][k-1]
        return dp[r][c][K]
        
    def next_moves(self, r, c, n) -> [[int]]:
        res = []
        if r-2 >= 0:
            if c-1 >= 0:
                res.append([r-2,c-1])
            if c+1 < n:
                res.append([r-2,c+1])
        if r-1 >= 0:
            if c-2 >= 0:
                res.append([r-1,c-2])
            if c+2 < n:
                res.append([r-1,c+2])
        if r+1 < n:
            if c-2 >= 0:
                res.append([r+1,c-2])
            if c+2 < n:
                res.append([r+1,c+2])
        if r+2 < n:
            if c-1 >= 0:
                res.append([r+2,c-1])
            if c+1 < n:
                res.append([r+2,c+1])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.knightProbability(1,0,0,0)
    s.knightProbability(25,100,0,0)
