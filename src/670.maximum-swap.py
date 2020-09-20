#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (41.20%)
# Likes:    750
# Dislikes: 54
# Total Accepted:    51.2K
# Total Submissions: 122.8K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.

# Note:
# 
# The given number is in the range [0, 10^8]


# @lc code=start
class Solution:
    def maximumSwap(self, num: int) -> int:
        s = str(num)
        if len(s) == 1:
            return num

        def search(ss: str) -> str:
            if len(ss) == 1:
                return ss
            m = max(ss)
            if ss[0] == m:
                return ss[0] + search(ss[1:])
            else:
                idx = ss.rfind(m)
                return m + ss[1:idx] + ss[0] + ss[idx+1:]

        res = search(s)
        return int(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maximumSwap(9973)
