#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
#
# algorithms
# Medium (34.86%)
# Likes:    895
# Dislikes: 74
# Total Accepted:    80K
# Total Submissions: 229K
# Testcase Example:  '[1,7,11]\n[2,4,6]\n3'
#
# You are given two integer arrays nums1 and nums2 sorted in ascending order
# and an integer k.
# 
# Define a pair (u,v) which consists of one element from the first array and
# one element from the second array.
# 
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]] 
# Explanation: The first 3 pairs are returned from the sequence: 
# [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
# 
# Example 2:
# 
# 
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence: 
# [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
# 
# 
#

# @lc code=start
import heapq
class Solution:
    # def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    def kSmallestPairs(self, nums1, nums2, k: int) -> [[int]]:
        if not nums1 or not nums2:
            return []
        res = []
        minHeap = []
        n1 = 0
        n2 = 0
        while len(res) < min(k, len(nums1)*len(nums2)):
            if n2 <= n1:
                for a in range(n1, len(nums1)):
                    heapq.heappush(minHeap, (nums1[a]+nums2[n2], [nums1[a], nums2[n2]]))
                # for nums2, max loops -> n1
                for b in range(n2, len(nums2)):
                    if b != n1:
                        heapq.heappush(minHeap, (nums1[n1]+nums2[b], [nums1[n1], nums2[b]]))
            res.append(heapq.heappop(minHeap)[1])
            n1 = min(n1+1, len(nums1)-1)
            n2 = min(n2+1, len(nums2)-1)
        return res
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.kSmallestPairs([1], [3,5,6,7,8,100], 4)

# [1,1,2]
# [1,2,3]
# 10
# [1,1,2]\n[1,2,2]\n10
# [1]\n[3,5,6,7,8,100]\n4