#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/description/
#
# algorithms
# Medium (61.85%)
# Likes:    92
# Dislikes: 13
# Total Accepted:    10.1K
# Total Submissions: 16.3K
# Testcase Example:  '2\n6\n5'
#
# Given 3 positives numbers a, b and c. Return the minimum flips required in
# some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0
# to 1 in their binary representation.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)
# 
# Example 2:
# 
# 
# Input: a = 4, b = 2, c = 7
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: a = 1, b = 2, c = 3
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= a <= 10^9
# 1 <= b <= 10^9
# 1 <= c <= 10^9
# 
#

# @lc code=start
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        # if (a | b) ^ c is 0, a | b and c are equal, otherwise not equal and we need to check them bit by bit;
        # For ith bit of (a | b) ^ c, use 1 << i as mask to do & operation to check if the bit is 0; if not, ith bits of a | b and c are not same and we need at least 1 flip; there are 3 cases:
        # i) the ith bit of a | b less than that of c; then ith bit of a | b must be 0, we only need to flip the ith bit of either a or b;
        # ii) the ith bit of a | b bigger than that of c; then ith bit of a | b must be 1, but if only one of a or b's ith bit is 1, we only need to flip one of them;
        # iii) Other case, we need to flip both set bit of a and b, hence need 2 flips.
        # In short, if ith bits of a | b and c are not same, then only if ith bits of a and b are both 1 and that of c is 0, we need 2 flips; otherwise only 1 flip needed.
        equal, res = (a | b) ^ c, 0
        for i in range(32):
            mask = 1 << i
            if (equal & mask) > 0:
                res += 2 if (a & mask) == (b & mask) and (c & mask) == 0 else 1
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minFlips(2,6,5)
