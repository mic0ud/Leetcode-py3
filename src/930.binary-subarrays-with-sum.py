#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (39.88%)
# Likes:    334
# Dislikes: 20
# Total Accepted:    15K
# Total Submissions: 36.9K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, A: [int], S: int) -> int:
        prefixSum, res = 0, 0
        count = defaultdict(int)
        count[0] = 1
        for a in A:
            prefixSum += a
            # prefixSum = sum(0~i), target = S, prefixSum - (prefixSum - S) = S , check the occurence of prefixSum - S
            res += count[prefixSum-S] 
            count[prefixSum] += 1            
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.numSubarraysWithSum([1,0,1,0,1],2)
    s.numSubarraysWithSum([0,0,0,0,0],0)
