#
# @lc app=leetcode id=474 lang=python3
#
# [474] Ones and Zeroes
#
# https://leetcode.com/problems/ones-and-zeroes/description/
#
# algorithms
# Medium (40.97%)
# Likes:    780
# Dislikes: 189
# Total Accepted:    41.1K
# Total Submissions: 98.3K
# Testcase Example:  '["10","0001","111001","1","0"]\n5\n3'
#
# In the computer world, use restricted resource you have to generate maximum
# benefit is what we always want to pursue.
# 
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the
# other hand, there is an array with strings consisting of only 0s and 1s.
# 
# Now your task is to find the maximum number of strings that you can form with
# given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# Note:

# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.

# Example 1:
 
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# 
# Explanation: This are totally 4 strings can be formed by the using of 5 0s
# and 3 1s, which are “10,”0001”,”1”,”0”

# Example 2:

# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# 
# Explanation: You could form "10", but then you'd have nothing left. Better
# form "0" and "1".

# @lc code=start
from functools import cmp_to_key
class Solution:
    def findMaxForm(self, strs: [str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        counts = [[s.count('0'), s.count('1')] for s in strs]
        for z, o in counts:
            for i in range(m,-1,-1):
                for j in range(n,-1,-1):
                    if z <= i and o <= j:
                        dp[i][j] = max(dp[i-z][j-o]+1, dp[i][j])
        return dp[m][n]  

    def findMaxForm_SLOW(self, strs: [str], m: int, n: int) -> int:
        dp = [[[0 for _ in range(len(strs))] for _ in range(n+1)] for _ in range(m+1)]
        counts = [[s.count('0'), s.count('1')] for s in strs]
        for i in range(m+1):
            for j in range(n+1):
                for k in range(len(counts)):
                    zero, one = counts[k][0], counts[k][1]
                    if zero <= i and one <= j:
                        dp[i][j][k] = 1 if k == 0 else max(dp[i-zero][j-one][k-1]+1, dp[i][j][k-1])
                    else:
                        dp[i][j][k] = 0 if k == 0 else dp[i][j][k-1]
        return dp[m][n][len(strs)-1]

    def findMaxForm_WRONG(self, strs: [str], m: int, n: int) -> int:
        k = ['0' if m <= n else '1']
        def mycmp(s1, s2) -> int:
            if s1.count(k[0]) > s2.count(k[0]):
                return 1
            elif s1.count(k[0]) < s2.count(k[0]):
                return -1
            else:
                return len(s1) - len(s2)
        strs.sort(key=cmp_to_key(mycmp))
        strs.sort(key=lambda s: s.count('0' if m <= n else '1'))
        res = 0
        for _ in range(len(strs)):
            m -= strs[0].count('0')
            n -= strs[0].count('1')
            if m >= 0 and n >= 0:
                res += 1
                k = ['0' if m <= n else '1']     
                strs = sorted(strs[1:], key=cmp_to_key(mycmp))  
            else:
                break  
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findMaxForm(["011111","001","001"],4,5) # 2
    s.findMaxForm(["10","0001","111001","1","0"],4,3) # 3
    s.findMaxForm(["1100","100000","011111"],6,6)
    s.findMaxForm(["111","1000","1000","1000"],9,3)
    s.findMaxForm(["10", "0", "1"],1,1)
    s.findMaxForm(["10", "0001", "111001", "1", "0"],5,3)
