#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (45.14%)
# Likes:    1739
# Dislikes: 66
# Total Accepted:    112.9K
# Total Submissions: 249.4K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
# 
# 
# Example:
# 
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int]) -> int:
        if len(prices) <= 1:
            return 0
        cooldown = [0 for _ in range(len(prices) + 1)]
        buy = [0 for _ in range(len(prices) + 1)]
        sell = [0 for _ in range(len(prices) + 1)]
        buy[0] = float('-inf')
        for i in range(1, len(prices)+1):
            cooldown[i] = max(cooldown[i-1], sell[i-1])
            buy[i] = max(cooldown[i-1]-prices[i-1], buy[i-1])
            sell[i] = buy[i-1] + prices[i-1]
        return max(cooldown[-1], sell[-1])
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxProfit([1,2,3,0,2])