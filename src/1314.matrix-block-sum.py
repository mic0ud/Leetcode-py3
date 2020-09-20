#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#
# https://leetcode.com/problems/matrix-block-sum/description/
#
# algorithms
# Medium (72.61%)
# Likes:    287
# Dislikes: 57
# Total Accepted:    12.2K
# Total Submissions: 16.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a m * n matrix mat and an integer K, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j
# - K <= c <= j + K, and (r, c) is a valid position in the matrix.
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
# 
#

# @lc code=start
class Solution:
    def matrixBlockSum(self, mat: [[int]], K: int) -> [[int]]:
        m, n = len(mat), len(mat[0])
        dp, res = [[0 for _ in range(n+1)] for _ in range(m+1)], [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i+1][1] = mat[i][0] + dp[i][1]
        for j in range(n):
            dp[1][j+1] = mat[0][j] + dp[1][j]
        for i in range(1,m):
            for j in range(1,n):
                dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] + mat[i][j] - dp[i][j]
        for r in range(m):           
            for c in range(n):    
                i1, i2 = 0 if r-K < 0 else r-K, m-1 if r+K >= m else r+K            
                j1, j2 = 0 if c-K < 0 else c-K, n-1 if c+K >= n else c+K
                res [r][c] = dp[i2+1][j2+1] - dp[i2+1][j1] - dp[i1][j2+1] + dp[i1][j1]
        return res

    def matrixBlockSum_SLOW(self, mat: [[int]], K: int) -> [[int]]:
        m, n = len(mat), len(mat[0])
        presum_row = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                presum_row[i][j] = mat[i-1][j-1] + presum_row[i][j-1]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):           
            for c in range(n):    
                up, down = 0 if r-K < 0 else r-K, m-1 if r+K >= m else r+K            
                left, right = 0 if c-K < 0 else c-K, n-1 if c+K >= n else c+K
                for k in range(up, down+1):
                    res[r][c] += presum_row[k+1][right+1] - presum_row[k+1][left]
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]],2)
