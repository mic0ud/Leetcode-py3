#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#
# https://leetcode.com/problems/shuffle-an-array/description/
#
# algorithms
# Medium (51.25%)
# Likes:    417
# Dislikes: 884
# Total Accepted:    107.5K
# Total Submissions: 207.1K
# Testcase Example:  '["Solution","shuffle","reset","shuffle"]\n[[[1,2,3]],[],[],[]]'
#
# Shuffle a set of numbers without duplicates.

# Example:
# 
# // Init an array with set 1, 2, and 3.
# int[] nums = {1,2,3};
# Solution solution = new Solution(nums);
# 
# // Shuffle the array [1,2,3] and return its result. Any permutation of
# [1,2,3] must equally likely to be returned.
# solution.shuffle();
# 
# // Resets the array back to its original configuration [1,2,3].
# solution.reset();
# 
# // Returns the random shuffling of array [1,2,3].
# solution.shuffle();

# @lc code=start
from random import randint
class Solution:

    def __init__(self, nums: [int]):
        self.o = list(nums)

    def reset(self) -> [int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.o)

    def shuffle(self) -> [int]:
        """
        Returns a random shuffling of the array.
        """
        res = []
        self.generateIndex(0, len(self.o)-1, res)
        return [self.o[i] for i in res]

    def generateIndex(self, i, j, res:[]):
        if i > j:
            return
        if i == j:
            res.append(i)
            return
        idx = randint(i,j)
        res.append(idx)
        self.generateIndex(i,idx-1,res)
        self.generateIndex(idx+1,j,res)

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end
if __name__ == '__main__':
    s = Solution([1,2,3,4])
    s.shuffle()
