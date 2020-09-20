#
# @lc app=leetcode id=1147 lang=python3
#
# [1147] Longest Chunked Palindrome Decomposition
#
# https://leetcode.com/problems/longest-chunked-palindrome-decomposition/description/
#
# algorithms
# Hard (58.03%)
# Likes:    133
# Dislikes: 11
# Total Accepted:    7.6K
# Total Submissions: 13K
# Testcase Example:  '"ghiabcdefhelloadamhelloabcdefghi"'
#
# Return the largest possible k such that there exists a_1, a_2, ..., a_k such
# that:
# 
# 
# Each a_i is a non-empty string;
# Their concatenation a_1 + a_2 + ... + a_k is equal to text;
# For all 1 <= i <= k,  a_i = a_{k+1 - i}.

# Example 1:

# Input: text = "ghiabcdefhelloadamhelloabcdefghi"
# Output: 7
# Explanation: We can split the string on
# "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)".

# Example 2:

# Input: text = "merchant"
# Output: 1
# Explanation: We can split the string on "(merchant)".

# Example 3:

# Input: text = "antaprezatepzapreanta"
# Output: 11
# Explanation: We can split the string on
# "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)".

# Example 4:

# Input: text = "aaa"
# Output: 3
# Explanation: We can split the string on "(a)(a)(a)".

# Constraints:

# text consists only of lowercase English characters.
# 1 <= text.length <= 1000


# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        def search(t) -> int:
            if len(t) < 2:
                return 1 if len(t) > 0 else 0
            l,r = 0, len(t)-1
            while l < r and t[:l+1] != t[r:]:
                l += 1
                r -= 1
            if l >= r:
                return 1
            else:
                return 2 + search(t[l+1:r]) 
        res = search(text)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestDecomposition("elvtoelvto")
    s.longestDecomposition("merchant")
    s.longestDecomposition("aaa")
    s.longestDecomposition("antaprezatepzapreanta")
    s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi")
