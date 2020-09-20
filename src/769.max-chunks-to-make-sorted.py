#
# @lc app=leetcode id=769 lang=python3
#
# [769] Max Chunks To Make Sorted
#
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/
#
# algorithms
# Medium (53.14%)
# Likes:    637
# Dislikes: 102
# Total Accepted:    31.9K
# Total Submissions: 59.5K
# Testcase Example:  '[4,3,2,1,0]'
#
# Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], we
# split the array into some number of "chunks" (partitions), and individually
# sort each chunk.  After concatenating them, the result equals the sorted
# array.
# 
# What is the most number of chunks we could have made?
# 
# Example 1:
# 
# 
# Input: arr = [4,3,2,1,0]
# Output: 1
# Explanation:
# Splitting into two or more chunks will not return the required result.
# For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2],
# which isn't sorted.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,0,2,3,4]
# Output: 4
# Explanation:
# We can split into two chunks, such as [1, 0], [2, 3, 4].
# However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks
# possible.
# 
# 
# Note:
# 
# 
# arr will have length in range [1, 10].
# arr[i] will be a permutation of [0, 1, ..., arr.length - 1].


# @lc code=start
class Solution:
    def maxChunksToSorted(self, arr: [int]) -> int:
        def search(i, j, res: []):
            while j <= len(arr) and sorted(arr[i:j]) != [k for k in range(i, j)]:
                j += 1
            if j >= len(arr):
                res[0] += 1
                return
            else:
                res[0] += 1
                i = j
                search(i,j+1, res)
        res = [0]
        search(0,1, res)
        return res[0]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxChunksToSorted([1,0,2,3,4])
