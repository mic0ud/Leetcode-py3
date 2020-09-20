#
# @lc app=leetcode id=1039 lang=python3
#
# [1039] Minimum Score Triangulation of Polygon
#
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/
#
# algorithms
# Medium (44.32%)
# Likes:    262
# Dislikes: 31
# Total Accepted:    5.9K
# Total Submissions: 12.8K
# Testcase Example:  '[1,2,3]'
#
# Given N, consider a convex N-sided polygon with vertices labelled A[0], A[i],
# ..., A[N-1] in clockwise order.
# 
# Suppose you triangulate the polygon into N-2 triangles.  For each triangle,
# the value of that triangle is the product of the labels of the vertices, and
# the total score of the triangulation is the sum of these values over all N-2
# triangles in the triangulation.
# 
# Return the smallest possible total score that you can achieve with some
# triangulation of the polygon.

# Example 1:
 
# Input: [1,2,3]
# Output: 6
# Explanation: The polygon is already triangulated, and the score of the only
# triangle is 6.

# Example 2:

# Input: [3,7,4,5]
# Output: 144
# Explanation: There are two triangulations, with possible scores: 3*7*5 +
# 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.  The minimum score is 144.
 
# Example 3:

# Input: [1,3,1,4,1,5]
# Output: 13
# Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5
# + 1*1*1 = 13.

# Note:
# 
# 
# 3 <= A.length <= 50
# 1 <= A[i] <= 100


# @lc code=start
class Solution:
    def minScoreTriangulation(self, A: [int]) -> int:
        n = len(A)
        # dp[i][j]: res from A[i] to A[j](inclusive)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 0
            if i < n-1:
                dp[i][i+1] = 0
        # start from length of 3 
        for i in range(2, n+1):
            for j in range(n-i):
                for k in range(j,j+i+1):
                    tmp = dp[j][k] + dp[k][j+i] + A[j]*A[k]*A[j+i]
                    dp[j][j+i] = min(dp[j][j+i], tmp)
        return dp[0][-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minScoreTriangulation([1,3,1,4,1,5])
