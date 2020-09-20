#
# @lc app=leetcode id=1306 lang=python3
#
# [1306] Jump Game III
#
# https://leetcode.com/problems/jump-game-iii/description/
#
# algorithms
# Medium (60.64%)
# Likes:    370
# Dislikes: 12
# Total Accepted:    23.5K
# Total Submissions: 38.9K
# Testcase Example:  '[4,2,3,0,3,1,2]\n5'
#
# Given an array of non-negative integers arr, you are initially positioned at
# start index of the array. When you are at index i, you can jump to i + arr[i]
# or i - arr[i], check if you can reach to any index with value 0.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation: 
# All possible ways to reach at index 3 with value 0 are: 
# index 5 -> index 4 -> index 1 -> index 3 
# index 5 -> index 6 -> index 4 -> index 1 -> index 3 
# 
# 
# Example 2:
# 
# 
# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true 
# Explanation: 
# One possible way to reach at index 3 with value 0 is: 
# index 0 -> index 4 -> index 1 -> index 3
# 
# 
# Example 3:
# 
# 
# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5 * 10^4
# 0 <= arr[i] < arr.length
# 0 <= start < arr.length
# 
# 
#

# @lc code=start
class Solution:
    def canReach(self, arr: [int], start: int) -> bool:
        reachable = set()
        def search(i) -> bool:
            if i< 0 or i >= len(arr) or i in reachable:
                return False
            if arr[i] == 0:
                return True
            reachable.add(i)
            if search(i-arr[i]) or search(i+arr[i]):
                return True
            return False
        res = search(start)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.canReach([0,3,0,6,3,3,4], 6)
