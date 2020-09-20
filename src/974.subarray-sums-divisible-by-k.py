#
# @lc app=leetcode id=974 lang=python3
#
# [974] Subarray Sums Divisible by K
#
# https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (47.16%)
# Likes:    566
# Dislikes: 53
# Total Accepted:    23.4K
# Total Submissions: 49.3K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# Given an array A of integers, return the number of (contiguous, non-empty)
# subarrays that have a sum divisible by K.

# Example 1:
# 
# 
# Input: A = [4,5,0,-2,-3,1], K = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by K = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]

# Note:
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000


# @lc code=start
class Solution:
    def subarraysDivByK(self, A: [int], K: int) -> int:
        # prefix sum, search the prefix sum count if K*i was added to the sum
        prefixCount = [0 for _ in range(K)]
        prefixCount[0] = 1
        total = 0
        res = 0
        for a in A:
            total = (total + a) % K
            res += prefixCount[total]
            prefixCount[total] += 1            
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.subarraysDivByK([4,5,0,-2,-3,1],5)
