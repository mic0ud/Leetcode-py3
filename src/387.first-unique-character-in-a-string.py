#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (50.97%)
# Likes:    1338
# Dislikes: 92
# Total Accepted:    360.5K
# Total Submissions: 704.9K
# Testcase Example:  '"leetcode"'
#
# 
# Given a string, find the first non-repeating character in it and return it's
# index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# return 0.
# 
# s = "loveleetcode",
# return 2.
# 
# 
# 
# 
# Note: You may assume the string contain only lowercase letters.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        count = defaultdict(int)
        visit = {}
        for i in range(len(s)):
            count[s[i]] += 1
            if s[i] not in visit:
                visit[s[i]] = i
        minIndex = float('inf')
        exist = False
        for k,v in count.items():
            if v == 1:
                exist = True
                minIndex = min(minIndex, visit[k])
        return minIndex if exist else -1
# @lc code=end

