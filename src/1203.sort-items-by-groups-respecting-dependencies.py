#
# @lc app=leetcode id=1203 lang=python3
#
# [1203] Sort Items by Groups Respecting Dependencies
#
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
#
# algorithms
# Hard (44.41%)
# Likes:    142
# Dislikes: 32
# Total Accepted:    3.7K
# Total Submissions: 8K
# Testcase Example:  '8\n2\n[-1,-1,1,0,0,1,0,-1]\n[[],[6],[5],[6],[3,6],[],[],[]]'
#
# There are n items each belonging to zero or one of m groups where group[i] is
# the group that the i-th item belongs to and it's equal to -1 if the i-th item
# belongs to no group. The items and the groups are zero indexed. A group can
# have no item belonging to it.
# 
# Return a sorted list of the items such that:

# The items that belong to the same group are next to each other in the sorted
# list.
# There are some relations between these items where beforeItems[i] is a list
# containing all the items that should come before the i-th item in the sorted
# array (to the left of the i-th item).

# Return any solution if there is more than one solution and return an empty
# list if there is no solution.
 
# Example 1:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3,6],[],[],[]]
# Output: [6,3,4,1,5,2,0,7]

# Example 2:

# Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems =
# [[],[6],[5],[6],[3],[],[4],[]]
# Output: []
# Explanation: This is the same as example 1 except that 4 needs to be before 6
# in the sorted list.
 
# Constraints:

# 1 <= m <= n <= 3*10^4
# group.length == beforeItems.length == n
# -1 <= group[i] <= m-1
# 0 <= beforeItems[i].length <= n-1
# 0 <= beforeItems[i][j] <= n-1
# i != beforeItems[i][j]
# beforeItems[i] does not contain duplicates elements.


# @lc code=start
from collections import defaultdict
from functools import cmp_to_key 
class Solution:
    def sortItems(self, n: int, m: int, group: [int], beforeItems: [[int]]) -> [int]:
        grp, before, grpMap = defaultdict(set), defaultdict(set), defaultdict(dict)
        for i,g in enumerate(group):
            grp[g].add(i)
            before[g] = set()
            if g not in grpMap:
                grpMap[g] = defaultdict(set)
            grpMap[g][i] = set()
        for i in range(len(beforeItems)):
            if beforeItems[i]:
                for j in beforeItems[i]:
                    if group[i] == group[j]:
                        grpMap[group[i]][j].add(i)
                    else:
                        before[group[j]].add(group[i])
        if self.hasCircle(before):
            return []
        sortedGrp = self.topologicalSort(before)
        res = []
        for sg in sortedGrp:
            if self.hasCircle(grpMap[sg]):
                return []
            res += self.topologicalSort(grpMap[sg])
        return res

    def topologicalSort(self, g: {}) -> []:
        stack, visited = [], defaultdict(bool)
        def sort_(curr, stack):
            if visited[curr]:
                return
            visited[curr] = True
            if curr in g:
                for next_ in g[curr]:
                    sort_(next_, stack)
            stack.append(curr)

        for v in g:
            if not visited[v]:
                sort_(v, stack)
        return stack[::-1]

    def hasCircle(self, g: {}) -> bool:
        visited = defaultdict(bool)
        def dfs(curr, path: []) -> bool:
            if curr in path:
                return True
            visited[curr] = True
            path.append(curr)
            for next_ in g[curr]:
                if dfs(next_, list(path)):
                    return True
            return False
        for i in list(g.keys()):
            if not visited[i]:
                if dfs(i, []):
                    return True
        return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.sortItems(5,4,[0,2,1,-1,-1],[[],[],[],[],[]])
    # s.sortItems(5,3,[0,0,2,1,0],[[3],[],[],[],[1,3,2]])
    # s.sortItems(5,5,[2,0,-1,3,0],[[2,1,3],[2,4],[],[],[]])
    # s.sortItems(4,4,[-1,0,0,-1],[[],[0],[1,3],[2]])
    s.sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3,6],[],[],[]])
    # s.sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[2,6],[3,6],[],[],[]])
    s.sortItems(8,2,[-1,-1,1,0,0,1,0,-1],[[],[6],[5],[6],[3],[],[4],[]])
