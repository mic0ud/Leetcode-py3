#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (27.77%)
# Likes:    5395
# Dislikes: 795
# Total Accepted:    545.6K
# Total Submissions: 2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#

# @lc code=start
import bisect
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2: [int]) -> float:
        if len(nums2) < len(nums1):
            return self.findMedianSortedArrays(nums2, nums1)
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 == 0:
            return nums2[n2//2] if n2 % 2 > 0 else (nums2[n2//2]+nums2[n2//2-1])/2
        half = (n1+n2) // 2 # left part
        left, right = 0, n1
        # l1,l2,r1,r2 = float('-inf'), float('inf'), float('-inf'), float('inf')
        while left <= right:
            k1 = (left + right)//2 # take k1 ints from nums1
            k2 = half - k1 # take k2 ints from nums2
            l1 = nums1[k1-1] if k1 > 0 else float('-inf')
            l2 = nums1[k1] if k1 < n1 else float('inf')
            r1 = nums2[k2-1] if k2 > 0 else float('-inf')
            r2 = nums2[k2] if k2 < n2 else float('inf')
            if max(l1, r1) <= min(l2,r2): # got it
                break
            else:
                if l1 > r1:
                    right = k1
                else:
                    left = k1+1
        if (n1+n2) % 2 > 0:
            return min(l2,r2)
        return (max(l1,r1)+min(l2,r2))/2
# @lc code=end
# [3]\n[-2,-1]
if __name__ == '__main__':
    s = Solution()
    s.findMedianSortedArrays([3],[-3,-1])
