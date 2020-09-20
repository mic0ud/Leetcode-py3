#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (37.30%)
# Likes:    3057
# Dislikes: 167
# Total Accepted:    427.8K
# Total Submissions: 1.1M
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        for i in range(1,len(s)+1):
            for w in wordDict:
                wLength = len(w)
                if s[max(0, i-wLength):i] == w and (dp[max(0, i-wLength)] or i <= wLength):
                    dp[i] = True
        return dp[-1]

    def bruteForce(self, s: str, wordDict: [str]) -> bool:
        if s in wordDict:
            return True
        for i in range(1, len(s)):
            if s[:i] in wordDict and self.bruteForce(s[i:], wordDict):
                return True
        return False
# @lc code=end

# "catsandog"\n["cats", "dog", "sand", "and", "cat"]

if __name__ == '__main__':
    s = Solution()
    s.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"])