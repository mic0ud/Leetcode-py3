#
# @lc app=leetcode id=477 lang=python3
#
# [477] Total Hamming Distance
#
# https://leetcode.com/problems/total-hamming-distance/description/
#
# algorithms
# Medium (49.96%)
# Likes:    682
# Dislikes: 48
# Total Accepted:    57.2K
# Total Submissions: 113.9K
# Testcase Example:  '[4,14,2]'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Now your job is to find the total Hamming distance between all pairs of the
# given numbers.
# 
# 
# Example:
# 
# Input: 4, 14, 2
# 
# Output: 6
# 
# Explanation: In binary representation, the 4 is 0100, 14 is 1110, and 2 is
# 0010 (just
# showing the four bits relevant in this case). So the answer will be:
# HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 +
# 2 + 2 = 6.
# 
# 
# 
# Note:
# 
# Elements of the given array are in the range of 0  to 10^9
# Length of the array will not exceed 10^4. 

# @lc code=start
from collections import Counter
class Solution:
    def totalHammingDistance(self, nums: [int]) -> int:
        barray = [bin(n)[2:][::-1] for n in nums]
        res = 0
        for i in range(max([len(b) for b in barray], default=0)):
            c = Counter([ba[i] if i < len(ba) else '0' for ba in barray])
            res += c['0'] * c['1']
        return res 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.totalHammingDistance([4,14,2])
