#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.com/problems/course-schedule-ii/description/
#
# algorithms
# Medium (37.04%)
# Likes:    1436
# Dislikes: 99
# Total Accepted:    198.2K
# Total Submissions: 529.1K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, return
# the ordering of courses you should take to finish all courses.
# 
# There may be multiple correct orders, you just need to return one of them. If
# it is impossible to finish all courses, return an empty array.
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished   
# course 0. So the correct course order is [0,1] .
# 
# Example 2:
# 
# 
# Input: 4, [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,1,2,3] or [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both     
# ⁠            courses 1 and 2. Both courses 1 and 2 should be taken after you
# finished course 0. 
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3] .
# 
# Note:
# 
# 
# The input prerequisites is a graph represented by a list of edges, not
# adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        if numCourses <= 0:
            return []
        g = defaultdict(list)
        d = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            g[b].append(a)
            d[a] += 1
        res = [i for i in range(numCourses) if d[i] == 0]
        for r in res:
            for n in g[r]:
                d[n] -= 1
                if d[n] == 0:
                    res.append(n)
        return res if len(res) == numCourses else []

    def findOrderTopSort(self, numCourses: int, prerequisites: [[int]]) -> [int]:
        if numCourses <= 0:
            return []
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)
        v = [0 for _ in range(numCourses)] # -1: visiting, 1: visited, 0: defaut state

        def visit(n: int, res: [int]) -> bool:
            if v[n] == -1:
                return False
            if v[n] == 1:
                return True
            v[n] = -1
            for i in g[n]:
                if not visit(i, res):
                    return False
            v[n] = 1
            res.append(n)
            return True

        res = []
        for n in range(numCourses):
            if not visit(n, res):
                return []
        return res
# @lc code=end
# 2\n[[0,1]]
