#
# @lc app=leetcode id=1139 lang=python3
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (44.82%)
# Likes:    107
# Dislikes: 30
# Total Accepted:    6.6K
# Total Submissions: 14.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
# 
#
# [1,1,1],
# [1,0,1],
# [1,1,1]
# @lc code=start
class Solution:
    def largest1BorderedSquare(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        # visited = [[False for _ in range(n)] for _ in range(n)]
        def search(i,j,row=True) -> int:
            res = 1
            if row:
                k = j+1
                while k < n and grid[i][k] == 1:
                    res += 1
                    k += 1
            else:
                k = i+1
                while k < m and grid[k][j] == 1:
                    res += 1
                    k += 1
            return res

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    left = search(i,j)
                    down = search(i,j,False)
                    for k in range(min(left,down),0,-1):
                        if search(i,j+k-1,False) >= k and search(i+k-1,j) >= k:
                            res = max(res, k*k)
        return res
# @lc code=end
# [1,1,1],
# [1,1,1],
# [1,1,1],
# [1,1,1],
# [1,1,1],
# [1,1,1],
# [1,1,1],
# [0,1,1],
# [1,1,1]]
# [[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[0,1,1],[1,1,1]]
if __name__ == '__main__':
    s = Solution()
    s.largest1BorderedSquare([[1,1,1],[1,1,1],[1,1,1],[0,1,1],[1,1,1]])
