#
# @lc app=leetcode id=467 lang=python3
#
# [467] Unique Substrings in Wraparound String
#
# https://leetcode.com/problems/unique-substrings-in-wraparound-string/description/
#
# algorithms
# Medium (34.59%)
# Likes:    485
# Dislikes: 76
# Total Accepted:    22.5K
# Total Submissions: 64.4K
# Testcase Example:  '"a"'
#
# Consider the string s to be the infinite wraparound string of
# "abcdefghijklmnopqrstuvwxyz", so s will look like this:
# "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".
# 
# Now we have another string p. Your job is to find out how many unique
# non-empty substrings of p are present in s. In particular, your input is the
# string p and you need to output the number of different non-empty substrings
# of p in the string s.
# 
# Note: p consists of only lowercase English letters and the size of p might be
# over 10000.
# 
# Example 1:
# 
# Input: "a"
# Output: 1
# 
# Explanation: Only the substring "a" of string "a" is in the string s.
# 
# 
# 
# Example 2:
# 
# Input: "cac"
# Output: 2
# Explanation: There are two substrings "a", "c" of string "cac" in the string
# s.
# 
# 
# 
# Example 3:
# 
# Input: "zab"
# Output: 6
# Explanation: There are six substrings "z", "a", "b", "za", "ab", "zab" of
# string "zab" in the string s.

# @lc code=start
from collections import defaultdict
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = defaultdict(int)
        n, length = len(p), 1
        for i in range(n):
            if i > 0 and (ord(p[i])-ord(p[i-1]) == 1 or ord(p[i])-ord(p[i-1]) == -25):
                length += 1
            else:
                length = 1
            count[p[i]] = max(count[p[i]], length)  
        return sum(count.values())

    def findSubstringInWraproundString_WRONG(self, p: str) -> int:
        s = 'zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd'
        n = len(p)
        # dp1[i]: count at p[i] containing p[i]
        # dp2[i]: count at p[i] NOT containing p[i]
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n):
            dp1[i] = dp1[i-1]+1 if p[:i+1] in s else 1
            dp2[i] = dp1[i-1] + dp2[i-1]
        return dp1[n-1] + dp2[n-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findSubstringInWraproundString("zaba")
    s.findSubstringInWraproundString("cac")
