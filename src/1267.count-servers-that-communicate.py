#
# @lc app=leetcode id=1267 lang=python3
#
# [1267] Count Servers that Communicate
#
# https://leetcode.com/problems/count-servers-that-communicate/description/
#
# algorithms
# Medium (57.80%)
# Likes:    249
# Dislikes: 25
# Total Accepted:    16.4K
# Total Submissions: 28.3K
# Testcase Example:  '[[1,0],[0,1]]'
#
# You are given a map of a server center, represented as a m * n integer matrix
# grid, where 1 means that on that cell there is a server and 0 means that it
# is no server. Two servers are said to communicate if they are on the same row
# or on the same column.
# 
# Return the number of servers that communicate with any other server.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.
# 
# Example 2:
# 
# 
# 
# 
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other
# server.
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each
# other. The two servers in the third column can communicate with each other.
# The server at right bottom corner can't communicate with any other
# server.
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m <= 250
# 1 <= n <= 250
# grid[i][j] == 0 or 1
# 
# 
#

# @lc code=start
class Solution:
    def countServers(self, grid: [[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = set()
        for i in range(m):
            tmp = set()
            for j in range(n):
                if grid[i][j] == 1:
                    # tmp.add(str(i)+','+str(j))
                    tmp.add((i,j))
            if len(tmp) >= 2:
                res = res.union(tmp)
        for j in range(n):
            tmp = set()
            for i in range(m):
                if grid[i][j] == 1:
                    # tmp.add(str(i)+','+str(j))
                    tmp.add((i,j))
            if len(tmp) >= 2:
                res = res.union(tmp)
        return len(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]])
