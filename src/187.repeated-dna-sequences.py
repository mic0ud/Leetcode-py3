#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (38.21%)
# Likes:    698
# Dislikes: 267
# Total Accepted:    158.3K
# Total Submissions: 410.8K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> [str]:
        n, res = len(s), set()
        if n < 10:
            return res
        count = defaultdict(int)
        for i in range(n-9):
            count[s[i:i+10]] += 1
            if count[s[i:i+10]] > 1:
                res.add(s[i:i+10])
        return list(res)
        
    def suffix_prefix(self, s:str) -> [int]:
        res, i = [0], 0
        for j in range(1, len(s)):
            while i > 0 and s[i] != s[j]:
                i = res[i-1]
            if s[j] == s[i]:
                res.append(i+1)
                i += 1
            else:
                res.append(0)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')
    s.findRepeatedDnaSequences('AAAAAAAAAAA')
    # s.suffix_prefix('ababcdabc')
