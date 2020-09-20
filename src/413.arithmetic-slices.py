#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (56.73%)
# Likes:    802
# Dislikes: 149
# Total Accepted:    77.5K
# Total Submissions: 135.9K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of number is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 
# 
# A slice (P, Q) of array A is called arithmetic if the sequence:
# ⁠   A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# means that P + 1 < Q.
# 
# The function should return the number of arithmetic slices in the array A. 
# 
# 
# Example:
# 
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.


# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: [int]) -> int:
        n = len(A)
        if n < 3:
            return 0
        res, a, count, i = 0, A[1]-A[0], 0, 2
        while i < n:
            while i < n and A[i]-A[i-1] == a:
                i += 1
                count += 1
            if count > 0:
                res += sum([j for j in range(1,count+1)])
            if i < n:
                a, count = A[i]-A[i-1], 0
                i += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numberOfArithmeticSlices([1,2,3,4,6,7,10,9,8])
