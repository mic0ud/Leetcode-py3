#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (44.82%)
# Likes:    250
# Dislikes: 47
# Total Accepted:    6.7K
# Total Submissions: 14.6K
# Testcase Example:  '"cdadabcc"'
#
# Return the lexicographically smallest subsequence of text that contains all
# the distinct characters of text exactly once.
# 
# 
# 
# Example 1:
# 
# 
# Input: "cdadabcc"
# Output: "adbc"
# 
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: "abcd"
# 
# 
# 
# Example 3:
# 
# 
# Input: "ecbacba"
# Output: "eacb"
# 
# 
# 
# Example 4:
# 
# 
# Input: "leetcode"
# Output: "letcod"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= text.length <= 1000
# text consists of lowercase English letters.
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def smallestSubsequence(self, text: str) -> str:
        n = len(text)
        if n <= 1:
            return text
        res = [] # make res monotonically increasing
        count = defaultdict(int)
        for c in text:
            count[c] += 1
        for c in text:
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
    s.smallestSubsequence("leetcode")
