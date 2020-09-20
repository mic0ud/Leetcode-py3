#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
#
# algorithms
# Medium (68.95%)
# Likes:    873
# Dislikes: 18
# Total Accepted:    58.8K
# Total Submissions: 80.6K
# Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [
# [0,1,1,1],
# [1,1,1,1],
# [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# 
# 
# Example 2:
# 
# 
# Input: matrix = 
# [
# ⁠ [1,0,1],
# ⁠ [1,1,0],
# ⁠ [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
# 
# 
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: [[int]]) -> int:
    # Explanation
    # dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
    # dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.

    # If A[i][j] == 0, no possible square.
    # If A[i][j] == 1,
    # we compare the size of square dp[i-1][j-1], dp[i-1][j] and dp[i][j-1].
    # min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1 is the maximum size of square that we can find.
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1
        res = sum(map(sum, dp))
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
