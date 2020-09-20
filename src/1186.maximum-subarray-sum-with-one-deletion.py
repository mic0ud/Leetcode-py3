#
# @lc app=leetcode id=1186 lang=python3
#
# [1186] Maximum Subarray Sum with One Deletion
#
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/description/
#
# algorithms
# Medium (34.49%)
# Likes:    348
# Dislikes: 14
# Total Accepted:    11.2K
# Total Submissions: 31.1K
# Testcase Example:  '[1,-2,0,3]'
#
# Given an array of integers, return the maximum sum for a non-empty subarray
# (contiguous elements) with at most one element deletion. In other words, you
# want to choose a subarray and optionally delete one element from it so that
# there is still at least one element left and the sum of the remaining
# elements is maximum possible.
# 
# Note that the subarray needs to be non-empty after deleting one element.

# Example 1:

# Input: arr = [1,-2,0,3]
# Output: 4
# Explanation: Because we can choose [1, -2, 0, 3] and drop -2, thus the
# subarray [1, 0, 3] becomes the maximum value.
# 
# Example 2:

# Input: arr = [1,-2,-2,3]
# Output: 3
# Explanation: We just choose [3] and it's the maximum sum.

# Example 3:

# Input: arr = [-1,-1,-1,-1]
# Output: -1
# Explanation: The final subarray needs to be non-empty. You can't choose [-1]
# and delete -1 from it, then get an empty subarray to make the sum equals to
# 0.
 
# Constraints:

# 1 <= arr.length <= 10^5
# -10^4 <= arr[i] <= 10^4


# @lc code=start
class Solution:
    def maximumSum(self, arr: [int]) -> int:
        n = len(arr)
        dp1_0 = [float('-inf') for _ in range(n)] # delete one
        dp1_1 = [float('-inf') for _ in range(n)] # without deleting
        dp2_0 = [float('-inf') for _ in range(n)]
        dp2_1 = [float('-inf') for _ in range(n)]
        res, dp1_1[0] = arr[0], arr[0]
        for i in range(1,n):
            dp1_0[i] = max(arr[i], dp1_0[i-1]+arr[i], dp1_1[i-1])
            dp1_1[i] = max(arr[i], dp1_1[i-1]+arr[i])
            dp2_0[i] = max(dp1_0[i-1], dp2_0[i-1])
            dp2_1[i] = max(dp1_1[i-1], dp2_1[i-1])
            res = max(res, dp1_0[i], dp1_1[i], dp2_0[i], dp2_1[i])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maximumSum([1,-2,0,3])
    s.maximumSum([1,-2,-2,3])
    s.maximumSum([-1,-1,-1,-1])
