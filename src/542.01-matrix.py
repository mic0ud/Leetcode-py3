#
# @lc app=leetcode id=542 lang=python3
#
# [542] 01 Matrix
#
# https://leetcode.com/problems/01-matrix/description/
#
# algorithms
# Medium (37.48%)
# Likes:    967
# Dislikes: 93
# Total Accepted:    63.5K
# Total Submissions: 167.8K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for
# each cell.
# 
# The distance between two adjacent cells is 1.
# 
# 
# 
# Example 1: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[0,0,0]]
# 
# Output:
# [[0,0,0],
# [0,1,0],
# [0,0,0]]
# 
# 
# Example 2: 
# 
# 
# Input:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,1,1]]
# 
# Output:
# [[0,0,0],
# ⁠[0,1,0],
# ⁠[1,2,1]]
# 
# 
# 
# 
# Note:
# 
# 
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
# 
# 
#

# @lc code=start
from queue import Queue
class Solution:
    def updateMatrixSLOW(self, matrix: [[int]]) -> [[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def bfs(i, j) -> int:
            count = 0
            q = Queue()
            s = [[i-1, j],[i+1,j],[i,j-1],[i,j+1]]
            q.put(s)
            while not q.empty():
                tmp = q.get()
                ss = []
                count += 1
                for t in tmp:
                    if t[0] >= 0 and t[0] < m and t[1] >= 0 and t[1] < n:
                        if matrix[t[0]][t[1]] == 0:
                            return count
                        ss += [[t[0]-1, t[1]],[t[0]+1,t[1]],[t[0],t[1]-1],[t[0],t[1]+1]]
                if ss:
                    q.put(ss)

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and matrix[i][j] != 0:
                    matrix[i][j] = bfs(i, j)
                    visited[i][j] = True
        return matrix

    def updateMatrix(self, matrix: [[int]]) -> [[int]]:
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j, target: int, count: [int]):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j]:
                return            
            count[0] += 1
            if matrix[i][j] == target and target == 0:
                visited[i][j] = True
                dfs(i-1,j, target, count)
                dfs(i+1,j, target, count)
                dfs(i,j-1, target, count)
                dfs(i,j+1, target, count)
            else:
                matrix[i][j] = target + 1
                return
                
        count = [0]
        target = 0
        while count[0] < m*n:
            for i in range(m):
                for j in range(n):
                    if not visited[i][j] and matrix[i][j] == target:
                        dfs(i,j,target,count)
            target += 1
        return matrix
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    a = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    s.updateMatrix(a)

# [[0,0,0],[0,1,0],[1,1,1]]

# [1,0,1,1,0,0,1,0,0,1],
# [0,1,1,0,1,0,1,0,1,1],
# [0,0,1,0,1,0,0,1,0,0],
# [1,0,1,0,1,1,1,1,1,1],
# [0,1,0,1,1,0,0,0,0,1],
# [0,0,1,0,1,1,1,0,1,0],
# [0,1,0,1,0,1,0,0,1,1],
# [1,0,0,0,1,1,1,1,0,1],
# [1,1,1,1,1,1,1,0,1,0],
# [1,1,1,1,0,1,0,0,1,1]]

# wrong
# [1,0,1,1,0,0,1,0,0,1],
# [0,1,1,0,1,0,1,0,1,1],
# [0,0,1,0,1,0,0,1,0,0],
# [1,0,1,0,1,1,1,1,1,1],
# [0,1,0,1,1,0,0,0,0,1],
# [0,0,1,0,1,1,1,0,1,0],
# [0,1,0,1,0,1,0,0,1,1],
# [1,0,0,0,1,2,1,1,0,1],
# [2,1,1,1,1,2,1,0,1,0],
# [6,2,2,1,0,1,0,0,1,1]]

# correct
# [1,0,1,1,0,0,1,0,0,1],
# [0,1,1,0,1,0,1,0,1,1],
# [0,0,1,0,1,0,0,1,0,0],
# [1,0,1,0,1,1,1,1,1,1],
# [0,1,0,1,1,0,0,0,0,1],
# [0,0,1,0,1,1,1,0,1,0],
# [0,1,0,1,0,1,0,0,1,1],
# [1,0,0,0,1,2,1,1,0,1],
# [2,1,1,1,1,2,1,0,1,0],
# [3,2,2,1,0,1,0,0,1,1]]