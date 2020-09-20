#
# @lc app=leetcode id=954 lang=python3
#
# [954] Array of Doubled Pairs
#
# https://leetcode.com/problems/array-of-doubled-pairs/description/
#
# algorithms
# Medium (35.36%)
# Likes:    173
# Dislikes: 37
# Total Accepted:    14.1K
# Total Submissions: 39.8K
# Testcase Example:  '[3,1,3,6]'
#
# Given an array of integers A with even length, return true if and only if it
# is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0
# <= i < len(A) / 2.

# Example 1:

# Input: [3,1,3,6]
# Output: false
 
# Example 2:

# Input: [2,1,2,6]
# Output: false

# Example 3:
 
# Input: [4,-2,2,-4]
# Output: true
# Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or
# [2,4,-2,-4].
 
# Example 4:

# Input: [1,2,4,16,8,4]
# Output: false

# Note:
# 
# 
# 0 <= A.length <= 30000
# A.length is even
# -100000 <= A[i] <= 100000


# @lc code=start
from collections import defaultdict
class Solution:
    def canReorderDoubled(self, A: [int]) -> bool:
        countPositive, maxP = defaultdict(int), 0
        countNegative, maxN = defaultdict(int), 0
        for a in A:
            if a > 0:
                countPositive[a] += 1
                maxP = max(maxP, a)
            else:
                countNegative[a] += 1
                maxN = min(maxN, a)
        for k in sorted(countPositive.keys()):
            if 2*k <= maxP:
                while countPositive[k] > 0:
                    countPositive[k] -= 1
                    countPositive[2*k] -= 1
        for k in sorted(countNegative.keys(), reverse=True):
            if 2*k >= maxN:
                while countNegative[k] > 0:
                    countNegative[k] -= 1
                    countNegative[2*k] -= 1
        for v in countPositive.values():
            if v != 0:
                return False
        for v in countNegative.values():
            if v != 0:
                return False
        return True
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.canReorderDoubled([1,2,4,16,8,4,2,32])
