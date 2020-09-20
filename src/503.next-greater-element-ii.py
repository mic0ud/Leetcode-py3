#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (52.79%)
# Likes:    920
# Dislikes: 53
# Total Accepted:    66.7K
# Total Submissions: 125.7K
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: [int]) -> [int]:
        circularNums = nums + nums
        res = [-1 for r in range(len(circularNums))]
        stack = []
        
        for i in range(len(circularNums)):
            while stack and circularNums[i] > stack[-1][1]:
                item = stack.pop()
                res[item[0]] = circularNums[i]
            stack.append((i, circularNums[i]))
        return res[:len(nums)]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.nextGreaterElements([1,2,1])
