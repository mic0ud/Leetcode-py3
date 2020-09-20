#
# @lc app=leetcode id=820 lang=python3
#
# [820] Short Encoding of Words
#
# https://leetcode.com/problems/short-encoding-of-words/description/
#
# algorithms
# Medium (48.57%)
# Likes:    194
# Dislikes: 51
# Total Accepted:    11K
# Total Submissions: 22.5K
# Testcase Example:  '["time", "me", "bell"]'
#
# Given a list of words, we may encode it by writing a reference string S and a
# list of indexes A.
# 
# For example, if the list of words is ["time", "me", "bell"], we can write it
# as S = "time#bell#" and indexes = [0, 2, 5].
# 
# Then for each index, we will recover the word by reading from the reference
# string from that index until we reach a "#" character.
# 
# What is the length of the shortest reference string S possible that encodes
# the given words?
# 
# Example:
# 
# 
# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: S = "time#bell#" and indexes = [0, 2, 5].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 2000.
# 1 <= words[i].length <= 7.
# Each word has only lowercase letters.
# 
# 
#

# @lc code=start
class Solution:
    def minimumLengthEncoding(self, words: [str]) -> int:
        s = set(words)
        for w in words:
            for i in range(1, len(w)):
                s.discard(w[i:])
        return sum(len(w) + 1 for w in s)

    def minimumLengthEncoding_SLOW(self, words: [str]) -> int:
        if not words:
            return 0
        newWrods = list(set(words))
        longest = '#'.join(newWrods) + '#'
        res = len(longest)
        for w in newWrods:
            count = longest.count(w+'#')
            if count > 1:
                res -= len(w) + 1
        return res

    def minimumLengthEncoding_BRUTE_TLE(self, words: [str]) -> int:
        if not words:
            return 0
        res = [words[0] + '#']
        for w in words[1:]:
            curr = w + '#'
            for i in range(len(res)):
                if curr in res[i]:
                    break
                if res[i] in curr:
                    res[i] = curr
                    break
                res.append(curr)
        return len(''.join(res)) 
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    s.minimumLengthEncoding(["time", "atime", "btime"])