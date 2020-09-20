#
# @lc app=leetcode id=926 lang=python3
#
# [926] Flip String to Monotone Increasing
#
# https://leetcode.com/problems/flip-string-to-monotone-increasing/description/
#
# algorithms
# Medium (51.24%)
# Likes:    441
# Dislikes: 15
# Total Accepted:    17.4K
# Total Submissions: 33.9K
# Testcase Example:  '"00110"'
#
# A string of '0's and '1's is monotone increasing if it consists of some
# number of '0's (possibly 0), followed by some number of '1's (also possibly
# 0.)
# 
# We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or
# a '1' to a '0'.
# 
# Return the minimum number of flips to make S monotone increasing.
 
# Example 1:

# Input: "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.

# Example 2:

# Input: "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.

# Example 3:

# Input: "00011000"
# Output: 2
# Explanation: We flip to get 00000000.

# Note:
 
# 1 <= S.length <= 20000
# S only consists of '0' and '1' characters.

# @lc code=start
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        '''
        we assume the string after flip is s = '0'*i + '1'*j, the index of first '1' is i

        we just need to find the i in the initial string. We make all 1 before index i flip to 0, and make all 0 after index i flip to 1. 
        Then, we get the right answer.

        for instance, s = 010110.
        if we choose the first 1(index=1) as i, we need to make all 1 before i flip to 0(all 0), make all 0 after i flip to 1(all 2),so the answer is 2.
        if we choose the second 1(index=3) as i, the answer is 1 + 1 = 2
        if we choose the third 1(index=4) as i, the answer is 2 + 1 = 3
        and so on
        '''
        # cnt0 to record the number of 0 after i, cnt1 to record th number of 1 before i
        n = len(S)
        ctn0 = S.count('0')
        ctn1 = 0
        res = n - ctn0
        for s in S:
            if s == '0':
                ctn0 -= 1
            else:
                res = min(res, ctn0+ctn1)
                ctn1 += 1
        return res

    def minFlipsMonoIncr_DP_SLOW(self, S: str) -> int:
        n = len(S)
        if n <= 1:
            return 0
        # dp0[i]: min flips for S[:i] with S[i-1] flipped to 0
        # dp1[i]: min flips for S[:i] with S[i-1] flipped to 1
        dp0 = [float('inf') for _ in range(n+1)]
        dp1 = [float('inf') for _ in range(n+1)]
        dp0[0], dp1[0] = 0, 0
        if S[0] == '0':
            dp0[1] = 0
            dp1[1] = 1
        else:
            dp0[1] = 1
            dp1[1] = 0
        for i in range(2, n+1):
            if S[i-1] == '0':
                dp0[i] = dp0[i-1]
                dp1[i] = min(dp1[i-1], dp0[i-1]) + 1
            else:
                dp1[i] = min(dp1[i-1], dp0[i-1])
                dp0[i] = dp0[i-1] + 1
        return min(dp0[n], dp1[n])
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minFlipsMonoIncr("00011000")
