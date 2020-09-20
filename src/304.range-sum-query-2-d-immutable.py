#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#
# https://leetcode.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (35.07%)
# Likes:    640
# Dislikes: 151
# Total Accepted:    90.2K
# Total Submissions: 255.1K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# Given a 2D matrix matrix, find the sum of the elements inside the rectangle
# defined by its upper left corner (row1, col1) and lower right corner (row2,
# col2).
# 
# 
# 
# The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
# and (row2, col2) = (4, 3), which contains sum = 8.
# 
# 
# Example:
# 
# Given matrix = [
# ⁠ [3, 0, 1, 4, 2],    [3, 3, 4, 8, 10]
# ⁠ [5, 6, 3, 2, 1],    [8, 14, 18, 24, 27]
# ⁠ [1, 2, 0, 1, 5],    [9, 2, 0, 1, 5]
# ⁠ [4, 1, 0, 1, 7],    [13, 1, 0, 1, 7]
# ⁠ [1, 0, 3, 0, 5]     [15, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# Note:
# 
# You may assume that the matrix does not change.
# There are many calls to sumRegion function.
# You may assume that row1 ≤ row2 and col1 ≤ col2.
# 
# 
#

# @lc code=start
class NumMatrix:

    def __init__(self, matrix: [[int]]):
        if not matrix or not matrix[0]:
            self.matrix = None
            return
        # matrix = matrix[0]
        self.matrix = matrix
        self.dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.dp[0][0] = matrix[0][0]
        if len(matrix) > 1:
            for i in range(1, len(matrix)):
                self.dp[i][0] = self.dp[i-1][0] + matrix[i][0]                
        if len(matrix[0]) > 1:
            for i in range(1, len(matrix[0])):
                self.dp[0][i] = self.dp[0][i-1] + matrix[0][i]
        if len(matrix) > 1 and len(matrix[0]) > 1:
            for i in range(1, len(matrix)):
                for j in range(1, len(matrix[0])):
                    self.dp[i][j] = self.dp[i-1][j] + self.dp[i][j-1] - self.dp[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.matrix:
            return 0
        
        return self.dp[row2][col2] - (self.dp[row2][col1-1] if col1 > 0 else 0) - (self.dp[row1-1][col2] if row1 > 0 else 0) + (self.dp[row1-1][col1-1] if col1 > 0 and row1 > 0 else 0)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end
# [2,1,4,3],[1,1,2,2],[1,2,2,4]
if __name__ == '__main__':
    s = NumMatrix([[-4,-5]])
    print(s.sumRegion(0,0,0,0))


# ["NumMatrix","sumRegion","sumRegion","sumRegion"]\n[[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]