#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (34.97%)
# Likes:    271
# Dislikes: 52
# Total Accepted:    15.7K
# Total Submissions: 44.8K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# Given an integer array A, and an integer target, return the number of tuples
# i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
# 
# As the answer can be very large, return it modulo 10^9 + 7.

# Example 1:

# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.

# Example 2:

# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.

# Note:
 
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300


# @lc code=start
class Solution:
    def threeSumMulti(self, A: [int], target: int) -> int:


    def threeSumMulti_TLE(self, A: [int], target: int) -> int:
        n = len(A)
        # count[i]: count of twoSum == i
        count = [0 for _ in range(target+1)]
        res, mod = 0, 10**9 + 7
        for i in range(n):
            if target - A[i] >= 0:
                res = (res + count[target - A[i]]) % mod
            for j in range(i):
                if A[i]+A[j] <= target:
                    count[A[i]+A[j]] += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.threeSumMulti([1,1,2,2,2,2], 5)
