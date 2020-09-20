#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#
# https://leetcode.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (32.53%)
# Likes:    3344
# Dislikes: 246
# Total Accepted:    320.4K
# Total Submissions: 969.8K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# Given a string S and a string T, find the minimum window in S which will
# contain all the characters in T in complexity O(n).
# 
# Example:
# 
# 
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# 
# 
# Note:
# 
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "".
# If there is such window, you are guaranteed that there will always be only
# one unique minimum window in S.
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc, idx, keys = Counter(t), [], set(t)
        res, i = '', 0
        for j in range(len(s)):
            if s[j] in tc:
                tc[s[j]] -= 1
                if tc[s[j]] <= 0:
                    keys.discard(s[j])
                idx.append(j)
            while len(keys) == 0:
                start = idx[i]
                if not res or len(res) > (j-start+1):
                    res = s[start:j+1]
                tc[s[start]] += 1
                if tc[s[start]] > 0:
                    keys.add(s[start])
                i += 1
        return res

    def minWindow_(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ''
        g = {}
        for c in t:
            if c not in g:
                g[c] = 1
            else:
                g[c] += 1
        count = len(g.keys())
        start, head, res = 0, 0, float('inf')
        for end in range(len(s)):     
            if s[end] in g:
                g[s[end]] -= 1
                if g[s[end]] == 0:
                    count -= 1
            while count == 0:
                while s[start] not in g.keys():
                    start += 1
                if end - start < res:
                    res = end - start
                    head = start
                g[s[start]] += 1
                if g[s[start]] > 0:
                    count += 1
                start += 1
                
        return '' if res == float('inf') else s[head:head+res+1]
# @lc code=end
# "ADOBECODEBANC"\n"ABC"
if __name__ == '__main__':
    s = Solution()
    s.minWindow("ADOBECODEBANC", "ABC")