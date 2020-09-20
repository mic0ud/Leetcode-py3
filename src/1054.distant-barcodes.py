#
# @lc app=leetcode id=1054 lang=python3
#
# [1054] Distant Barcodes
#
# https://leetcode.com/problems/distant-barcodes/description/
#
# algorithms
# Medium (40.16%)
# Likes:    198
# Dislikes: 14
# Total Accepted:    10.3K
# Total Submissions: 25.3K
# Testcase Example:  '[1,1,1,2,2,2]'
#
# In a warehouse, there is a row of barcodes, where the i-th barcode is
# barcodes[i].
# 
# Rearrange the barcodes so that no two adjacent barcodes are equal.  You may
# return any answer, and it is guaranteed an answer exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,2,2,2]
# Output: [2,1,2,1,2,1]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,1,2,2,3,3]
# Output: [1,3,1,3,2,1,2,1]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= barcodes.length <= 10000
# 1 <= barcodes[i] <= 10000
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter
class Solution:
    def rearrangeBarcodes(self, barcodes: [int]) -> [int]:
        if not barcodes:
            return []
        i, n = 0, len(barcodes)
        res = ['' for _ in range(n)]
        for k, v in Counter(barcodes).most_common():
            for _ in range(v): # insert v times
                res[i] = k
                i += 2
                if i >= n:
                    i = 1 # it is guaranteed an answer exists, so at most 2 passes if insert very 2 postions
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.rearrangeBarcodes([1,1,1,1,2,2,3,3])
