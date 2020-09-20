#
# @lc app=leetcode id=886 lang=python3
#
# [886] Possible Bipartition
#
# https://leetcode.com/problems/possible-bipartition/description/
#
# algorithms
# Medium (41.65%)
# Likes:    385
# Dislikes: 16
# Total Accepted:    18.2K
# Total Submissions: 43.2K
# Testcase Example:  '4\n[[1,2],[1,3],[2,4]]'
#
# Given a set of N people (numbered 1, 2, ..., N), we would like to split
# everyone into two groups of any size.
# 
# Each person may dislike some other people, and they should not go into the
# same group. 
# 
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the
# people numbered a and b into the same group.
# 
# Return true if and only if it is possible to split everyone into two groups
# in this way.

# Example 1:
# 
# 
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]

# Example 2:
# 
# 
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false

# Example 3:
# 
# 
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
 
# Note:
# 
# 
# 1 <= N <= 2000
# 0 <= dislikes.length <= 10000
# 1 <= dislikes[i][j] <= N
# dislikes[i][0] < dislikes[i][1]
# There does not exist i != j for which dislikes[i] == dislikes[j].


# @lc code=start
from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: [[int]]) -> bool:
        visited = [-1 for _ in range(N+1)]
        g = defaultdict(list)
        for d in dislikes:
            g[d[0]].append(d[1])
            g[d[1]].append(d[0])
        def checkOddCircleExists(n, count) -> bool:
            if visited[n] >= 0:
                return (count - visited[n]) % 2 > 0
            visited[n] = count
            for d in g[n]:
                if checkOddCircleExists(d, count+1):
                    return True
            return False
        for i in range(1, N+1):
            if visited[i] == -1 and g[i]:
                if checkOddCircleExists(i, 0):
                    return False
        return True
# @lc code=end
# 10\n[[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]]
if __name__ == '__main__':
    s = Solution()
    # s.possibleBipartition(3, [[1,2],[1,3],[2,3]])
    s.possibleBipartition(10, [[4,7],[4,8],[5,6],[1,6],[3,7],[2,5],[5,8],[1,2],[4,9],[6,10],[8,10],[3,6],[2,10],[9,10],[3,9],[2,3],[1,9],[4,6],[5,7],[3,8],[1,8],[1,7],[2,4]])
