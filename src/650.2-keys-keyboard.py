#
# @lc app=leetcode id=650 lang=python3
#
# [650] 2 Keys Keyboard
#
# https://leetcode.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (47.48%)
# Likes:    801
# Dislikes: 59
# Total Accepted:    41.7K
# Total Submissions: 87.5K
# Testcase Example:  '3'
#
# Initially on a notepad only one character 'A' is present. You can perform two
# operations on this notepad for each step:
# 
# 
# Copy All: You can copy all the characters present on the notepad (partial
# copy is not allowed).
# Paste: You can paste the characters which are copied last time.
# 
# 
# 
# 
# Given a number n. You have to get exactly n 'A' on the notepad by performing
# the minimum number of steps permitted. Output the minimum number of steps to
# get n 'A'.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
# 
# 
# 
# 
# Note:
# 
# 
# The n will be in the range [1, 1000].
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1] = 0
        for i in range(2, n+1):
            minOp = float('inf')
            for j in range(i-1,0,-1):
                if i % j == 0:
                    minOp = min(minOp, dp[j] + i//j)
                    break
            dp[i] = min(minOp, i)
        return dp[n]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minSteps(121)

