#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (32.74%)
# Likes:    2721
# Dislikes: 65
# Total Accepted:    217.8K
# Total Submissions: 656.1K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
# 
# 
# 
# 
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
# 
# 
# 
# 
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
# 
# 
# 
# Example:
# 
# 
# Input: [2,1,5,6,2,3]
# Output: 10
# 
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: [int]) -> int:
        res, stack, n = 0, [], len(heights)
        for i,h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                curr = heights[stack.pop()]
                area = curr * (i if not stack else (i-stack[-1]-1))
                res = max(res, area)
            stack.append(i)
        while stack:
            curr = heights[stack.pop()]
            area = curr * (n if not stack else (n-stack[-1]-1))
            res = max(res, area)
        return res

    def largestRectangleArea_(self, heights: [int]) -> int:
        if not heights:
            return 0
        stack = []
        res = 0
        for i in range(len(heights)):
            if not stack or heights[i] > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i] <= heights[stack[-1]]:
                    h = heights[stack.pop()]
                    area = h * i if not stack else h * (i-stack[-1]-1)
                    res = max(res, area)
                stack.append(i)
        while stack:
            h = heights[stack.pop()]
            area = h * len(heights) if not stack else h * (len(heights)-stack[-1]-1)
            res = max(res, area)
        return res
# @lc code=end
# [2,1,5,6,2,3]
if __name__ == '__main__':
    s = Solution()
    s.largestRectangleArea([2,1,5,6,2,3])
