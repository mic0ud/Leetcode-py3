#
# @lc app=leetcode id=1296 lang=python3
#
# [1296] Divide Array in Sets of K Consecutive Numbers
#
# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/description/
#
# algorithms
# Medium (50.81%)
# Likes:    294
# Dislikes: 32
# Total Accepted:    18.7K
# Total Submissions: 35.7K
# Testcase Example:  '[1,2,3,3,4,4,5,6]\n4'
#
# Given an array of integers nums and a positive integer k, find whether it's
# possible to divide this array into sets of k consecutive numbers
# Return True if its possible otherwise return False.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,3,4,4,5,6], k = 4
# Output: true
# Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# Output: true
# Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and
# [9,10,11].
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,3,2,2,1,1], k = 3
# Output: true
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# Explanation: Each array should be divided in subarrays of size 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 
# Note: This question is the same as 846:
# https://leetcode.com/problems/hand-of-straights/
#

# @lc code=start
from collections import Counter, deque
class Solution:
    def isPossibleDivide(self, nums: [int], k: int) -> bool:
        counter = Counter(nums)
        keys = deque(sorted(counter.keys()))
        while counter:
            i = keys[0]
            for j in range(k):
                if i+j not in counter:
                    return False
                counter[i+j] -= 1
                if counter[i+j] == 0:
                    counter.pop(i+j)
                    if i+j == keys[0]:
                        keys.popleft()
        return True

    def isPossibleDivide_SLOW(self, nums: [int], k: int) -> bool:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        i = 0
        while counter:
            for j in range(k):
                if keys[i]+j not in counter:
                    return False
                counter[keys[i]+j] -= 1
                if counter[keys[i]+j] == 0:
                    counter.pop(keys[i]+j)
            while i < len(keys) and keys[i] not in counter:
                i += 1
        return True
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.isPossibleDivide([3,2,1,2,3,4,3,4,5,9,10,11],3)
