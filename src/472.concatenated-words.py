#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (38.38%)
# Likes:    433
# Dislikes: 82
# Total Accepted:    37.9K
# Total Submissions: 95.7K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given a list of words (without duplicates), please write a program that
# returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
# 
# Example:
# 
# Input:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat"
# can be concatenated by "rat", "cat", "dog" and "cat".
# 
# 
# 
# Note:
# 
# The number of elements of the given array will not exceed 10,000 
# The length sum of elements in the given array will not exceed 600,000. 
# All the input string will only include lower case letters.
# The returned elements order does not matter. 
# 
# 
#

# @lc code=start
class Solution:
    def findAllConcatenatedWordsInADict(self, words: [str]) -> [str]:
        res = []
        wordSet = set(words)
        def dfs(w: str) -> bool:
            for i in range(1, len(w)):
                prefix = w[:i]
                suffix = w[i:]
                if prefix in wordSet and suffix in wordSet:
                    return True
                if prefix in wordSet and dfs(suffix):
                    return True
                # if suffix in wordSet and dfs(prefix):
                #     return True
            return False
        
        for word in words:
            if dfs(word):
                res.append(word)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"])
