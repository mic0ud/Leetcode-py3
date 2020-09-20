#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (47.17%)
# Likes:    2162
# Dislikes: 116
# Total Accepted:    149.6K
# Total Submissions: 316.1K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
# 
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
# 
# Examples:
# 
# 
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                tmp = stack.pop()
                while stack and stack[-1] != '[' :
                    tmp = stack.pop() + tmp
                stack.pop()
                count = stack.pop()
                while stack and self.isInt(stack[-1]):
                    count = stack.pop() + count
                tmp = tmp * int(count)
                stack.append(tmp)
        return ''.join(stack)
    
    def isInt(self, s: str) -> bool:
        try:
            int(s)
            return True
        except:
            return False
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.decodeString("100[leetcode]")
