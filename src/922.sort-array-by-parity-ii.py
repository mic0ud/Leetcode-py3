#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (67.39%)
# Likes:    428
# Dislikes: 40
# Total Accepted:    70.7K
# Total Submissions: 104.5K
# Testcase Example:  '[4,2,5,7]'
#
# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
# 
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
# even, i is even.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# Example 1:
# 
# 
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been
# accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: [int]) -> [int]:
        B = [-1 for _ in range(len(A))]
        even = 0
        odd = 1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                B[even] = A[i]
                even += 2
            else:
                B[odd] = A[i]
                odd += 2
        return B
# @lc code=end

