#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (52.32%)
# Likes:    1149
# Dislikes: 33
# Total Accepted:    52.3K
# Total Submissions: 99.6K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# Your are given an array of integers prices, for which the i-th element is the
# price of a given stock on day i; and a non-negative integer fee representing
# a transaction fee.
# You may complete as many transactions as you like, but you need to pay the
# transaction fee for each transaction.  You may not buy more than 1 share of a
# stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
# 
# Example 1:
# 
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling
# at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 
# 
# Note:
# 0 < prices.length .
# 0 < prices[i] < 50000.
# 0 .
# 
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: [int], fee: int) -> int:
        pl = len(prices)
        if pl < 2:
            return 0
        pl = len(prices)
        hold = [0 for _ in range(pl + 1)]
        hold[1] = float('-inf')
        buy = [0 for _ in range(pl + 1)]
        buy[1] = -(prices[0])
        sell = [0 for _ in range(pl + 1)]
        sell[1] = float('-inf')
        skip = [0 for _ in range(pl + 1)]
        for i in range(2, pl+1):
            hold[i] = max(hold[i-1], buy[i-1])
            buy[i] = max(sell[i-1]-prices[i-1], skip[i-1]-prices[i-1])
            sell[i] = max(buy[i-1]+prices[i-1]-fee, hold[i-1]+prices[i-1]-fee)
            skip[i] = max(skip[i-1], sell[i-1])
        return max(skip[-1], sell[-1])
# @lc code=end
# [1,3,2,8,4,9]
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([1,3,2,8,4,9],2))
