#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (43.07%)
# Likes:    514
# Dislikes: 125
# Total Accepted:    71.1K
# Total Submissions: 162.5K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the n^th super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
# 
# Example:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:

# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
# The n^th super ugly number is guaranteed to fit in a 32-bit signed integer.


# @lc code=start
import heapq
from functools import reduce
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: [int]) -> int:
        res = [1]
        def next_(primes) -> [int]:
            for r in res:
                yield r * primes

        g = heapq.merge(*map(next_, primes))        
        while len(res) < n:
            c = next(g)
            if c != res[-1]:
                res.append(c)

        return res[-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.nthSuperUglyNumber(12,[2,7,13,19])
