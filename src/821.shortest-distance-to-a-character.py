#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (64.73%)
# Likes:    815
# Dislikes: 67
# Total Accepted:    52.7K
# Total Submissions: 80.6K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#

# @lc code=start
class Solution:
    def shortestToChar(self, S: str, C: str) -> [int]:
        i, j, n = 0, 0, len(S)
        res = [float('inf') for _ in range(n)]
        while j < n:
            while j < n and S[j] != C:
                j += 1
            if j >= n:
                break
            res[j] = 0
            if i == 0 and S[i] != C:
                for k in range(j):
                    res[k] = j-k
            else:
                for k in range(i+1,j):
                    res[k] = min(k-i,j-k)
            i = j
            j += 1
        for k in range(i+1, n):
            res[k] = k-i
        return res    
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.shortestToChar("loveleetcode", 'e')
    # s.shortestToChar("baab", 'b')
