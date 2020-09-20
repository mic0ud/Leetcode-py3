#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (47.92%)
# Likes:    1073
# Dislikes: 101
# Total Accepted:    100.8K
# Total Submissions: 209.5K
# Testcase Example:  '["i", "love", "leetcode", "i", "love", "coding"]\n2'
#
# Given a non-empty list of words, return the k most frequent elements.
# Your answer should be sorted by frequency from highest to lowest. If two
# words have the same frequency, then the word with the lower alphabetical
# order comes first.
# 
# Example 1:
# 
# Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# Output: ["i", "love"]
# Explanation: "i" and "love" are the two most frequent words.
# ⁠   Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# 
# Example 2:
# 
# Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
# "is"], k = 4
# Output: ["the", "is", "sunny", "day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# ⁠   with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Note:
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Input words contain only lowercase letters.
# 
# 
# 
# Follow up:
# 
# Try to solve it in O(n log k) time and O(n) extra space.
# 
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        countMap = {}
        for w in words:
            if w in countMap.keys():
                countMap[w] += 1
            else:
                countMap[w] = 1

        frqMap = {}
        for kk, v in countMap.items():
            if v in frqMap.keys():
                frqMap[v].append(kk)
            else:
                frqMap[v] = [kk]
        res = []
        for kkk in reversed(sorted(frqMap.keys())):
            res += sorted(frqMap[kkk])
            if len(res) >= k:
                return res[:k]
        return res
# @lc code=end

