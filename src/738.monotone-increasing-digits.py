#
# @lc app=leetcode id=738 lang=python3
#
# [738] Monotone Increasing Digits
#
# https://leetcode.com/problems/monotone-increasing-digits/description/
#
# algorithms
# Medium (42.67%)
# Likes:    339
# Dislikes: 53
# Total Accepted:    18.1K
# Total Submissions: 41.8K
# Testcase Example:  '10'
#
# 
# Given a non-negative integer N, find the largest number that is less than or
# equal to N with monotone increasing digits.
# 
# (Recall that an integer has monotone increasing digits if and only if each
# pair of adjacent digits x and y satisfy x .)
# 
# 
# Example 1:
# 
# Input: N = 10
# Output: 9
# 
# 
# 
# Example 2:
# 
# Input: N = 1234
# Output: 1234
# 
# 
# 
# Example 3:
# 
# Input: N = 332
# Output: 299
# 
# 
# 
# Note:
# N is an integer in the range [0, 10^9].
# 
#

# @lc code=start
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n_str = str(N)
        if len(n_str) == 1:
            return N
        res, i, j = '', len(n_str)-1, len(n_str)
        while i > 0:
            while i > 0 and n_str[i-1] <= n_str[i]:
                i -= 1
            if i > 0:
                n_str = str(int(n_str[:i])-1) + n_str[i:]
                res = '9' * (j-i) + res
                j = i
                i -= 1
            else:
                return int(n_str[:j] + res)
        if j > 0:
            res = n_str[:j] + res
        return int(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.monotoneIncreasingDigits(10)
    # s.monotoneIncreasingDigits(322)
    s.monotoneIncreasingDigits(332)
