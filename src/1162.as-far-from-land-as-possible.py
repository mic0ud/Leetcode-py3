#
# @lc app=leetcode id=1162 lang=python3
#
# [1162] As Far from Land as Possible
#
# https://leetcode.com/problems/as-far-from-land-as-possible/description/
#
# algorithms
# Medium (40.09%)
# Likes:    197
# Dislikes: 13
# Total Accepted:    10.3K
# Total Submissions: 24.8K
# Testcase Example:  '[[1,0,1],[0,0,0],[1,0,1]]'
#
# Given an N x N grid containing only values 0 and 1, where 0 represents water
# and 1 represents land, find a water cell such that its distance to the
# nearest land cell is maximized and return the distance.
# 
# The distance used in this problem is the Manhattan distance: the distance
# between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
# 
# If no land or water exists in the grid, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [
# [1,0,1],
# [0,0,0],
# [1,0,1]]
# Output: 2
# Explanation: 
# The cell (1, 1) is as far as possible from all the land with distance 2.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: [
# [1,0,0],
# [0,0,0],
# [0,0,0]]
# Output: 4
# Explanation: 
# The cell (2, 2) is as far as possible from all the land with distance 4.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length == grid[0].length <= 100
# grid[i][j] is 0 or 1
# 
# [0,0,2,0,0],
# [0,2,1,2,0],
# [2,1,0,1,2]
# [0,2,1,2,0]
# [0,0,2,0,0]
# @lc code=start
from queue import Queue
class Solution:
    def maxDistance(self, grid: [[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        q = Queue()
        start = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start.append([i,j]) # put all 1s in the queue
        q.put(start)
        res = -1
        count = 0            
        while not q.empty():
            ps = q.get()
            next_ = []               
            for p in ps:                
                if p[0] - 1 >= 0 and grid[p[0]-1][p[1]] == 0:
                    grid[p[0]-1][p[1]] = 2 # tag as visited
                    next_.append([p[0]-1,p[1]])
                if p[0] + 1 < m and grid[p[0]+1][p[1]] == 0:
                    grid[p[0]+1][p[1]] = 2 # tag as visited
                    next_.append([p[0]+1,p[1]])
                if p[1] - 1 >= 0 and grid[p[0]][p[1]-1] == 0:
                    grid[p[0]][p[1]-1] = 2 # tag as visited
                    next_.append([p[0],p[1]-1])
                if p[1] + 1 < n and grid[p[0]][p[1]+1] == 0:
                    grid[p[0]][p[1]+1] = 2 # tag as visited
                    next_.append([p[0],p[1]+1])
            if next_:
                count += 1
                q.put(next_)
            res = max(res, count)
        return res if res > 0 else -1
# @lc code=end
# [1,0,1]
# [0,0,0]
# [1,0,1]
# [1,0,0,0,0,1,0,0,0,1]
# [1,1,0,1,1,1,0,1,1,0],
# [0,1,1,0,1,0,0,1,0,0],
# [1,0,1,0,1,0,0,0,0,0],
# [0,1,0,0,0,1,1,0,1,1],
# [0,0,1,0,0,1,0,1,0,1],
# [0,0,0,1,1,1,1,0,0,1],
# [0,1,0,0,1,0,0,1,0,0],
# [0,0,0,0,0,1,1,1,0,0],
# [1,1,0,1,1,1,1,1,0,0]]
if __name__ == '__main__':
    s = Solution()
    s.maxDistance([[1,0,0,0,0,1,0,0,0,1],[1,1,0,1,1,1,0,1,1,0],[0,1,1,0,1,0,0,1,0,0],[1,0,1,0,1,0,0,0,0,0],[0,1,0,0,0,1,1,0,1,1],[0,0,1,0,0,1,0,1,0,1],[0,0,0,1,1,1,1,0,0,1],[0,1,0,0,1,0,0,1,0,0],[0,0,0,0,0,1,1,1,0,0],[1,1,0,1,1,1,1,1,0,0]])