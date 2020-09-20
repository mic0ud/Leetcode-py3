#
# @lc app=leetcode id=1292 lang=python3
#
# [1292] Maximum Side Length of a Square with Sum Less than or Equal to Threshold
#
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/description/
#
# algorithms
# Medium (47.10%)
# Likes:    279
# Dislikes: 13
# Total Accepted:    10.8K
# Total Submissions: 22.4K
# Testcase Example:  '[[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]]\r\n4\r'
#
# Given a m x n matrix mat and an integer threshold. Return the maximum
# side-length of a square with a sum less than or equal to threshold or return
# 0 if there is no such square.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# Output: 2
# Explanation: The maximum side length of square with sum less than 4 is 2 as
# shown.
# 
# 
# Example 2:
# 
# 
# Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
# threshold = 1
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]],
# threshold = 40184
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= m, n <= 300
# m == mat.length
# n == mat[i].length
# 0 <= mat[i][j] <= 10000
# 0 <= threshold <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def maxSideLength(self, mat: [[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                presum[i+1][j+1] = presum[i+1][j] + presum[i][j+1] + mat[i][j] - presum[i][j]
        for k in range(min(m,n),1,-1):
            for i in range(k, m+1):
                for j in range(k, n+1):
                    tmp = presum[i][j] - presum[i][j-k] - presum[i-k][j] + presum[i-k][j-k]
                    if tmp <= threshold:
                        return k
        return 0
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], 1)
    s.maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184)
    s.maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6)
    s.maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
