#
# @lc app=leetcode id=1079 lang=python3
#
# [1079] Letter Tile Possibilities
#
# https://leetcode.com/problems/letter-tile-possibilities/description/
#
# algorithms
# Medium (74.40%)
# Likes:    351
# Dislikes: 15
# Total Accepted:    17.3K
# Total Submissions: 23.2K
# Testcase Example:  '"AAB"'
#
# You have a set of tiles, where each tile has one letter tiles[i] printed on
# it.  Return the number of possible non-empty sequences of letters you can
# make.
# 
# 
# 
# Example 1:
# 
# 
# Input: "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
# "ABA", "BAA".
# 
# 
# 
# Example 2:
# 
# 
# Input: "AAABBC"
# Output: 188
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        n = len(tiles)
        if n <= 1:
            return n
        count = defaultdict(int)
        for c in tiles:
            count[c] += 1
        res = set()
        level = 0
        self.nextPermute(n, count, level, '', res)
        return len(res)-1 # exclude the ''
        
    def nextPermute(self, n: int, count: {str:int}, level: int, curr: str, res):
        res.add(curr)
        if level >= n:
            return        
        for c in count:
            if count[c] > 0:
                count[c] -= 1
                self.nextPermute(n, count, level+1, curr+c, res)
                count[c] += 1    
# @lc code=end

