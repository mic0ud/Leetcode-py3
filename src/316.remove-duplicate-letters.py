#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.com/problems/remove-duplicate-letters/description/
#
# algorithms
# Hard (33.75%)
# Likes:    960
# Dislikes: 90
# Total Accepted:    66.1K
# Total Submissions: 195.5K
# Testcase Example:  '"bcabc"'
#
# Given a string which contains only lowercase letters, remove duplicate
# letters so that every letter appears once and only once. You must make sure
# your result is the smallest in lexicographical order among all possible
# results.
# 
# Example 1:
# 
# 
# Input: "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: "cbacdcbc"
# Output: "acdb"
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        count = defaultdict(int)
        res = [] # monotonically increasing
        for c in s:
            count[c] += 1
        for c in s:
            if c in res:
                count[c] -= 1
            else:
                while res and res[-1] > c and count[res[-1]] > 0:
                    res.pop()
                res.append(c)
                count[c] -= 1
        return ''.join(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.removeDuplicateLetters("cbacdcbc")
