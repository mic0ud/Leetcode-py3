#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (51.52%)
# Likes:    162
# Dislikes: 76
# Total Accepted:    11.8K
# Total Submissions: 22.9K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
# 
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: 24
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: 46
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = Counter(str(N))
        return any(c == Counter(str(1<<i)) for i in range(30))

    def reorderedPowerOf2_SLOW(self, N: int) -> bool:
        if N < 1:
            return False
        if N & N - 1 == 0:
            return True           
        nstr = str(N)
        countMap = defaultdict(int)
        for c in nstr:
            countMap[c] += 1

        def dfs(count: {}, i: int, ns: str) -> bool:
            if len(ns) >= len(nstr):
                return ns[0] != '0' and int(ns) & int(ns) - 1 == 0
            for c in count:
                if count[c] > 0:
                    count[c] -= 1
                    if dfs(count, i+1, ns+c):
                        return True
                    count[c] += 1
            return False

        return dfs(countMap, 0, '')
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    print(s.reorderedPowerOf2(4120))
