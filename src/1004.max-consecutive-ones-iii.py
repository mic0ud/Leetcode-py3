#
# @lc app=leetcode id=1004 lang=python3
#
# [1004] Max Consecutive Ones III
#
# https://leetcode.com/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (55.55%)
# Likes:    602
# Dislikes: 12
# Total Accepted:    31.7K
# Total Submissions: 56.2K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
# 
# Return the length of the longest (contiguous) subarray that contains only
# 1s. 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# Example 2:
# 
# 
# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is
# underlined.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 0 <= K <= A.length
# A[i] is 0 or 1 
# 
# 
# 
#

# @lc code=start
from collections import deque
class Solution:
    def longestOnes(self, A: [int], K: int) -> int:
        n = len(A)
        if n <= K:
            return n
        count = K
        res, start, end = 0,0,0
        stack = deque() # []
        for i in range(n):
            if A[i] == 1:
                end = i
            else:
                stack.append(i)
                if count > 0:
                    count -= 1
                    end += 1
                else:
                    zeroIndex = stack.popleft()
                    start = zeroIndex + 1
                    end = i
            res = max(res, end-start+1)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)
