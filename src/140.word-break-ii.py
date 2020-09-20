#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (28.81%)
# Likes:    1335
# Dislikes: 295
# Total Accepted:    188.5K
# Total Submissions: 649.8K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
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
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#

# @lc code=start
from collections import defaultdict
class Solution:

    def wordBreak_COPIED(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        if s in memo: return memo[s]
        if not s: return []
        
        res = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res

    def wordBreak(self, s: str, wordDict: [str]) -> [str]:
        if not s or not wordDict:
            return []
        dp = defaultdict(list)
        def search(subs: str) -> []:
            if subs in dp.keys():
                return dp[subs]
            if not subs:
                return []
            tmp = []
            for w in wordDict:
                if not subs.startswith(w):
                    continue
                if subs == w:
                    tmp.append(w)
                else:
                    for r in search(subs[len(w):]):
                        tmp.append(w + ' ' + r)
            dp[subs] = tmp
            return tmp

        search(s)
        return dp[s]

    def wordBreak_TLE(self, s: str, wordDict: [str]) -> [str]:
        if not s or not wordDict:
            return []
        # dp = [False for _ in range(len(s)+1)]
        res = [[] for _ in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for w in wordDict:
                start = max(0, i-len(w))
                if s[start:i] == w and (len(res[start]) > 0 or i <= len(w)):
                    # dp[i] = True                                      
                    if start == 0:
                        res[i].append(w)
                    else:
                        for r in res[start]:
                            res[i].append(r + ' ' + w)
        return res[-1]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"])
# "pineapplepenapple"\n["apple", "pen", "applepen", "pine", "pineapple"]
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]
# "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"\n["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
