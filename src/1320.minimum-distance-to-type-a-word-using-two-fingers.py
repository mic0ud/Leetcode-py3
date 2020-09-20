#
# @lc app=leetcode id=1320 lang=python3
#
# [1320] Minimum Distance to Type a Word Using Two Fingers
#
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/description/
#
# algorithms
# Hard (59.72%)
# Likes:    326
# Dislikes: 14
# Total Accepted:    10.8K
# Total Submissions: 17.7K
# Testcase Example:  '"CAKE"'
#
# 
# 
# You have a keyboard layout as shown above in the XY plane, where each English
# uppercase letter is located at some coordinate, for example, the letter A is
# located at coordinate (0,0), the letter B is located at coordinate (0,1), the
# letter P is located at coordinate (2,3) and the letter Z is located at
# coordinate (4,1).
# 
# Given the string word, return the minimum total distance to type such string
# using only two fingers. The distance between coordinates (x1,y1) and (x2,y2)
# is |x1 - x2| + |y1 - y2|. 
# 
# Note that the initial positions of your two fingers are considered free so
# don't count towards your total distance, also your two fingers do not have to
# start at the first letter or the first two letters.
# 
# 
# Example 1:
# 
# 
# Input: word = "CAKE"
# Output: 3
# Explanation: 
# Using two fingers, one optimal way to type "CAKE" is: 
# Finger 1 on letter 'C' -> cost = 0 
# Finger 1 on letter 'A' -> cost = Distance from letter 'C' to letter 'A' = 2 
# Finger 2 on letter 'K' -> cost = 0 
# Finger 2 on letter 'E' -> cost = Distance from letter 'K' to letter 'E' = 1 
# Total distance = 3
# 
# 
# Example 2:
# 
# 
# Input: word = "HAPPY"
# Output: 6
# Explanation: 
# Using two fingers, one optimal way to type "HAPPY" is:
# Finger 1 on letter 'H' -> cost = 0
# Finger 1 on letter 'A' -> cost = Distance from letter 'H' to letter 'A' = 2
# Finger 2 on letter 'P' -> cost = 0
# Finger 2 on letter 'P' -> cost = Distance from letter 'P' to letter 'P' = 0
# Finger 1 on letter 'Y' -> cost = Distance from letter 'A' to letter 'Y' = 4
# Total distance = 6
# 
# 
# Example 3:
# 
# 
# Input: word = "NEW"
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: word = "YEAR"
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# 2 <= word.length <= 300
# Each word[i] is an English uppercase letter.
# 
#

# @lc code=start
class Solution:
    def minimumDistance_(self, A):
        def d(a, b):
            return a and abs(a / 6 - b / 6) + abs(a % 6 - b % 6)

        dp, dp2 = {(0, 0): 0}, {}
        for c in (ord(c) + 1 for c in A):
            for a, b in dp:
                dp2[c, b] = min(dp2.get((c, b), 3000), dp[a, b] + d(a, c))
                dp2[a, c] = min(dp2.get((a, c), 3000), dp[a, b] + d(b, c))
            dp, dp2 = dp2, {}
        return min(dp.values())

    def minimumDistance(self, word: str) -> int:
        chars = {}
        i = j = 0
        for c in range(65, 91):
            chars[chr(c)] = [i, j]
            j += 1
            if j >= 6:
                i += 1
                j = 0
        def distance(a,b) -> int:
            if a == 0 or b == 0:
                return 0
            return abs(chars[chr(a)][0]-chars[chr(b)][0]) + abs(chars[chr(a)][1]-chars[chr(b)][1])
        # Initial the position of two fingers as (0,0).
        # Iterate the input sttring and track the position of two fingers after tap the last character.
        # dp[a,b] means with one finger at a and the other at postion b,
        # the minimum distance we need is dp[a, b].
        # d(a, b) return the distance moving from a to b. Also if a = 0 we return 0.
        dp, dp2 = {(0, 0): 0}, {}
        for c in word:
            for a, b in dp:
                dp2[(a,ord(c))] = min(dp2.get((a, ord(c)), float('inf')), dp[(a, b)] + distance(a, ord(c)))
                dp2[(ord(c),b)] = min(dp2.get((ord(c), b), float('inf')), dp[(a, b)] + distance(ord(c), b))
            dp, dp2 = dp2, {}
        return min(dp.values())
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.minimumDistance("YEAR")
