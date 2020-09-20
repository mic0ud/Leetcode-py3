#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (28.17%)
# Likes:    817
# Dislikes: 145
# Total Accepted:    46.1K
# Total Submissions: 162K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.

# @lc code=start
from collections import defaultdict
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        total = (1+maxChoosableInteger)*maxChoosableInteger/2
        if total < desiredTotal:
            return False
        if desiredTotal <= maxChoosableInteger:
            return True
        memo = defaultdict(bool)
        choose = ['0' for _ in range(maxChoosableInteger)]
        def search(total) -> bool:
            if total <= 0:
                return False
            k = ''.join(choose)
            if k not in memo:
                for i in range(maxChoosableInteger):
                    if choose[i] == '0':
                        choose[i] = '1'
                        if not search(total-i-1):
                            memo[k] = True
                            choose[i] = '0'
                            return True                        
                        choose[i] = '0'  
                memo[k] = False              
            return memo[k]
        res = search(desiredTotal)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.canIWin(4,6)
