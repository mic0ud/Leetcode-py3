#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (44.22%)
# Likes:    251
# Dislikes: 12
# Total Accepted:    16.8K
# Total Submissions: 37.8K
# Testcase Example:  '[1,2,2]'
#
# Given an array of integers A, a move consists of choosing any A[i], and
# incrementing it by 1.
# 
# Return the least number of moves to make every value in A unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
# 
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        if not A:
            return 0
        maxVal = max(A)
        minVal = min(A)
        aMap = {}
        for i in range(minVal, maxVal+len(A)):
            aMap[i] = 0
        for a in A:
            aMap[a] += 1

        sortedKeys = sorted(aMap.keys())
        res = 0
        nextPos = 0
        for i in range(len(sortedKeys)-1):
            while aMap[sortedKeys[i]] > 1:
                j = (nextPos if nextPos > sortedKeys[i] else i) + 1
                while j < len(sortedKeys) and aMap[sortedKeys[j]] > 0:
                    j += 1
                nextPos = j
                res += sortedKeys[j] - sortedKeys[i]
                aMap[sortedKeys[i]] -= 1
                aMap[sortedKeys[j]] = 1
        return res
# @lc code=end

