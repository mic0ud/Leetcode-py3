#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (63.77%)
# Likes:    562
# Dislikes: 160
# Total Accepted:    50.9K
# Total Submissions: 79.1K
# Testcase Example:  '"cba"\n"abcd"'
#
# S and T are strings composed of lowercase letters. In S, no letter occurs
# more than once.
# 
# S was sorted in some custom order previously. We want to permute the
# characters of T so that they match the order that S was sorted. More
# specifically, if x occurs before y in S, then x should occur before y in the
# returned string.
# 
# Return any permutation of T (as a string) that satisfies this property.
# 
# 
# Example :
# Input: 
# S = "cba"
# T = "abcd"
# Output: "cbad"
# Explanation: 
# "a", "b", "c" appear in S, so the order of "a", "b", "c" should be "c", "b",
# and "a". 
# Since "d" does not appear in S, it can be at any position in T. "dcba",
# "cdba", "cbda" are also valid outputs.
# 
# 
# 
# 
# Note:
# 
# 
# S has length at most 26, and no character is repeated in S.
# T has length at most 200.
# S and T consist of lowercase letters only.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def customSortString(self, S: str, T: str) -> str:
        t_count = Counter(T)
        res = ''
        for c in S:
            if c in t_count:
                res += c * t_count[c]
                t_count.pop(c)
        for k, v in t_count.items():
            res += k * v
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.customSortString("cba", "abcd")
