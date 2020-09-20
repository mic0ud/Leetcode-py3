#
# @lc app=leetcode id=1014 lang=python3
#
# [1014] Best Sightseeing Pair
#
# https://leetcode.com/problems/best-sightseeing-pair/description/
#
# algorithms
# Medium (51.11%)
# Likes:    307
# Dislikes: 18
# Total Accepted:    12K
# Total Submissions: 23.5K
# Testcase Example:  '[8,1,5,2,6]'
#
# Given an array A of positive integers, A[i] represents the value of the i-th
# sightseeing spot, and two sightseeing spots i and j have distance j - i
# between them.
# 
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) :
# the sum of the values of the sightseeing spots, minus the distance between
# them.
# 
# Return the maximum score of a pair of sightseeing spots.
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 50000
# 1 <= A[i] <= 1000
# 
#

# @lc code=start
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        # current max val, decreases by 1 each step
        currentMaxNumber = 0
        res = 0
        for val in A:
            res = max(res, currentMaxNumber + val)
            currentMaxNumber = max(currentMaxNumber, val) - 1
        return res



    def maxScoreSightseeingPairBruteForce(self, A: List[int]) -> int:
        length = len(A)
        dp = [0 for n in range(length)]
        maxScore = dp[0]
        for i in range(1, length):
            val = A[i]
            tmpScore = 0
            for j in range(max(0, i-val), i):
                tmpScore = max(tmpScore, A[j]+A[i]-(i-j))
            dp[i] = tmpScore
            maxScore = max(maxScore, dp[i])
        return maxScore
# @lc code=end
# [3,7,2,3]
