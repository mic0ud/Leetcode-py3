#
# @lc app=leetcode id=1291 lang=python3
#
# [1291] Sequential Digits
#
# https://leetcode.com/problems/sequential-digits/description/
#
# algorithms
# Medium (52.29%)
# Likes:    154
# Dislikes: 18
# Total Accepted:    10.2K
# Total Submissions: 19.3K
# Testcase Example:  '100\n300'
#
# An integer has sequential digits if and only if each digit in the number is
# one more than the previous digit.
# 
# Return a sorted list of all the integers in the range [low, high] inclusive
# that have sequential digits.
# 
# 
# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]
# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
# 
# 
# Constraints:
# 
# 
# 10 <= low <= high <= 10^9
# 
# 
#

# @lc code=start
from bisect import bisect_left, bisect_right
class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        m, n, total = 2, 10, []
        for i in range(m, n):
            for j in range(1, 11-i):
                total.append(int(''.join([str(j+k) for k in range(i)])))
        left = bisect_left(total, low)
        right = bisect_right(total, high)
        res = total[left:right]
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.sequentialDigits(10,10**9)
    s.sequentialDigits(100,300)
    s.sequentialDigits(1000,13000)
