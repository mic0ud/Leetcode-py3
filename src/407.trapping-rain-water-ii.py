#
# @lc app=leetcode id=407 lang=python3
#
# [407] Trapping Rain Water II
#
# https://leetcode.com/problems/trapping-rain-water-ii/description/
#
# algorithms
# Hard (40.25%)
# Likes:    933
# Dislikes: 25
# Total Accepted:    33.6K
# Total Submissions: 83.2K
# Testcase Example:  '[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]'
#
# Given an m x n matrix of positive integers representing the height of each
# unit cell in a 2D elevation map, compute the volume of water it is able to
# trap after raining.
# 
# 
# 
# Note:
# 
# Both m and n are less than 110. The height of each unit cell is greater than
# 0 and is less than 20,000.
# 
# 
# 
# Example:
# 
# 
# Given the following 3x6 height map:
# [
# ⁠ [1,4,3,1,3,2],
# ⁠ [3,2,1,3,2,4],
# ⁠ [2,3,3,2,3,1]
# ]
# 
# Return 4.
# 
# 
# 
# 
# The above image represents the elevation map
# [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] before the rain.
# 
# 
# 
# 
# 
# After the rain, water is trapped between the blocks. The total volume of
# water trapped is 4.
# 
#

# @lc code=start
import heapq
class Solution:
    def trapRainWater(self, heightMap: [[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        visit = [[False for _ in range(n)] for _ in range(m)]
        heap = []
        for i in range(n):
            heapq.heappush(heap, (heightMap[0][i], 0, i))
            heapq.heappush(heap, (heightMap[m-1][i], m-1, i))
            visit[0][i] = True
            visit[m-1][i] = True
        for i in range(1, m-1):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][-1], i, n-1))
            visit[i][0] = True
            visit[i][-1] = True
        res = [0]
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            self.dfs(heightMap, heap, curr[0], curr[1],curr[2],visit, res)
        return res[0]
        
    def dfs(self, heightMap: [[int]], heap, currMax: int, i, j, visit: [bool], res: [int]):
        neighbours = self.getNeighbours(i,j, len(heightMap), len(heightMap[0]))
        for nb in neighbours:
            if not visit[nb[0]][nb[1]]:
                visit[nb[0]][nb[1]] = True
                if heightMap[nb[0]][nb[1]] < currMax:
                    res[0] += (currMax-heightMap[nb[0]][nb[1]])
                    self.dfs(heightMap, heap, currMax, nb[0], nb[1], visit, res)
                else:
                    heapq.heappush(heap, (heightMap[nb[0]][nb[1]], nb[0], nb[1]))

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

# [
#     [12,13,1,12],
#     [13,4,13,12],
#     [13,8,10,12],
#     [12,13,12,12],
#     [13,13,13,13]]

if __name__ == '__main__':
    s = Solution()
    s.trapRainWater([[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]])


