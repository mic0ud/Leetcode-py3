#
# @lc app=leetcode id=433 lang=python3
#
# [433] Minimum Genetic Mutation
#
# https://leetcode.com/problems/minimum-genetic-mutation/description/
#
# algorithms
# Medium (39.60%)
# Likes:    342
# Dislikes: 42
# Total Accepted:    27.3K
# Total Submissions: 67.7K
# Testcase Example:  '"AACCGGTT"\n"AACCGGTA"\n["AACCGGTA"]'
#
# A gene string can be represented by an 8-character long string, with choices
# from "A", "C", "G", "T".
# 
# Suppose we need to investigate about a mutation (mutation from "start" to
# "end"), where ONE mutation is defined as ONE single character changed in the
# gene string.
# 
# For example, "AACCGGTT" -> "AACCGGTA" is 1 mutation.
# 
# Also, there is a given gene "bank", which records all the valid gene
# mutations. A gene must be in the bank to make it a valid gene string.
# 
# Now, given 3 things - start, end, bank, your task is to determine what is the
# minimum number of mutations needed to mutate from "start" to "end". If there
# is no such a mutation, return -1.
# 
# Note:
# 
# 
# Starting point is assumed to be valid, so it might not be included in the
# bank.
# If multiple mutations are needed, all mutations during in the sequence must
# be valid.
# You may assume start and end string is not the same.

# Example 1:

# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# return: 1
 
# Example 2:

# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# return: 2

# Example 3:

# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# return: 3


# @lc code=start
from queue import Queue
class Solution:
    def minMutation(self, start: str, end: str, bank: [str]) -> int:
        bank = set(bank)
        q = Queue()
        q.put([start])
        seen = set()
        res = -1
        while not q.empty():
            res += 1
            curr = q.get()
            next_ = []
            for c in curr:
                if c == end:
                    return res
                seen.add(c)
                next_ += self.generateNext(c, seen, bank)
            if next_:
                q.put(next_)
        return -1

    def generateNext(self, gene, seen, bank) -> []:
        res = []
        for i,c in enumerate(gene):
            for g in 'ACGT':
                if g != c:
                    tmp = gene[:i]+g+gene[i+1:]
                    if tmp not in seen and tmp in bank:
                        res.append(tmp)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minMutation("AACCGGTT","AACCGGTA",["AACCGGTA"])
    s.minMutation("AAAAACCC","AACCCCCC",["AAAACCCC", "AAACCCCC", "AACCCCCC"])
    s.minMutation("AACCGGTT","AAACGGTA",["AACCGGTA", "AACCGCTA", "AAACGGTA"])
