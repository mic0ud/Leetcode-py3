#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#
# https://leetcode.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (15.16%)
# Likes:    1583
# Dislikes: 9267
# Total Accepted:    566K
# Total Submissions: 3.7M
# Testcase Example:  '"42"'
#
# Implement atoi which converts a string to an integer.
# 
# The function first discards as many whitespace characters as necessary until
# the first non-whitespace character is found. Then, starting from this
# character, takes an optional initial plus or minus sign followed by as many
# numerical digits as possible, and interprets them as a numerical value.
# 
# The string can contain additional characters after those that form the
# integral number, which are ignored and have no effect on the behavior of this
# function.
# 
# If the first sequence of non-whitespace characters in str is not a valid
# integral number, or if no such sequence exists because either str is empty or
# it contains only whitespace characters, no conversion is performed.
# 
# If no valid conversion could be performed, a zero value is returned.
# 
# Note:
# 
# 
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. If the numerical
# value is out of the range of representable values, INT_MAX (2^31 − 1) or
# INT_MIN (−2^31) is returned.
# 
# 
# Example 1:
# 
# 
# Input: "42"
# Output: 42
# 
# 
# Example 2:
# 
# 
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus
# sign.
# Then take as many numerical digits as possible, which gets 42.
# 
# 
# Example 3:
# 
# 
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a
# numerical digit.
# 
# 
# Example 4:
# 
# 
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a
# numerical 
# digit or a +/- sign. Therefore no valid conversion could be performed.
# 
# Example 5:
# 
# 
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed
# integer.
# Thefore INT_MIN (−2^31) is returned.
# 
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s or (not s[0].isdigit() and s[0] != '+' and s[0] != '-'):
            return 0
        sign = -1 if s[0] == '-' else 1
        start = i = 0 if s[0].isdigit() else 1
        max_val, min_val = str(2**31-1), -2**31
        while i < len(s) and s[i].isdigit():
            if s[i] == '0' and start == i:
                start += 1
            i += 1
        if i-start > len(max_val):
            return int(max_val) if sign == 1 else min_val
        elif i-start < len(max_val):
            return 0 if i == start else int(s[start:i]) * sign
        else:
            j = 0
            while j < len(max_val):
                if s[start+j] < max_val[j]:
                    return int(s[start:i]) * sign
                elif s[start+j] > max_val[j]:
                    return int(max_val) if sign == 1 else min_val
                else:
                    j += 1
            return int(max_val) * sign      
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.myAtoi("1095502006p8")
    s.myAtoi("-2147483648")
    s.myAtoi("010")
    s.myAtoi("  0000000000012345678")
