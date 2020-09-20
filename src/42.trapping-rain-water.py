#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (45.65%)
# Likes:    5037
# Dislikes: 89
# Total Accepted:    390.8K
# Total Submissions: 852.1K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
# 
# 
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
# 
# Example:
# 
# 
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def trap(self, height: [int]) -> int:
        if len(height) < 3:
            return 0
        stack, res = [], 0
        for i,h in enumerate(height):
            if stack and h > height[stack[-1]]:
                curr = height[stack.pop()]
                while stack and height[stack[-1]] <= h:
                    j = stack.pop()
                    res += (height[j]-curr)*(i-j-1)
                    curr = height[j]
                if stack:
                    res += (h-curr)*(i-stack[-1]-1)
            stack.append(i)
        return res

    def trap_(self, height: [int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        # left: descreasing stack with indices
        left, res = [0], 0
        for i in range(1, n):
            # found
            while left and height[i] > height[left[-1]]:
                prev = left.pop()
                if left:
                    res += (min(height[left[-1]], height[i]) - height[prev]) * (i-left[-1]-1)
                else:
                    left.append(i)
                    continue
            while left and height[left[-1]] <= height[i]:
                left.pop()
            left.append(i)
        return res
# @lc code=end
# [2,1,0,2]
if __name__ == '__main__':
    s = Solution()
    s.trap([4,2,3])
    s.trap([2,1,0,2])
    s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
