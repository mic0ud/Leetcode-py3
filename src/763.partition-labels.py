#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#
# https://leetcode.com/problems/partition-labels/description/
#
# algorithms
# Medium (72.90%)
# Likes:    1442
# Dislikes: 77
# Total Accepted:    80.1K
# Total Submissions: 109.7K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 
# A string S of lowercase letters is given.  We want to partition this string
# into as many parts as possible so that each letter appears in at most one
# part, and return a list of integers representing the size of these parts.
# 
# 
# Example 1:
# 
# Input: S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
# splits S into less parts.
# 
# 
# 
# Note:
# S will have length in range [1, 500].
# S will consist of lowercase letters ('a' to 'z') only.
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def partitionLabels(self, S: str) -> [int]:
        labelSet, counter = set(), Counter(S)
        start, end, res = 0, 0, [] 
        while end < len(S):
            labelSet.add(S[end])
            counter[S[end]] -= 1
            valid = True
            for label in labelSet:
                if counter[label] > 0:
                    valid = False
                    break
            if valid:
                res.append(end-start+1)
                labelSet = set()
                end += 1
                start = end
            else:
                end += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.partitionLabels("ababcbacadefegdehijhklij")
