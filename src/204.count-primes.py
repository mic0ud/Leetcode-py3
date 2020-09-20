#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (30.15%)
# Likes:    1447
# Dislikes: 484
# Total Accepted:    292.3K
# Total Submissions: 964.6K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        notPrime = [False for _ in range(n)]
        count = 0
        for i in range(2, n):
            if not notPrime[i]:
                count += 1
                for j in range(2, n):
                    if i*j >= n:
                        break
                    notPrime[i*j] = True
        return count

    def countPrimesTLE(self, n: int) -> int:
        if n < 3:
            return 0
        maxPrime = 2
        count = 1
        for i in range(3, n+1):
            for j in range(maxPrime+1, i):
                if self.isPrime(j):
                    count += 1
                    maxPrime = max(maxPrime, j)
        return count
            
    def isPrime(self, n) -> bool:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
        
# @lc code=end

