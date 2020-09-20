#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (30.65%)
# Likes:    499
# Dislikes: 152
# Total Accepted:    34.9K
# Total Submissions: 112.5K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1: 
# Input: 12
# Output: 21

# Example 2:
# Input: 21
# Output: -1

# @lc code=start
from bisect import bisect_right
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [c for c in str(n)]
        i = len(s)-1
        while i > 0 and s[i] <= s[i-1]:
            i -= 1
        if i == 0:
            return -1
        idx = bisect_right(s[i:][::-1], s[i-1])
        s[i-1], s[-idx-1] = s[-idx-1], s[i-1]
        res = int(''.join(s[:i]+sorted(s[i:])))
        return res if res <= 2147483647 else -1 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.nextGreaterElement(1234321)
    s.nextGreaterElement(12443322)
