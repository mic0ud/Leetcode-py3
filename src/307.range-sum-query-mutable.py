#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (31.09%)
# Likes:    1057
# Dislikes: 71
# Total Accepted:    94.2K
# Total Submissions: 291K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# Note:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#

# @lc code=start
class NumArray:
    # Use self.c to represent Binary Indexed Tree. Section sums are stored in self.c[1..len(nums)]. x & -x is lowbit function, which will return x's rightmost bit 1, e.g. lowbit(7) = 1, lowbit(20) = 4.
    # self.c[1] = nums[0]
    # self.c[2] = nums[0] + nums[1]
    # self.c[3] = nums[2]
    # self.c[4] = nums[0] + nums[1] + nums[2] + nums[3]
    # self.c[5] = nums[4]
    # self.c[6] = nums[4] + nums[5]
    # self.c[7] = nums[6]
    # self.c[8] = nums[0] + nums[1] + nums[2] + nums[3] + nums[4] + nums[5] + nums[6] + nums[7]
    def __init__(self, nums: [int]):
        self.nums = nums
        self.binaryIndexedTree = [0 for _ in range(len(nums)+1)]
        for i in range(len(nums)):
            k = i+1
            while k <= len(nums):
                self.binaryIndexedTree[k] += self.nums[i]
                k += (k & -k)

    def update(self, i: int, val: int) -> None:
        d = val - self.nums[i]
        self.nums[i] = val
        k = i+1
        while k <= len(self.nums):
            self.binaryIndexedTree[k] += d
            k += (k & -k)

    def sumRange(self, i: int, j: int) -> int:
        res, j = 0, j+1
        while j > 0:
            res += self.binaryIndexedTree[j]
            j -= (j & -j)
        while i > 0:
            res -= self.binaryIndexedTree[i]
            i -= (i & -i)
        return res
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
# @lc code=end
if __name__ == '__main__':
    s = NumArray([1, 3, 5])
    s.sumRange(0,2)
    s.update(1,2)
    s.sumRange(0,2)
