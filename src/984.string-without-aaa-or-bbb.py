#
# @lc app=leetcode id=984 lang=python3
#
# [984] String Without AAA or BBB
#
# https://leetcode.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (35.03%)
# Likes:    133
# Dislikes: 200
# Total Accepted:    13.5K
# Total Submissions: 38K
# Testcase Example:  '1\n2'
#
# Given two integers A and B, return any string S such that:
# 
# 
# S has length A + B and contains exactly A 'a' letters, and exactly B 'b'
# letters;
# The substring 'aaa' does not occur in S;
# The substring 'bbb' does not occur in S.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = 1, B = 2
# Output: "abb"
# Explanation: "abb", "bab" and "bba" are all correct answers.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = 4, B = 1
# Output: "aabaa"
# 
# A <= 2*B + 2
# aabaabaabaa
# 
# Note:
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# It is guaranteed such an S exists for the given A and B.
# 
# 
#

# @lc code=start
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A <= 0 and B <= 0:
            return ''
        if A == B:
            return 'ab' * A
        big = max(A,B)
        small = min(A,B)
        bigChar = 'a' if A > B else 'b'
        smallChar = 'a' if A < B else 'b'
        res = (bigChar + bigChar + smallChar)*small
        todo = big - 2*small
        i = 0
        while todo != 0:
            if todo > 0:
                res += bigChar
                todo -= 1
            else:
                res = res[:i] + res[i+1:]
                i += 2
                todo += 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.strWithout3a3b(1,2)