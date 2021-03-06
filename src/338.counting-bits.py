#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (66.03%)
# Likes:    1806
# Dislikes: 127
# Total Accepted:    206.3K
# Total Submissions: 311.4K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,1]
# 
# Example 2:
# 
# 
# Input: 5
# Output: [0,1,1,2,1,2]
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
# 
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> [int]:
        if num == 0:
            return [0]
        dp = [0 for _ in range(num+1)]
        dp[1] = 1
        if num == 1:
            return dp
        for i in range(2, num+1):
            j = 1
            while 2**j <= i:
                j += 1
            j -= 1
            dp[i] = dp[i-2**j] + 1
        return dp
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.countBits(5))
