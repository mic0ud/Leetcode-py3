#
# @lc app=leetcode id=386 lang=python3
#
# [386] Lexicographical Numbers
#
# https://leetcode.com/problems/lexicographical-numbers/description/
#
# algorithms
# Medium (48.51%)
# Likes:    497
# Dislikes: 66
# Total Accepted:    49.1K
# Total Submissions: 99.1K
# Testcase Example:  '13'
#
# Given an integer n, return 1 - n in lexicographical order.
# 
# For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
# 
# Please optimize your algorithm to use less time and space. The input size may
# be as large as 5,000,000.
# 
#

# @lc code=start
from functools import cmp_to_key
class Solution:
    def lexicalOrder(self, n: int) -> [int]:
        # 42      =>  42000000000042
        # 4200    =>  42000000004200
        # 123456  =>  12345600123456
        keys, p = [], len(str(n))
        for i in range(1, n+1):
            keys.append(i*(10**p)*(10**(p-len(str(i))))+i)
        res = [i%(10**p) for i in sorted(keys)]
        return res

    def lexicalOrder_2(self, n: int) -> [int]:
        top = 10**len(str(n))
        def my_cmp(n1,n2,top=top) -> int:
            while n1 < top: n1 *= 10
            while n2 < top: n2 *= 10
            return -1 if n1 < n2 else n1 > n2
        res = [i for i in range(1, n+1)]
        return sorted(res, key=cmp_to_key(my_cmp))
# @lc code=end

