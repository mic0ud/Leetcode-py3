#
# @lc app=leetcode id=334 lang=python3
#
# [334] Increasing Triplet Subsequence
#
# https://leetcode.com/problems/increasing-triplet-subsequence/description/
#
# algorithms
# Medium (39.71%)
# Likes:    1284
# Dislikes: 116
# Total Accepted:    126.3K
# Total Submissions: 317K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given an unsorted array return whether an increasing subsequence of length 3
# exists or not in the array.
# 
# Formally the function should:
# 
# Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return
# false.
# 
# Note: Your algorithm should run in O(n) time complexity and O(1) space
# complexity.

# Example 1:
# 
# 
# Input: [1,2,3,4,5]
# Output: true

# Example 2:
# 
# 
# Input: [5,4,3,2,1]
# Output: false


# @lc code=start
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        left,mid = float('inf'),float('inf')
        for n in nums:
            if n > mid:
                return True
            if left < n < mid:
                mid = n
            elif n < left:
                left = n
        return False

    def increasingTriplet_VERBOSE(self, nums: [int]) -> bool:
        tmpLeft,left,mid = None,float('inf'),float('inf')
        for n in nums:
            if n > mid:
                return True
            if left < n < mid:
                mid = n
            elif n < left:
                if tmpLeft is None or n < tmpLeft:
                    tmpLeft = n
                elif n > tmpLeft:
                    left, mid = tmpLeft, n
                    tmpLeft = None
        return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.increasingTriplet([1,0,2,3])
