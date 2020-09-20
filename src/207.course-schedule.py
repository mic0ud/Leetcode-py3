#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (39.93%)
# Likes:    2602
# Dislikes: 134
# Total Accepted:    300.4K
# Total Submissions: 745.7K
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of n courses you have to take, labeled from 0 to n-1.
# 
# Some courses may have prerequisites, for example to take course 0 you have to
# first take course 1, which is expressed as a pair: [0,1]
# 
# Given the total number of courses and a list of prerequisite pairs, is it
# possible for you to finish all courses?
# 
# Example 1:
# 
# 
# Input: 2, [[1,0]] 
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# Example 2:
# 
# 
# Input: 2, [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should
# also have finished course 1. So it is impossible.
# 
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
    def canFinish2(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n

    def canFinish(self, numCourses: int, prerequisites: [[int]]) -> bool:
        if numCourses <= 0 or not prerequisites:
            return True
        g = defaultdict(list)
        d = defaultdict(int)
        for a, b in prerequisites:
            g[b].append(a)
            d[a] += 1 
        taken = []
        for i in range(numCourses):
            if d[i] == 0:
                taken.append(i)
        for k in taken:
            for j in g[k]:
                d[j] -= 1
                if d[j] == 0:
                    taken.append(j)
        return len(taken) == numCourses

    def dfs(self, numCourses: int, prerequisites: [[int]]) -> bool:
        if numCourses <= 0 or not prerequisites:
            return True
        g = defaultdict(list)
        v = defaultdict(int) # 0: not visited yet, -1: being visited, 1: visited
        for a, b in prerequisites:
            g[a] += b,
            v[a] = 0

        def visit(course: int) -> bool:
            # circular
            if v[course] == -1:
                return False
            if v[course] == 1:
                return True
            v[course] = -1
            for c in g[course]:
                if not visit(c):
                    return False
            v[course] = 1
            return True
        for i in range(numCourses):
            if not visit(i):
                return False
        return True
# @lc code=end
# 2, [[1,0],[0,1]]
# 2\n[[0,1],[1,0]]
if __name__ == '__main__':
    s = Solution()
    s.canFinish(2, [[0,1],[1,0]])