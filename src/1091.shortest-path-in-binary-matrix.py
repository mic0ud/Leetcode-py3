#
# @lc app=leetcode id=1091 lang=python3
#
# [1091] Shortest Path in Binary Matrix
#
# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/
#
# algorithms
# Medium (36.45%)
# Likes:    218
# Dislikes: 31
# Total Accepted:    17.6K
# Total Submissions: 47.3K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In an N by N square grid, each cell is either empty (0) or blocked (1).
# 
# A clear path from top-left to bottom-right has length k if and only if it is
# composed of cells C_1, C_2, ..., C_k such that:
# 
# 
# Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are
# different and share an edge or corner)
# C_1 is at location (0, 0) (ie. has value grid[0][0])
# C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
# If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] ==
# 0).
# 
# 
# Return the length of the shortest such clear path from top-left to
# bottom-right.  If such a path does not exist, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,0]]
# 
# 
# Output: 2
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,0,0],[1,1,0],[1,1,0]]
# [0,0,0],
# [1,1,0],
# [1,1,0]]
# 
# Output: 4

# Note:
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[r][c] is 0 or 1
# 
# 
#

# @lc code=start
from queue import Queue
class Solution:
    def shortestPathBinaryMatrix(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        q = Queue()
        q.put([[0,0]])
        visited = [[False for _ in range(n)] for _ in range(n)]
        res = 1
        while not q.empty():
            ps = q.get()
            next_ = []
            for p in ps:
                if p[0] == n-1 and p[1] == n-1:
                    return res
                visited[p[0]][p[1]] = True
                if grid[p[0]][p[1]] == 0:
                    a = p[0]-1
                    b = p[0]+1
                    c = p[1]-1
                    d = p[1]+1
                    if a >= 0 and d < n and not visited[a][d] and [a,d] not in next_:
                        next_.append([a,d])
                    if d < n and not visited[p[0]][d] and [p[0],d] not in next_:
                        next_.append([p[0],d])
                    if b < n:
                        if not visited[b][p[1]] and [b,p[1]] not in next_:
                            next_.append([b,p[1]])
                        if d < n and not visited[b][d] and [b,d] not in next_:
                            next_.append([b,d])   
                        if c >= 0 and not visited[b][c] and [b,c] not in next_:
                            next_.append([b,c])             
            if next_:
                res += 1
                q.put(next_)
        return -1                
# @lc code=end
# [0,0,1,0,0,0,0],
# [0,1,0,0,0,0,1],
# [0,0,1,0,1,0,0],
# [0,0,0,1,1,1,0],
# [1,0,0,1,1,0,0],
# [1,1,1,1,1,0,1],
# [0,0,1,0,0,0,0]]
if __name__ == '__main__':
    s = Solution()
    # s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])
    s.shortestPathBinaryMatrix([[0,0,1,0,0,0,0],[0,1,0,0,0,0,1],[0,0,1,0,1,0,0],[0,0,0,1,1,1,0],[1,0,0,1,1,0,0],[1,1,1,1,1,0,1],[0,0,1,0,0,0,0]])
