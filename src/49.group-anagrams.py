#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (50.72%)
# Likes:    2442
# Dislikes: 142
# Total Accepted:    469.4K
# Total Submissions: 904K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
# 
# Example:
# 
# 
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
# 
# Note:
# 
# 
# All inputs will be in lowercase.
# The order of your output does not matter.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        if not strs:
            return []
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
        return list(res.values())

    def groupAnagrams_SLOW(self, strs: [str]) -> [[str]]:
        if not strs:
            return []
        res = []
        counters = []
        for s in strs:
            c = Counter(s)
            if c in counters:
                res[counters.index(c)].append(s)
            else:
                counters.append(c)
                res.append([s])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
