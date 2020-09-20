#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (51.34%)
# Likes:    1611
# Dislikes: 97
# Total Accepted:    140.5K
# Total Submissions: 273.1K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n^2.
#

# @lc code=start
import heapq
class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        n = len(matrix)
        res = []
        minHeap = []
        for i in range(n):
            heapq.heappush(minHeap, (matrix[i][0], i, 0)) # (val, row, col)
        while len(res) < k:
            minVal, row, col = heapq.heappop(minHeap)
            res.append(minVal)
            if col < n-1:
                heapq.heappush(minHeap, (matrix[row][col+1], row, col+1))
        return res[-1]
# @lc code=end
# [[1,3,5],[6,7,12],[11,14,14]]\n5
# [[1,3,5],[6,7,12],[11,14,14]]\n3
# [[1,5,9],[10,11,13],[12,13,15]]\n8

if __name__ == '__main__':
    s = Solution()
    s.kthSmallest([[1,5,9],[10,11,13],[12,13,15]], 8)
