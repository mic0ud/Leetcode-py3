#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
# https://leetcode.com/problems/last-stone-weight-ii/description/
#
# algorithms
# Medium (41.78%)
# Likes:    327
# Dislikes: 15
# Total Accepted:    9.6K
# Total Submissions: 22.5K
# Testcase Example:  '[2,7,4,1,8,1]'
#
# We have a collection of rocks, each rock has a positive integer weight.
# 
# Each turn, we choose any two rocks and smash them together.  Suppose the
# stones have weights x and y with x <= y.  The result of this smash is:
# 
# 
# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of
# weight y has new weight y-x.
# 
# 
# At the end, there is at most 1 stone left.  Return the smallest possible
# weight of this stone (the weight is 0 if there are no stones left.)

# Example 1:
# 
# 
# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We can combine 2 and 4 to get 2 so the array converts to [2,7,1,8,1] then,
# we can combine 7 and 8 to get 1 so the array converts to [2,1,1,1] then,
# we can combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we can combine 1 and 1 to get 0 so the array converts to [1] then that's the
# optimal value.

# Note:
 
# 1 <= stones.length <= 30
# 1 <= stones[i] <= 100


# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:
        n = len(stones)
        if n == 1:
            return stones[0]
        # dp[i]: all possible sum at stone[i]
        dp = [set() for _ in range(n)]
        dp[0].add(stones[0])
        dp[0].add(-stones[0])
        for i in range(1, n):
            for s in dp[i-1]:
                tmp1 = s + stones[i]
                tmp2 = s - stones[i]
                dp[i].add(tmp1)
                dp[i].add(tmp2)
        return min([d for d in dp[-1] if d >= 0])
# @lc code=end
# [31,26,33,21,40], [21,26,31,33,40]
if __name__ == '__main__':
    s = Solution()
    s.lastStoneWeightII([31,26,33,21,40])
