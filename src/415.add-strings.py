#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (46.64%)
# Likes:    860
# Dislikes: 256
# Total Accepted:    173.1K
# Total Submissions: 369.7K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res, carry = [], 0
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1 = '0'*(len(num2)-len(num1)) + num1
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(len(num1)):
            tmp = str(int(num1[i]) + int(num2[i]) + carry)
            if len(tmp) == 1:
                res.append(tmp)
                carry = 0
            else:
                res.append(tmp[-1])
                carry = int(tmp[0])
        if carry > 0:
            res.append(str(carry))
        return ''.join(res[::-1])
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.addStrings('999','9')
