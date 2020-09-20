#
# @lc app=leetcode id=1405 lang=python3
#
# [1405] Longest Happy String
#
# https://leetcode.com/problems/longest-happy-string/description/
#
# algorithms
# Medium (45.91%)
# Likes:    196
# Dislikes: 58
# Total Accepted:    7.9K
# Total Submissions: 16.9K
# Testcase Example:  '1\n1\n7'
#
# A string is called happy if it does not have any of the strings 'aaa', 'bbb'
# or 'ccc' as a substring.
# 
# Given three integers a, b and c, return any string s, which satisfies
# following conditions:
# 
# 
# s is happy and longest possible.
# s contains at most a occurrences of the letter 'a', at most b occurrences of
# the letter 'b' and at most c occurrences of the letter 'c'.
# s will only contain 'a', 'b' and 'c' letters.
# 
# 
# If there is no such string s return the empty string "".
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# 
# 
# Example 2:
# 
# 
# Input: a = 2, b = 2, c = 1
# Output: "aabbc"
# 
# 
# Example 3:
# 
# 
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It's the only correct answer in this case.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= a, b, c <= 100
# a + b + c > 0
# 
# 
#

# @lc code=start
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        count, res = [], ''
        if a > 0:
            heapq.heappush(count, [-a,'a'])
        if b > 0:
            heapq.heappush(count, [-b,'b'])
        if c > 0:
            heapq.heappush(count, [-c,'c'])
        while len(count) > 1:
            max1 = heapq.heappop(count)
            if not res or res[-1] != max1[-1]:
                res += max1[-1]*(2 if -max1[0] >= 2 else 1)
                max1[0] += 2
                if max1[0] < 0:
                    heapq.heappush(count, [max1[0], max1[-1]])
            else:
                max2 = heapq.heappop(count)
                res += max2[-1]
                max2[0] += 1
                if max2[0] < 0:
                    heapq.heappush(count, [max2[0], max2[-1]])    
                heapq.heappush(count, max1)     
        if count and (not res or res[-1] != count[0][-1]):
            res += count[0][-1]*(2 if -count[0][0] >= 2 else 1)     
        return res 
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.longestDiverseString(0,8,11)
    s.longestDiverseString(2,2,1)
    s.longestDiverseString(7,1,0)
    s.longestDiverseString(1,1,7)
