#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (57.53%)
# Likes:    2078
# Dislikes: 138
# Total Accepted:    276.9K
# Total Submissions: 479.8K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

# @lc code=start
class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k: int) -> [int]:
        if len(nums) <= 1:
            return nums
        countMap = {}
        for n in nums:
            if n not in countMap.keys():
                countMap[n] = 1
            else:
                countMap[n] += 1
        frqMap = {}
        for kk, v in countMap.items():
            if v in frqMap.keys():
                frqMap[v].append(kk)
            else:
                frqMap[v] = [kk]
        res = []
        for f in range(len(nums),0,-1):
            if f in frqMap.keys():
                for i in frqMap[f]:
                    res.append(i)
        return [res[j] for j in range(k)]
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.topKFrequent([-1,-1],1)