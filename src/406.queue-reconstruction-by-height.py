#
# @lc app=leetcode id=406 lang=python3
#
# [406] Queue Reconstruction by Height
#
# https://leetcode.com/problems/queue-reconstruction-by-height/description/
#
# algorithms
# Medium (61.63%)
# Likes:    2028
# Dislikes: 237
# Total Accepted:    100.7K
# Total Submissions: 162.1K
# Testcase Example:  '[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]'
#
# Suppose you have a random list of people standing in a queue. Each person is
# described by a pair of integers (h, k), where h is the height of the person
# and k is the number of people in front of this person who have a height
# greater than or equal to h. Write an algorithm to reconstruct the queue.
# 
# Note:
# The number of people is less than 1,100.
# 
# 
# Example
# 
# 
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
# 
# 
# 
# 
#

# @lc code=start
from operator import itemgetter
class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        if not people or not people[0]:
            return []
        people.sort(key=lambda x: (-x[0], x[1]))
        res = []
        for p in people:
            res.insert(p[1], p)           
        return res        
# @lc code=end
# [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
# [[4,0],[5,0],[6,0],[2,2],[1,4],[3,2]]
# [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

# [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
# [[5,0],[6,1],[5,2],[7,0],[4,4],[7,1]]
# [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
if __name__ == '__main__':
    s = Solution()
    s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])