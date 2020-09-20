#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (56.02%)
# Likes:    561
# Dislikes: 135
# Total Accepted:    45.4K
# Total Submissions: 80.2K
# Testcase Example:  '2'
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 <= i <= N) in this array:
# 
# 
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.

# Now given N, how many beautiful arrangements can you construct?
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: 
# 
# The first beautiful arrangement is [1, 2]:
# 
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# 
# The second beautiful arrangement is [2, 1]:
# 
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

# Note:
# 
# 
# N is a positive integer and will not exceed 15.


# @lc code=start
class Solution:
    def countArrangement(self, N: int) -> int:
        if N < 3:
            return N
        taken = [False for _ in range(N)]
        def dfs(i, res:[]):
            if i == 1:
                res[0] += 1
                return
            for j, t in enumerate(taken):
                if not t and ((j+1)%i == 0 or i%(j+1) == 0):
                    taken[j] = True
                    dfs(i-1, res)
                    taken[j] = False
        res = [0]
        dfs(N, res)
        return res[0]        


    def countArrangement_SLOW(self, N: int) -> int:
        if N < 3:
            return N
        taken = [False for _ in range(N)]
        def dfs(i, path:[], res:[]):
            if i > N:
                res[0] += 1
                return
            for j, t in enumerate(taken):
                if not t and ((j+1)%i == 0 or i%(j+1) == 0):
                    path.append(j+1)
                    taken[j] = True
                    dfs(i+1, list(path), res)
                    taken[j] = False
        res = [0]
        dfs(1, [], res)
        return res[0]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countArrangement(14)
