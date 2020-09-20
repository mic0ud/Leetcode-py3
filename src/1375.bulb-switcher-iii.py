#
# @lc app=leetcode id=1375 lang=python3
#
# [1375] Bulb Switcher III
#
# https://leetcode.com/problems/bulb-switcher-iii/description/
#
# algorithms
# Medium (60.13%)
# Likes:    180
# Dislikes: 25
# Total Accepted:    13.2K
# Total Submissions: 21.5K
# Testcase Example:  '[2,1,3,5,4]'
#
# There is a room with n bulbs, numbered from 1 to n, arranged in a row from
# left to right. Initially, all the bulbs are turned off.
# 
# At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb
# change color to blue only if it is on and all the previous bulbs (to the
# left) are turned on too.
# 
# Return the number of moments in which all turned on bulbs are blue.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: light = [2,1,3,5,4]
# Output: 3
# Explanation: All bulbs turned on, are blue at the moment 1, 2 and 4.
# 
# 
# Example 2:
# 
# 
# Input: light = [3,2,4,1,5]
# Output: 2
# Explanation: All bulbs turned on, are blue at the moment 3, and 4
# (index-0).
# 
# 
# Example 3:
# 
# 
# Input: light = [4,1,2,3]
# Output: 1
# Explanation: All bulbs turned on, are blue at the moment 3 (index-0).
# Bulb 4th changes to blue at the moment 3.
# 
# 
# Example 4:
# 
# 
# Input: light = [2,1,4,3,6,5]
# Output: 3
# 
# 
# Example 5:
# 
# 
# Input: light = [1,2,3,4,5,6]
# Output: 6
# 
# 
# 
# Constraints:
# 
# 
# n == light.length
# 1 <= n <= 5 * 10^4
# light is a permutation of  [1, 2, ..., n]
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def numTimesAllBlue(self, light: [int]) -> int:
        right = res = 0
        for i,n in enumerate(light):
            right = max(right, n)
            if right == i+1:
                res += 1
        return res

    def numTimesAllBlue_SLOW(self, light: [int]) -> int:
        bt = [0 for _ in range(len(light)+1)]
        res, on_right = 0, []
        for n in light:
            self.update(bt, n)
            if self.get_pre_sum(bt,n) == n:
                m = n+1
                while on_right and on_right[0] == m:
                    heapq.heappop(on_right)
                    m += 1
                if not on_right:
                    res += 1
            else:
                heapq.heappush(on_right, n)       
        return res
        
    def update(self, bt, i):
        while i < len(bt):
            bt[i] += 1
            i += (i & -i)

    def get_pre_sum(self, bt, i):
        res = 0
        while i > 0:
            res += bt[i]
            i -= (i & -i)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numTimesAllBlue([1,8,3,4,9,6,7,2,5,10])
    s.numTimesAllBlue([2,1,4,3,6,5])
    s.numTimesAllBlue([4,1,2,3])
    s.numTimesAllBlue([3,2,4,1,5])
