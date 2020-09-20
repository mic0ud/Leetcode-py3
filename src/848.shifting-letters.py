#
# @lc app=leetcode id=848 lang=python3
#
# [848] Shifting Letters
#
# https://leetcode.com/problems/shifting-letters/description/
#
# algorithms
# Medium (42.59%)
# Likes:    215
# Dislikes: 45
# Total Accepted:    18.8K
# Total Submissions: 43.4K
# Testcase Example:  '"abc"\n[3,5,9]'
#
# We have a string S of lowercase letters, and an integer array shifts.
# 
# Call the shift of a letter, the next letter in the alphabet, (wrapping around
# so that 'z' becomes 'a'). 
# 
# For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
# 
# Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x
# times.
# 
# Return the final string after all such shifts to S are applied.
# 
# Example 1:
# 
# 
# Input: S = "abc", shifts = [3,5,9]
# Output: "rpl"
# Explanation: 
# We start with "abc".
# After shifting the first 1 letters of S by 3, we have "dbc".
# After shifting the first 2 letters of S by 5, we have "igc".
# After shifting the first 3 letters of S by 9, we have "rpl", the answer.
# 
# 
# Note:
# 
# 
# 1 <= S.length = shifts.length <= 20000
# 0 <= shifts[i] <= 10 ^ 9
# 
# 
#

# @lc code=start
class Solution:
    def shiftingLetters(self, S: str, shifts: [int]) -> str:
        n = len(S)
        reversedPrefixSum = []
        tmp = 0
        for a in shifts[::-1]:
            tmp += a
            reversedPrefixSum.append(tmp)
        res = ''
        for i in range(n):
            asci = ord(S[i])+reversedPrefixSum[n-1-i]%26
            res += chr(asci if asci <= ord('z') else ord('a')-1+asci - ord('z'))
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.shiftingLetters("ruu", [26,9,17])
