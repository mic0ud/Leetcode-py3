#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#
# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
#
# algorithms
# Medium (39.06%)
# Likes:    985
# Dislikes: 123
# Total Accepted:    151.6K
# Total Submissions: 386.7K
# Testcase Example:  '5\n7'
#
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND
# of all numbers in this range, inclusive.
# 
# Example 1:
# 
# 
# Input: [5,7]
# Output: 4
# 
# 
# Example 2:
# 
# 
# Input: [0,1]
# Output: 0
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i, res = 32, 0
        while i > 0:
            if m - res >= 2**(i-1) and n - res < 2**i:
                res += 2**(i-1)
            i -= 1            
        return res

    def rangeBitwiseAnd_(self, m: int, n: int) -> int:
        while n > m:
            n &= n-1
        return m&n

    def rangeBitwiseAnd_SLOW(self, m: int, n: int) -> int:
        if m == 0 or m == n:
            return m & n
        i = 0
        while 2**i <= m:
            i += 1
        if n >= 2**i:
            return 0
        i -= 1
        res = 2**i
        while i > 0:
            if m - res >= 2**(i-1) and n - res < 2**i:
                res += 2**(i-1)
            i -= 1            
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.rangeBitwiseAnd(11,12)
    s.rangeBitwiseAnd(1,2)
    s.rangeBitwiseAnd(2,3)
    s.rangeBitwiseAnd(14,15)
    s.rangeBitwiseAnd(6,7)
    s.rangeBitwiseAnd(2040,2047)
    s.rangeBitwiseAnd(5,7)
