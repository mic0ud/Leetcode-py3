#
# @lc app=leetcode id=1208 lang=python3
#
# [1208] Get Equal Substrings Within Budget
#
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
#
# algorithms
# Medium (36.81%)
# Likes:    183
# Dislikes: 14
# Total Accepted:    11.3K
# Total Submissions: 28.9K
# Testcase Example:  '"abcd"\n"bcdf"\n3'
#
# You are given two strings s and t of the same length. You want to change s to
# t. Changing the i-th character of s to i-th character of t costs |s[i] -
# t[i]| that is, the absolute difference between the ASCII values of the
# characters.
# 
# You are also given an integer maxCost.
# 
# Return the maximum length of a substring of s that can be changed to be the
# same as the corresponding substring of t with a cost less than or equal to
# maxCost.
# 
# If there is no substring from s that can be changed to its corresponding
# substring from t, return 0.

# Example 1:

# Input: s = "abcd", t = "bcdf", maxCost = 3
# Output: 3
# Explanation: "abc" of s can change to "bcd". That costs 3, so the maximum
# length is 3.
# 
# Example 2:

# Input: s = "abcd", t = "cdef", maxCost = 3
# Output: 1
# Explanation: Each character in s costs 2 to change to charactor in t, so the
# maximum length is 1.

# Example 3:

# Input: s = "abcd", t = "acde", maxCost = 0
# Output: 1
# Explanation: You can't make any change, so the maximum length is 1.

# Constraints:

# 1 <= s.length, t.length <= 10^5
# 0 <= maxCost <= 10^6
# s and t only contain lower case English letters.


# @lc code=start
from bisect import bisect_left, bisect_right
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start, res = 0, 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i])-ord(t[i]))
            if maxCost < 0:
                maxCost += abs(ord(s[start])-ord(t[start]))
                start += 1
                res = max(res, i-start+1)
        return max(res, i-start+1)

    def equalSubstring_SLOW(self, s: str, t: str, maxCost: int) -> int:
        costsPresum, preSum, res = [0], 0, 0
        for i in range(len(s)):
            preSum += abs(ord(s[i])-ord(t[i]))
            costsPresum.append(preSum)
        for i in range(len(costsPresum)-1,0,-1):
            l = bisect_left(costsPresum, costsPresum[i]-maxCost)
            # r = bisect_right(costsPresum, costsPresum[i]-maxCost)
            res = max(res, i-l)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.equalSubstring("krpgjbjjznpzdfy", "nxargkbydxmsgby", 14)
    s.equalSubstring("krrgw", "zjxss", 19)
    s.equalSubstring("abcd", "acde", 0)
    s.equalSubstring("abcd", "cdef", 3)
    s.equalSubstring("abcd", "bcdf", 3)
