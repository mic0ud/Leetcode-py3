#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#
# https://leetcode.com/problems/make-array-strictly-increasing/description/
#
# algorithms
# Hard (40.54%)
# Likes:    192
# Dislikes: 7
# Total Accepted:    3.7K
# Total Submissions: 9.1K
# Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
#
# Given two integer arrays arr1 and arr2, return the minimum number of
# operations (possibly zero) needed to make arr1 strictly increasing.
# 
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j
# < arr2.length and do the assignment arr1[i] = arr2[j].
# 
# If there is no way to make arr1 strictly increasing, return -1.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6,
# 7].
# 
# 
# Example 3:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing.
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 
# 
# 
#

# @lc code=start
class Solution:
    def makeArrayIncreasing(self, arr1: [int], arr2: [int]) -> int:
        if not arr1:
            return -1
        n = len(arr1)
        if n == 1:
            return 0
        arr2 = sorted(list(set(arr2)))
        # swap[i][j]: min operations for arr1[:i] by assigning arr1[i] = arr2[j]
        # keep[i]: min operations for arr1[:i] without assigning arr1[i]
        swap = [[float('inf') for _ in range(len(arr2))] for _ in range(n)]
        keep = [float('inf') for _ in range(n)]
        for i in range(len(arr2)):
            swap[0][i] = 1
        keep[0] = 0
        # compare arr1[i], arr1[i-1], arr2[j] and arr2[j-1]
        # 1. arr1[i] > arr1[i-1]: keep[i] = keep[i-1]
        # 2. arr2[j] > arr1[i-1]: arr1[i] = arr2[j], swap[i][j] = keep[i-1] + 1
        # 3. arr1[i] > arr2[j]: arr1[i-1] = arr2[k] (k <= j), keep[i] = min(swap[i-1][k])
        # 4. arr2[j] > arr2[k] (k < j, condition always True): arr1[i] = arr2[j], swap[i][j] = min(swap[i-1][k]) + 1
        # for i in range(1, n):
        #     if arr1[i] > arr1[i-1]: 
        #         keep[i] = keep[i-1]
        #     for j in range(len(arr2)):
        #         if arr2[j] > arr1[i-1]:
        #             swap[i][j] = keep[i-1] + 1
        #         for k in range(j+1):
        #             if arr1[i] > arr2[k]:
        #                 keep[i] = min(keep[i], swap[i-1][k])
        #             if k < j:
        #                 swap[i][j] = min(swap[i][j], swap[i-1][k]+1)
        for i in range(1, n):
            minSwap = float('inf')
            minKeep = float('inf')
            for j in range(len(arr2)):
                if j > 0:
                    minSwap = min(minSwap, swap[i-1][j-1]+1)
                if arr1[i] > arr2[j]:
                    minKeep = min(minKeep, swap[i-1][j])
                if arr2[j] > arr1[i-1]:
                    swap[i][j] = keep[i-1] + 1
                if arr1[i] > arr1[i-1]:
                    keep[i] = keep[i-1]
                swap[i][j] = min(swap[i][j], minSwap)
                keep[i] = min(keep[i], minKeep)
        res = min(keep[n-1], min(swap[n-1])) 
        return -1 if res == float('inf') else res
# @lc code=end
# [0,11,6,1,4,3]\n[5,4,11,10,1,0]
if __name__ == '__main__':
    s = Solution()
    s.makeArrayIncreasing([1,5,3,6,7], [1,3,4])