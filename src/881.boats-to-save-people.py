#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#
# https://leetcode.com/problems/boats-to-save-people/description/
#
# algorithms
# Medium (44.92%)
# Likes:    369
# Dislikes: 26
# Total Accepted:    22.2K
# Total Submissions: 49K
# Testcase Example:  '[1,2]\n3'
#
# The i-th person has weight people[i], and each boat can carry a maximum
# weight of limit.
# 
# Each boat carries at most 2 people at the same time, provided the sum of the
# weight of those people is at most limit.
# 
# Return the minimum number of boats to carry every given person.  (It is
# guaranteed each person can be carried by a boat.)
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# 
# 
# 
# Example 2:
# 
# 
# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# 
# 
# 
# Example 3:
# 
# 
# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# 
# Note:
# 
# 
# 1 <= people.length <= 50000
# 1 <= people[i] <= limit <= 30000
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def numRescueBoats(self, people: [int], limit: int) -> int:
        if not people:
            return 0
        people.sort(reverse=True)
        left, right = 0, len(people)-1
        count = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            left += 1
            count += 1
        return count
# @lc code=end
# [5,1,4,2]\n6
# [3,2,3,2,2]\n6
