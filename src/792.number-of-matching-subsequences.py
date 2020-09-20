#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (45.62%)
# Likes:    699
# Dislikes: 47
# Total Accepted:    31.9K
# Total Submissions: 68.7K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#

# @lc code=start
from collections import defaultdict
from bisect import bisect_right
class Solution:
    def numMatchingSubseq(self, S: str, words: [str]) -> int:
        s_idx = defaultdict(list)
        for i in range(len(S)):
            s_idx[S[i]].append(i)

        def check(w: str) -> bool:
            curr = -1
            for c in w:
                idx = bisect_right(s_idx[c], curr)
                if not s_idx[c] or idx >= len(s_idx[c]):
                    return False
                curr = s_idx[c][idx]
            return True

        res = 0
        for w in words:
            if check(w):
                res += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numMatchingSubseq("abcde", ["a","bb","acd","ace"])
