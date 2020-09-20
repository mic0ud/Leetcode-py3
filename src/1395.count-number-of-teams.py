#
# @lc app=leetcode id=1395 lang=python3
#
# [1395] Count Number of Teams
#
# https://leetcode.com/problems/count-number-of-teams/description/
#
# algorithms
# Medium (81.59%)
# Likes:    267
# Dislikes: 60
# Total Accepted:    19K
# Total Submissions: 23.4K
# Testcase Example:  '[2,5,3,4,1]\r'
#
# There are n soldiers standing in a line. Each soldier is assigned a unique
# rating value.
# 
# You have to form a team of 3 soldiers amongst them under the following
# rules:
# 
# 
# Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j],
# rating[k]).
# A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] >
# rating[j] > rating[k]) where (0 <= i < j < k < n).
# 
# 
# Return the number of teams you can form given the conditions. (soldiers can
# be part of multiple teams).
# 
# 
# Example 1:
# 
# 
# Input: rating = [2,5,3,4,1]
# Output: 3
# Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1),
# (5,3,1). 
# 
# 
# Example 2:
# 
# 
# Input: rating = [2,1,3]
# Output: 0
# Explanation: We can't form any team given the conditions.
# 
# 
# Example 3:
# 
# 
# Input: rating = [1,2,3,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# n == rating.length
# 1 <= n <= 200
# 1 <= rating[i] <= 10^5
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numTeams(self, rating: [int]) -> int:
        n = len(rating)
        if n < 3:
            return 0
        dp_inc, dp_dec = [0 for _ in range(n)], [0 for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1,n):
                if rating[j] < rating[i]:
                    dp_dec[i] += 1 
                elif rating[j] > rating[i]:
                    dp_inc[i] += 1
        res = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                if rating[j] < rating[i]:
                    res += dp_dec[j]
                elif rating[j] > rating[i]:
                    res += dp_inc[j]
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numTeams([3,6,7,5,1])
    s.numTeams([1,2,3,4])
    s.numTeams([2,5,3,4,1])
