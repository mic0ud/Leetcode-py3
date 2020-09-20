#
# @lc app=leetcode id=890 lang=python3
#
# [890] Find and Replace Pattern
#
# https://leetcode.com/problems/find-and-replace-pattern/description/
#
# algorithms
# Medium (72.28%)
# Likes:    533
# Dislikes: 57
# Total Accepted:    42.8K
# Total Submissions: 58.9K
# Testcase Example:  '["abc","deq","mee","aqq","dkd","ccc"]\n"abb"'
#
# You have a list of words and a pattern, and you want to know which words in
# words matches the pattern.
# 
# A word matches the pattern if there exists a permutation of letters p so that
# after replacing every letter x in the pattern with p(x), we get the desired
# word.
# 
# (Recall that a permutation of letters is a bijection from letters to letters:
# every letter maps to another letter, and no two letters map to the same
# letter.)
# 
# Return a list of the words in words that match the given pattern. 
# 
# You may return the answer in any order.

# Example 1:
# 
# 
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a ->
# m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a
# permutation,
# since a and b map to the same letter.
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20


# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: [str], pattern: str) -> [str]:
        res = []
        for w in words:
            if self.check(w, pattern):
                res.append(w)
        return res

    def check(self, s1,s2) -> bool:
        m = {}
        for i in range(len(s1)):
            if s2[i] not in m:
                if s1[i] in m.values():
                    return False
                m[s2[i]] = s1[i]
            else:
                if m[s2[i]] != s1[i]:
                    return False
        return True
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.check('ccc','abb')
    s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], 'abb')
