#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (44.02%)
# Likes:    270
# Dislikes: 20
# Total Accepted:    16.1K
# Total Submissions: 36K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an array A, partition it into two (contiguous) subarrays left and right
# so that:
# 
# 
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# 
# 
# Return the length of left after such a partitioning.  It is guaranteed that
# such a partitioning exists.

# Example 1:
# 
# 
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]

# Example 2:
# 
# 
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]

# Note:
# 
# 
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.


# @lc code=start
class Solution:
    def partitionDisjoint(self, A: [int]) -> int:
        d = [0]
        res = 1
        for i in range(1, len(A)):
            if A[i] > A[d[-1]]:
                d.append(i)               
            elif A[i] < A[d[0]]:
                res = i+1
                if len(d) > 1:                    
                    d.pop(0)
        return res
# @lc code=end
# [6,0,8,30,37,6,75,98,39,90,63,74,52,92,64]
if __name__ == '__main__':
    s = Solution()
    a = [12,75,26,38,56,59,83,55,49,52,27,48,77,21,27,79,54,15,59,22,34,35,81,67,2,41,40,0,73,61,75,8,86,42,49,83,43,16,2,54,26,35,15,63,31,24,51,86,6,35,42,37,83,51,34,21,71,57,61,76,50,1,43,32,19,13,67,87,3,33,38,34,34,84,38,76,52,7,27,49,2,78,56,28,70,6,64,87,100,97,99,97,97,100,100,100,97,89,98,100]
    s.partitionDisjoint(a)
    # s.partitionDisjoint([6,0,8,30,37,6,75,98,39,90,63,74,52,92,64])
