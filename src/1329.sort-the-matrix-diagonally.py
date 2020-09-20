#
# @lc app=leetcode id=1329 lang=python3
#
# [1329] Sort the Matrix Diagonally
#
# https://leetcode.com/problems/sort-the-matrix-diagonally/description/
#
# algorithms
# Medium (77.97%)
# Likes:    238
# Dislikes: 83
# Total Accepted:    12.5K
# Total Submissions: 16.1K
# Testcase Example:  '[[3,3,1,1],[2,2,1,2],[1,1,1,2]]'
#
# Given a m * n matrix mat of integers, sort it diagonally in ascending order
# from the top-left to the bottom-right then return the sorted array.
# 
# 
# Example 1:
# 
# 
# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 100
# 1 <= mat[i][j] <= 100
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: [[int]]) -> [[int]]:
        # A[i][j] on the same diagonal have same value of i - j
        m, n = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = d[i-j].pop()
        return mat
# @lc code=end

