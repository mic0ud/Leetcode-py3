#
# @lc app=leetcode id=1048 lang=python3
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (51.39%)
# Likes:    433
# Dislikes: 30
# Total Accepted:    30K
# Total Submissions: 57.3K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
# 
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
# 
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
# 
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
 
# Example 1:

# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
 
# Note:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

# @lc code=start
from collections import defaultdict
class Solution:
    def longestStrChain(self, words: [str]) -> int:
        words = sorted(words, key=lambda w: len(w))
        # dp[i]: ongest word chain end at i
        # dp = [1 for _ in range(len(words))]
        memo = defaultdict(int)
        memo[words[0]] = 1
        res = 1
        for i in range(1, len(words)):
            if len(words[i]) == len(words[0]):
                memo[words[i]] = 1
                continue
            for j in range(len(words[i])):
                tmp = words[i][:j] + words[i][j+1:]
                memo[words[i]] = max(memo[words[i]], memo[tmp] + 1)
                res = max(res, memo[words[i]])
        return res
# @lc code=end
# ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
if __name__ == '__main__':
    s = Solution()
    s.longestStrChain(["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"])
