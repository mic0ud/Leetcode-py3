#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (44.95%)
# Likes:    926
# Dislikes: 47
# Total Accepted:    49.8K
# Total Submissions: 108K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].


# @lc code=start
from collections import defaultdict
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        if n == 1:
            return S
        count = defaultdict(int)
        for c in S:
            count[c] += 1
        countReversedMap = defaultdict(list)
        for k,v in count.items():
            countReversedMap[v].append(k)
        keys = sorted(countReversedMap.keys(), reverse=True)
        if keys[0] > (n // 2 + 1 if n % 2 > 0 else n // 2):
            return ''
        loop, i, k, res, curr = 0, 0, 0, ['' for _ in range(n)], countReversedMap[keys[0]].pop()
        while i < n:
            res[i] = curr
            count[curr] -= 1
            if count[curr] == 0:
                if countReversedMap[keys[k]]:
                    curr = countReversedMap[keys[k]].pop()
                else:
                    k += 1
                    curr = countReversedMap[keys[k]].pop() if k < len(keys) else ''
            i += 2
            if i >= n:
                i = 1
                loop += 1
                if loop >= 2:
                    break
        return ''.join(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.reorganizeString("aaab")
