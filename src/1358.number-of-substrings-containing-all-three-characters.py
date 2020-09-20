#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (55.08%)
# Likes:    254
# Dislikes: 3
# Total Accepted:    7.6K
# Total Submissions: 13.6K
# Testcase Example:  '"abcabc"'
#
# Given a string s consisting only of characters a, b and c.
# 
# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again). 
# 
# 
# Example 2:
# 
# 
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb". 
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
# 
#

# @lc code=start
from collections import defaultdict, deque, Counter
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        return self.at_most_k(s,3) - self.at_most_k(s,2)

    def at_most_k(self, s: str, k: int) -> int:
        counter = Counter()
        res = i = 0
        for j,c in enumerate(s):
            if counter[c] == 0:
                k -= 1
            counter[c] += 1
            while k < 0:
                counter[s[i]] -= 1
                if counter[s[i]] == 0:
                    k += 1
                i += 1
            res += j-i+1
        return res

    def numberOfSubstrings_SLOW(self, s: str) -> int:
        idx = defaultdict(deque) # indices of 'a', 'b', and 'c'
        res, i, n = 0, 0, len(s)
        for j,c in enumerate(s):
            idx[c].append(j)
            if idx['a'] and idx['b'] and idx['c']:
                # from left
                res += min(idx['a'][-1], idx['b'][-1], idx['c'][-1])-i
                # to right
                res += n-j
                idx[s[i]].popleft()         
                i += 1   
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.numberOfSubstrings("abcabc")
