#
# @lc app=leetcode id=462 lang=python3
#
# [462] Minimum Moves to Equal Array Elements II
#
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/description/
#
# algorithms
# Medium (52.88%)
# Likes:    436
# Dislikes: 42
# Total Accepted:    41.7K
# Total Submissions: 78.4K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty integer array, find the minimum number of moves required to
# make all array elements equal, where a move is incrementing a selected
# element by 1 or decrementing a selected element by 1.
# 
# You may assume the array's length is at most 10,000.
# 
# Example:
# 
# Input:
# [1,2,3]
# 
# Output:
# 2
# 
# Explanation:
# Only two moves are needed (remember each move increments or decrements one
# element):
# 
# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

# @lc code=start
from collections import Counter
class Solution:
    def minMoves2(self, nums: [int]) -> int:
        nums.sort()
        median = nums[len(nums)//2]
        return sum([abs(n-median) for n in nums])

    def minMoves2_SLOW(self, nums: [int]) -> int:
        nums.sort()
        count = Counter(nums)
        n, m, res = len(nums), 0, 0
        for k in sorted(count.keys()):
            m += count[k]
            if m >= n / 2 :
                m = k
                break
        for k, v in count.items():
            if k != m:
                res += abs(k-m)*v
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minMoves2([1,2,3])
    s.minMoves2([1,1,1,1,1,5,10])
