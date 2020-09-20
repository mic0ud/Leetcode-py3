#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (32.52%)
# Likes:    2611
# Dislikes: 91
# Total Accepted:    283K
# Total Submissions: 863.2K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
# 
# Example 1:
# 
# 
# Input: coins = [1, 2, 5], amount = 11
# Output: 3 
# Explanation: 11 = 5 + 5 + 1
# 
# Example 2:
# 
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.
# 
#

# @lc code=start
class Solution:
    def coinChange1(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or amount < 0:
            return -1
        sortedCoins = sorted(coins)
        dp = [-1 for n in range(amount+1)]
        for i in range(1, amount+1):
            if i in sortedCoins:
                dp[i] = 1
                continue
            minVal = float('inf')
            for c in sortedCoins:
                if c > i:
                    break
                if dp[i-c] != -1:
                    minVal = min(minVal, dp[i-c]+1)
            dp[i] = minVal if minVal != float('inf') else -1
        return dp[amount]

    def coinChange2(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or amount < min(coins):
            return -1
        dp = [-1] * (amount+1)
        for i in range(min(coins), amount+1):
            if i in coins:
                dp[i] = 1
            else:
                minCoins = float('inf')
                for c in coins:
                    if i-c > 0 and dp[i-c] != -1:
                        minCoins = min(minCoins, dp[i-c]+1)
                if minCoins != float('inf'):
                    dp[i] = minCoins
        return dp[amount]

    def coinChange(self, coins: [int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins or amount < min(coins):
            return -1
        res = [float('inf')]
        self.dfs(sorted(coins, reverse=True), 0, amount, res, 0)
        return res[0] if res[0] != float('inf') else -1

    def dfs(self, coins:[int], start: int, amount: int, minCount: [int], currCount: int) -> int:
        c = coins[start]
        k = amount // c
        r = amount % c
        if start == len(coins) - 1:
            if r == 0:
                minCount[0] = min(currCount+k, minCount[0])       
        else:
            while k >= 0 and currCount + k < minCount[0]:
                self.dfs(coins, start+1, amount-k*c, minCount, currCount + k)
                k -= 1

# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([2,5,8], 31))
