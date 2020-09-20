#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#
# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
#
# algorithms
# Medium (20.32%)
# Likes:    670
# Dislikes: 1455
# Total Accepted:    108.3K
# Total Submissions: 524.1K
# Testcase Example:  '1\n2'
#
# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
# 
# If the fractional part is repeating, enclose the repeating part in
# parentheses.
# 
# Example 1:
# 
# 
# Input: numerator = 1, denominator = 2
# Output: "0.5"
# 
# 
# Example 2:
# 
# 
# Input: numerator = 2, denominator = 1
# Output: "2"
# 
# Example 3:
# 
# 
# Input: numerator = 2, denominator = 3
# Output: "0.(6)"
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator//denominator)
        sign = 1 if (numerator > 0 and denominator > 0) or (numerator < 0 and denominator < 0) else -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        res1 = str(numerator//denominator)
        remainder = numerator % denominator
        res2 = []
        seen = defaultdict(int)
        seen[0] = -1
        i = 0
        while remainder not in seen:
            seen[remainder] = i
            i += 1
            res2.append(str((10*remainder) // denominator))
            remainder =  (10*remainder) % denominator 
        idx = seen[remainder]
        if idx == -1:
            res = res1 + '.' + ''.join(res2)
        else:
            res = res1 + '.' + ''.join(res2[:idx]) + '(' + ''.join(res2[idx:]) + ')'
        return res if sign == 1 else '-' + res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.fractionToDecimal(-50,8)
