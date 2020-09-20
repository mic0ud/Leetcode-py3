#
# @lc app=leetcode id=486 lang=python3
#
# [486] Predict the Winner
#
# https://leetcode.com/problems/predict-the-winner/description/
#
# algorithms
# Medium (47.14%)
# Likes:    1256
# Dislikes: 79
# Total Accepted:    61.9K
# Total Submissions: 130.8K
# Testcase Example:  '[1,5,2]'
#
# Given an array of scores that are non-negative integers. Player 1 picks one
# of the numbers from either end of the array followed by the player 2 and then
# player 1 and so on. Each time a player picks a number, that number will not
# be available for the next player. This continues until all the scores have
# been chosen. The player with the maximum score wins. 
# 
# Given an array of scores, predict whether player 1 is the winner. You can
# assume each player plays to maximize his score. 
# 
# Example 1:
# 
# Input: [1, 5, 2]
# Output: False
# Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2
# (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5,
# then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 +
# 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you
# need to return False.
# 
# 
# 
# Example 2:
# 
# Input: [1, 5, 233, 7]
# Output: True
# Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5
# and 7. No matter which number player 2 choose, player 1 can choose
# 233.Finally, player 1 has more score (234) than player 2 (12), so you need to
# return True representing player1 can win.
# 
# 
# 
# Note:
# 
# 1 
# Any scores in the given array are non-negative integers and will not exceed
# 10,000,000.
# If the scores of both players are equal, then player 1 is still the winner.


# @lc code=start
class Solution:
    def PredictTheWinner(self, nums: [int]) -> bool:
        n = len(nums)
        dp1 = [[0 for _ in range(n)] for _ in range(n)]
        dp2 = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp1[i][i] = nums[i]
            if i < n-1:
                dp1[i][i+1] = max(nums[i], nums[i+1])
                dp2[i][i+1] = min(nums[i], nums[i+1])
        for k in range(2,n):
            for i in range(n-k):
                dp1[i][i+k] = max(nums[i]+dp2[i+1][i+k], dp2[i][i+k-1]+nums[i+k])
                dp2[i][i+k] = dp1[i+1][i+k] if nums[i]+dp2[i+1][i+k] >= dp2[i][i+k-1]+nums[i+k] else dp1[i][i+k-1]
        return dp1[0][n-1] >= dp2[0][n-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.PredictTheWinner([1, 5, 2])
    s.PredictTheWinner([1, 5, 233, 7])
