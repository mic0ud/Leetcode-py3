#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (29.13%)
# Likes:    7000
# Dislikes: 414
# Total Accepted:    1.2M
# Total Submissions: 4.1M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        sMap = {}
        for i in range(len(s)):
            if s[i] in sMap.keys() and start <= sMap[s[i]]:
                start = sMap[s[i]] + 1
            else:
                res = max(res, i-start+1)
            sMap[s[i]] = i
        return res

    def ugly(self, s: str) -> int:
        sl = len(s)
        if sl <= 1:
            return sl
        sMap = {}
        sMap[s[0]] = 0
        res = 1
        i = 0
        k = 0
        while k < sl-1:
            maxLen = 1
            for j in range(i+1, sl):
                k = j
                if s[j] not in s[i:j]:    
                    maxLen += 1
                    sMap[s[j]] = j           
                    j += 1
                    k = j
                else:
                    i = sMap[s[j]] + 1
                    sMap[s[j]] = j
                    break               
            res = max(res, maxLen)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.lengthOfLongestSubstring("tmmzuxt")
