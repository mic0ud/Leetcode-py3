#
# @lc app=leetcode id=540 lang=python3
#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (57.53%)
# Likes:    1035
# Dislikes: 72
# Total Accepted:    76.9K
# Total Submissions: 133.3K
# Testcase Example:  '[1,1,2,3,3,4,4,8,8]'
#
# You are given a sorted array consisting of only integers where every element
# appears exactly twice, except for one element which appears exactly once.
# Find this single element that appears only once.

# Example 1:
 
# Input: [1,1,2,2,3,4,4,8,8]
# Output: 2
# 
# 
# Example 2:

# Input: [3,3,7,10,10,11,11]
# Output: 10

# Note: Your solution should run in O(log n) time and O(1) space.


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: [int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        l, r = 0, n-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] == nums[mid-1]:
                if (mid-l) % 2 == 0:
                    r = mid
                else:
                    l = mid+1
            else:
                if (mid-l) % 2 == 0:
                    l = mid
                else:
                    r = mid-1
        return nums[l]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.singleNonDuplicate([3,3,7,7,10,11,11])
    s.singleNonDuplicate([1,1,2,3,3,4,4,8,8])
