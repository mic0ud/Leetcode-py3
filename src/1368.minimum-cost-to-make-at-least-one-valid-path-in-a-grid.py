#
# @lc app=leetcode id=1368 lang=python3
#
# [1368] Minimum Cost to Make at Least One Valid Path in a Grid
#
# https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/description/
#
# algorithms
# Hard (52.54%)
# Likes:    205
# Dislikes: 4
# Total Accepted:    6.2K
# Total Submissions: 11.7K
# Testcase Example:  '[[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]'
#
# Given a m x n grid. Each cell of the grid has a sign pointing to the next
# cell you should visit if you are currently in this cell. The sign of
# grid[i][j] can be:
# 
# 1 which means go to the cell to the right. (i.e go from grid[i][j] to
# grid[i][j + 1])
# 2 which means go to the cell to the left. (i.e go from grid[i][j] to
# grid[i][j - 1])
# 3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i +
# 1][j])
# 4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i -
# 1][j])
# 
# 
# Notice that there could be some invalid signs on the cells of the grid which
# points outside the grid.
# 
# You will initially start at the upper left cell (0,0). A valid path in the
# grid is a path which starts from the upper left cell (0,0) and ends at the
# bottom-right cell (m - 1, n - 1) following the signs on the grid. The valid
# path doesn't have to be the shortest.
# 
# You can modify the sign on a cell with cost = 1. You can modify the sign on a
# cell one time only.
# 
# Return the minimum cost to make the grid have at least one valid path.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
# Output: 3
# Explanation: You will start at point (0, 0).
# The path to (3, 3) is as follows. (0, 0) --> (0, 1) --> (0, 2) --> (0, 3)
# change the arrow to down with cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) -->
# (1, 0) change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2,
# 2) --> (2, 3) change the arrow to down with cost = 1 --> (3, 3)
# The total cost = 3.
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,3],[3,2,2],[1,1,4]]
# Output: 0
# Explanation: You can follow the path from (0, 0) to (2, 2).
# 
# 
# Example 3:
# 
# 
# Input: grid = [[1,2],[4,3]]
# Output: 1
# 
# 
# Example 4:
# 
# 
# Input: grid = [[2,2,2],[2,2,2]]
# Output: 3
# 
# 
# Example 5:
# 
# 
# Input: grid = [[4]]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 100
# 
# 
#

# @lc code=start
from queue import Queue
class Solution:
    def minCost(self, grid: [[int]]) -> int:
        m, n, changes = len(grid), len(grid[0]), [[],[0,1],[0,-1],[1,0],[-1,0]]
        dp = [[float('inf') for _ in range(n)] for _ in range(m)]
        q, next_, count = Queue(), [], 0
        def dfs(i,j,k):
            if not (0 <= i < m and 0 <= j < n and dp[i][j] == float('inf')):
                return
            dp[i][j] = k
            next_.append([i,j])
            dfs(i+changes[grid[i][j]][0], j+changes[grid[i][j]][1], k)
        dfs(0,0,0)
        q.put(next_)
        while not q.empty():
            count += 1
            curr, next_ = q.get(), []
            for x,y in curr:
                dfs(x+1,y,count)
                dfs(x-1,y,count)
                dfs(x,y+1,count)
                dfs(x,y-1,count)
            if next_:
                q.put(next_)
        return dp[-1][-1]

    def minCost_WRONG(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q1, q2, res, seen = Queue(), Queue(), 0, [[False for _ in range(n)] for _ in range(m)]
        seen[0][0] = True
        first = set()
        first.add((0,0))
        init_move = self.get_next(0,0,grid)
        while init_move and not seen[init_move[0]][init_move[1]]:
            first.add(init_move)
            seen[init_move[0]][init_move[1]] = True
            init_move = self.get_next(init_move[0],init_move[1],grid)                        
        q1.put(first)
        while not q1.empty() or not q2.empty():
            next_1, next_2 = set(), set()
            if not q1.empty():
                curr1 = q1.get()
                for i,j in curr1:
                    if i == m-1 and j == n-1:
                        return res
                    next_move = self.get_next(i,j,grid) 
                    while next_move and not seen[next_move[0]][next_move[1]]:
                        next_1.add(next_move)
                        seen[next_move[0]][next_move[1]] = True
                        next_move = self.get_next(next_move[0],next_move[1],grid)
                    if i+1 < m and not seen[i+1][j]:
                        seen[i+1][j] = True
                        next_2.add((i+1,j))
                    if i-1 >= 0 and not seen[i-1][j]:
                        seen[i-1][j] = True
                        next_2.add((i-1,j))
                    if j+1 < n and not seen[i][j+1]:
                        seen[i][j+1] = True
                        next_2.add((i,j+1))
                    if j-1 >= 0 and not seen[i][j-1]:
                        seen[i][j-1] = True
                        next_2.add((i,j-1))
            if not q2.empty():
                curr2 = q2.get()
                for i,j in curr2:
                    if i == m-1 and j == n-1:
                        return res
                    next_move = self.get_next(i,j,grid) 
                    while next_move and not seen[next_move[0]][next_move[1]]:
                        next_1.add(next_move)
                        seen[next_move[0]][next_move[1]] = True
                        next_move = self.get_next(next_move[0],next_move[1],grid)
                    if i+1 < m and not seen[i+1][j]:
                        seen[i+1][j] = True
                        next_2.add((i+1,j))
                    if i-1 >= 0 and not seen[i-1][j]:
                        seen[i-1][j] = True
                        next_2.add((i-1,j))
                    if j+1 < n and not seen[i][j+1]:
                        seen[i][j+1] = True
                        next_2.add((i,j+1))
                    if j-1 >= 0 and not seen[i][j-1]:
                        seen[i][j-1] = True
                        next_2.add((i,j-1))           
            if next_1:
                q1.put(next_1)
            if next_2:
                q2.put(next_2)
                res += 1
        return res

    def get_next(self, i, j, grid) -> (int):
        if grid[i][j] == 3:
            return (i+1,j) if i+1 < len(grid) else None
        if grid[i][j] == 4:
            return (i-1,j) if i-1 >= 0 else None
        if grid[i][j] == 1:
            return (i,j+1) if j+1 < len(grid[0]) else None
        if grid[i][j] == 2:
            return (i,j-1) if j-1 >= 0 else None
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minCost([[3,4,3],[2,2,2],[2,1,1],[4,3,2],[2,1,4],[2,4,1],[3,3,3],[1,4,2],[2,2,1],[2,1,1],[3,3,1],[4,1,4],[2,1,4],[3,2,2],[3,3,1],[4,4,1],[1,2,2],[1,1,1],[1,3,4],[1,2,1],[2,2,4],[2,1,3],[1,2,1],[4,3,2],[3,3,4],[2,2,1],[3,4,3],[4,2,3],[4,4,4]])
    s.minCost([[1,2],[4,3]])
    s.minCost([[1,1,3],[2,2,2],[4,4,1]])
    s.minCost([[1,1,3],[3,2,2],[1,1,4]])
    s.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])
