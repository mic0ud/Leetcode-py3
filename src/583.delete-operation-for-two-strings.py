#
# @lc app=leetcode id=583 lang=python3
#
# [583] Delete Operation for Two Strings
#
# https://leetcode.com/problems/delete-operation-for-two-strings/description/
#
# algorithms
# Medium (46.13%)
# Likes:    877
# Dislikes: 24
# Total Accepted:    41.4K
# Total Submissions: 88.7K
# Testcase Example:  '"sea"\n"eat"'
#
# 
# Given two words word1 and word2, find the minimum number of steps required to
# make word1 and word2 the same, where in each step you can delete one
# character in either string.
# 
# 
# Example 1:
# 
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make
# "eat" to "ea".

# Note:
# 
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.


# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        n1, n2 = len(word1), len(word2)
        if not word1:
            return n2
        if not word2:
            return n1
        # dp[i][j]: operations needed for word1[:i+1] and word2[:j+1]
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        for i in range(n1):
            dp[i][0] = i+1+1 if word2[0] not in word1[:i+1] else i
        for j in range(n2):
            dp[0][j] = j+1+1 if word1[0] not in word2[:j+1] else j
        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+2)
        return dp[-1][-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.minDistance("delete", "leetcode")
    s.minDistance("a", "ba")
