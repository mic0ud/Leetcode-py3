#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#
# https://leetcode.com/problems/shortest-bridge/description/
#
# algorithms
# Medium (45.37%)
# Likes:    469
# Dislikes: 39
# Total Accepted:    17.9K
# Total Submissions: 39K
# Testcase Example:  '[[0,1],[1,0]]'
#
# In a given 2D binary array A, there are two islands.  (An island is a
# 4-directionally connected group of 1s not connected to any other 1s.)
# 
# Now, we may change 0s to 1s so as to connect the two islands together to form
# 1 island.
# 
# Return the smallest number of 0s that must be flipped.  (It is guaranteed
# that the answer is at least 1.)

# Example 1:

# Input: [
# [0,1],
# [1,0]]
# Output: 1

# Example 2:

# Input: [
# [0,1,0],
# [0,0,0],
# [0,0,1]]
# Output: 2

# Example 3:

# Input: [
# [1,1,1,1,1],
# [1,0,0,0,1],
# [1,0,1,0,1],
# [1,0,0,0,1],
# [1,1,1,1,1]]
# Output: 1

# Note:
# 
# 
# 1 <= A.length = A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1


# @lc code=start
from queue import Queue
class Solution:
    def shortestBridge(self, A: [[int]]) -> int:
        m = len(A)
        n = len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        q = Queue()
        first = set()
        def dfs(i,j):
            if visited[i][j]:
                return
            visited[i][j] = True
            if i-1 >= 0:
                if A[i-1][j] == 0:
                    first.add((i-1,j))
                else:
                    dfs(i-1,j)
            if i+1 < m:
                if A[i+1][j] == 0:
                    first.add((i+1,j))
                else:
                    dfs(i+1,j)
            if j-1 >= 0:
                if A[i][j-1] == 0:
                    first.add((i,j-1))
                else:
                    dfs(i,j-1)
            if j+1 < n:
                if A[i][j+1] == 0:
                    first.add((i,j+1))
                else:
                    dfs(i,j+1)
        found = False
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1:
                    found = True
                    dfs(i,j)
                    break
            if found:
                break
        if first:
            q.put(first)
        steps = 0
        while not q.empty():
            items = q.get()
            next_ = set()
            for i in items:
                if A[i[0]][i[1]] == 1 and not visited[i[0]][i[1]]:
                    return steps
                if A[i[0]][i[1]] == 0:
                    visited[i[0]][i[1]] = True
                    if i[0]-1 >= 0 and not visited[i[0]-1][i[1]]:
                        next_.add((i[0]-1, i[1]))
                    if i[0]+1 < m and not visited[i[0]+1][i[1]]:
                        next_.add((i[0]+1, i[1]))
                    if i[1]-1 >= 0 and not visited[i[0]][i[1]-1]:
                        next_.add((i[0], i[1]-1))
                    if i[1]+1 < m and not visited[i[0]][i[1]+1]:
                        next_.add((i[0], i[1]+1))
            if next_:
                q.put(next_)
                steps += 1
        return steps
# @lc code=end
# [[0,1,0],[0,0,0],[0,0,1]]
# [[0,1],[1,0]]
# [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
if __name__ == '__main__':
    s = Solution()
    s.shortestBridge([[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]])
