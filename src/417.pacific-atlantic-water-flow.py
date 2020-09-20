#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (38.73%)
# Likes:    879
# Dislikes: 162
# Total Accepted:    57.8K
# Total Submissions: 148.2K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
# 
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
# 
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
# 
# Note:
# 
# 
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
# 
# 
# 
# 
# Example:
# 
# 
# Given the following 5x5 matrix:
# 
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# 
# Return:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
# 
# 
# 
# 
#
# ⁠ Pacific ~   ~   ~   ~   ~ 
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
# @lc code=start
class Solution:
    def pacificAtlantic(self, matrix: [[int]]) -> [[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        if m == 1:
            return [[0, i] for i in range(n)]
        if n == 1:
            return [[i, 0] for i in range(m)]

        def dfs(v: [[bool]], i: int, j: int, maxHeight: int):
            if v[i][j] or matrix[i][j] < maxHeight:
                return
            v[i][j] = True
            nbs = self.getNeighbours(i, j, m, n)
            for nb in nbs:
                if matrix[nb[0]][nb[1]] >= maxHeight:                    
                    dfs(v, nb[0], nb[1], matrix[nb[0]][nb[1]])
            
        v1 = [[False for _ in range(n)] for _ in range(m)]
        v2 = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dfs(v1, i, 0, matrix[i][0])
            dfs(v2, i, n-1, matrix[i][n-1])        
        for j in range(n):
            dfs(v1, 0, j, matrix[0][j])
            dfs(v2, m-1, j, matrix[m-1][j])          
        res = []
        for i in range(m):
            for j in range(n):
                if v1[i][j] and v2[i][j]:
                    res.append([i, j])
        return res

    def getNeighbours(self, i, j, m, n) -> [[int]]:
        res = []
        if 0 < i < m-1:
            res.append([i-1, j])
            res.append([i+1, j])
        elif i == 0:
            res.append([i+1, j])
        elif i == m-1:
            res.append([i-1, j])

        if 0 < j < n-1:
            res.append([i, j-1])
            res.append([i, j+1])     
        elif j == 0:
             res.append([i, j+1]) 
        elif j == n-1:
            res.append([i, j-1])   

        return res 
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])
