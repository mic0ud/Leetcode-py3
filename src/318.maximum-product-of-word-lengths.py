#
# @lc app=leetcode id=318 lang=python3
#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (49.62%)
# Likes:    687
# Dislikes: 65
# Total Accepted:    91.4K
# Total Submissions: 182K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.


# @lc code=start
class Solution:
    def maxProduct(self, words: [str]) -> int:
        n = len(words)
        res = 0
        for i in range(n-1):
            for j in range(i+1,n):
                if len(set(words[i])&set(words[j])) == 0:
                    res = max(res, len(words[i])*len(words[j]))
        return res
# @lc code=end

