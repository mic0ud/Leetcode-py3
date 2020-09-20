#
# @lc app=leetcode id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (39.72%)
# Likes:    1122
# Dislikes: 98
# Total Accepted:    66.2K
# Total Submissions: 164.3K
# Testcase Example:  '"aaabb"\n3'
#
# 
# Find the length of the longest substring T of a given string (consists of
# lowercase letters only) such that every character in T appears no less than k
# times.
# 
# 
# Example 1:
# 
# Input:
# s = "aaabb", k = 3
# 
# Output:
# 3
# 
# The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# 
# Example 2:
# 
# Input:
# s = "ababbc", k = 2
# 
# Output:
# 5
# 
# The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is
# repeated 3 times.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0
        
        def search(s, k) -> int:
            indices = defaultdict(list)
            for i, c in enumerate(s):
                indices[c].append(i)
            b = []
            for idx in indices.values():
                if len(idx) < k:
                    b += idx
            if not b:
                return len(s)
            if len(b) == len(s):
                return 0
            res = 0
            for ss in [s[i+1:j] for i,j in zip([-1]+b, b+[None])]:
                res = max(res, search(ss,k))
            return res

        res = search(s, k)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestSubstring('ababbc',2)
    # s.longestSubstring('bbaaacbd',3)
