#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (44.91%)
# Likes:    906
# Dislikes: 62
# Total Accepted:    49.7K
# Total Submissions: 109.5K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string s that consists of only uppercase English letters, you can
# perform at most k operations on that string.
# 
# In one operation, you can choose any character of the string and change it to
# any other uppercase English character.
# 
# Find the length of the longest sub-string containing all repeating letters
# you can get after performing the above operations.
# 
# Note:
# Both the string's length and k will not exceed 10^4.
# 
# Example 1:

# Input:
# s = "ABAB", k = 2
# 
# Output:
# 4
# 
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# 
# 
# Input:
# s = "AABABBA", k = 1
# 
# Output:
# 4
# 
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.


# @lc code=start
from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        if k >= n:
            return n
        count = defaultdict(int)
        maxCharCount, start, ops, res = 0, 0, 0, k
        for end in range(n):
            count[s[end]] += 1
            maxCharCount = max(maxCharCount, count[s[end]])
            ops = end-start+1-maxCharCount
            if ops > k:                
                count[s[start]] -= 1
                start += 1
            else:
                res = max(res, end-start+1)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.characterReplacement("ABAA", 0)
