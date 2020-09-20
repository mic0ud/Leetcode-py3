#
# @lc app=leetcode id=1414 lang=python3
#
# [1414] Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
#
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/
#
# algorithms
# Medium (59.15%)
# Likes:    157
# Dislikes: 21
# Total Accepted:    9.6K
# Total Submissions: 16K
# Testcase Example:  '7'
#
# Given the number k, return the minimum number of Fibonacci numbers whose sum
# is equal to k, whether a Fibonacci number could be used multiple times.
# 
# The Fibonacci numbers are defined as:
# 
# 
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 , for n > 2.
# 
# It is guaranteed that for the given constraints we can always find such
# fibonacci numbers that sum k.
# 
# Example 1:
# 
# 
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# 
# Example 2:
# 
# 
# Input: k = 10
# Output: 2 
# Explanation: For k = 10 we can use 2 + 8 = 10.
# 
# 
# Example 3:
# 
# 
# Input: k = 19
# Output: 3 
# Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= 10^9
# 
#

# @lc code=start
from bisect import bisect_left
from collections import defaultdict
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fibs = self.fib(k)
        res = [k]
        def search(t, nums):
            idx = bisect_left(fibs,t)
            if fibs[idx] == t:
                res[0] = min(res[0],nums+1)
                return
            if idx == 0:
                return
            search(t-fibs[idx-1], nums+1)
        search(k,0)
        return res[0]
        
    def fib(self, max_val) -> [int]:
        res = [1,2]
        while res[-1] <= max_val:
            res.append(res[-1]+res[-2])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.fib(10**9)
    s.findMinFibonacciNumbers(10**9)
    s.findMinFibonacciNumbers(19)
