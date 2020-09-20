#
# @lc app=leetcode id=1253 lang=python3
#
# [1253] Reconstruct a 2-Row Binary Matrix
#
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
#
# algorithms
# Medium (37.16%)
# Likes:    84
# Dislikes: 9
# Total Accepted:    8.4K
# Total Submissions: 21.5K
# Testcase Example:  '2\n1\n[1,1,1]'
#
# Given the following details of a matrix with n columns and 2 rows :
# 
# 
# The matrix is a binary matrix, which means each element in the matrix can be
# 0 or 1.
# The sum of elements of the 0-th(upper) row is given as upper.
# The sum of elements of the 1-st(lower) row is given as lower.
# The sum of elements in the i-th column(0-indexed) is colsum[i], where colsum
# is given as an integer array with length n.
# 
# 
# Your task is to reconstruct the matrix with upper, lower and colsum.
# 
# Return it as a 2-D integer array.
# 
# If there are more than one valid solution, any of them will be accepted.
# 
# If no valid solution exists, return an empty 2-D array.
 
# Example 1:

# Input: upper = 2, lower = 1, colsum = [1,1,1]
# Output: [[1,1,0],[0,0,1]]
# Explanation: [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct
# answers.

# Example 2:

# Input: upper = 2, lower = 3, colsum = [2,2,1,1]
# Output: []

# Example 3:

# Input: upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# Output: [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
 
# Constraints:

# 1 <= colsum.length <= 10^5
# 0 <= upper, lower <= colsum.length
# 0 <= colsum[i] <= 2


# @lc code=start
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: [int]) -> [[int]]:
        res = [[],[]]
        for s in colsum:
            if s == 0:
                res[0].append(0)
                res[1].append(0)
            elif s == 1:
                if upper >= lower:
                    res[0].append(1)
                    res[1].append(0)
                    upper -= 1
                else:
                    res[0].append(0)
                    res[1].append(1)
                    lower -= 1
            elif s == 2:
                res[0].append(1)
                res[1].append(1)
                upper -= 1
                lower -= 1
        return res if upper == 0 and lower == 0 else []
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.reconstructMatrix(4,7,[2,1,2,2,1,1,1])
    s.reconstructMatrix(5,5,[2,1,2,0,1,0,1,2,0,1])
    s.reconstructMatrix(2,3,[2,2,1,1])
    s.reconstructMatrix(2,1,[1,1,1])
