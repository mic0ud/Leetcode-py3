#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (41.87%)
# Likes:    2263
# Dislikes: 66
# Total Accepted:    250.7K
# Total Submissions: 594K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#

# @lc code=start
import bisect
class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """ 
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False

        i = 0
        while target > matrix[i][n-1]:
            i += 1
        for i in range(i, m):
            p = bisect.bisect_right(matrix[i], target)
            if matrix[i][p-1] == target:
                return True
        return False
# @lc code=end
# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5
if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[5]], 5))
