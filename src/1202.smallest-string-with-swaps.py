#
# @lc app=leetcode id=1202 lang=python3
#
# [1202] Smallest String With Swaps
#
# https://leetcode.com/problems/smallest-string-with-swaps/description/
#
# algorithms
# Medium (41.64%)
# Likes:    285
# Dislikes: 10
# Total Accepted:    8.1K
# Total Submissions: 18.9K
# Testcase Example:  '"dcab"\n[[0,3],[1,2]]'
#
# You are given a string s, and an array of pairs of indices in the string
# pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
# 
# You can swap the characters at any pair of indices in the given pairs any
# number of times.
# 
# Return the lexicographically smallest string that s can be changed to after
# using the swaps.
# 
# 
# Example 1:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# 
# 
# Example 2:
# 
# 
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination: 
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# 
# Example 3:
# 
# 
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination: 
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: [[int]]) -> str:
        if not s or not pairs or not pairs[0]:
            return s
        n = len(s)
        root = list(range(n))
        m = defaultdict(list)
        indexList = defaultdict(list)
        for p in pairs:
            self.union(root, p[0], p[1])
        for i in range(len(s)):
            r = self.find(root, i)
            heapq.heappush(m[r], s[i])
            heapq.heappush(indexList[r], i)
        res = [None for _ in range(len(s))]
        for k in m.keys():
            for j in range(len(m[k])):
                res[heapq.heappop(indexList[k])] = heapq.heappop(m[k])
        return ''.join(res)

    def find(self, root: [int], p: int) -> int:
        while root[p] != p:
            p = root[p]
        return p

    def union(self, root, p, q):
        rootP = self.find(root, p)
        rootQ = self.find(root, q)
        if rootQ < rootP:
            rootP, rootQ = rootQ, rootP
        root[rootQ] = rootP
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.smallestStringWithSwaps("dcab", [[0,3],[1,2]])
