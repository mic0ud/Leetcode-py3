#
# @lc app=leetcode id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (56.10%)
# Likes:    715
# Dislikes: 41
# Total Accepted:    28.1K
# Total Submissions: 49.4K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to
# make two strings equal.
# 
# Example 1:
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# 
# Example 2:
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e]
# to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Note:
# 0 < s1.length, s2.length <= 1000
# All elements of each string will have an ASCII value in [97, 122]. 
# 
#

# @lc code=start
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        if s1 == s2:
            return 0
        n1, n2 = [ord(c1) for c1 in s1], [ord(c2) for c2 in s2]
        dp = [[0 for _ in range(len(s2))] for _ in range(len(s1))]
        for i in range(len(s1)):
            dp[i][0] = sum(n1[:i+1])+n2[0] if n2[0] not in n1[:i+1] else sum(n1[:i+1])-n2[0]
        for j in range(len(s2)):
            dp[0][j] = sum(n2[:j+1])+n1[0] if n1[0] not in n2[:j+1] else sum(n2[:j+1])-n1[0]
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if n1[i] == n2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+n1[i], dp[i][j-1]+n2[j])
        return dp[-1][-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.minimumDeleteSum('delete', 'leet')
    s.minimumDeleteSum('sea', 'eat')
