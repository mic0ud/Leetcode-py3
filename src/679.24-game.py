#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#
# https://leetcode.com/problems/24-game/description/
#
# algorithms
# Hard (44.27%)
# Likes:    519
# Dislikes: 111
# Total Accepted:    28.5K
# Total Submissions: 63.9K
# Testcase Example:  '[4,1,8,7]'
#
# 
# You have 4 cards each containing a number from 1 to 9.  You need to judge
# whether they could operated through *, /, +, -, (, ) to get the value of
# 24.
# 
# 
# Example 1:
# 
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
# 
# 
# 
# Example 2:
# 
# Input: [1, 2, 1, 2]
# Output: False
# 
# 
# 
# Note:
# 
# The division operator / represents real division, not integer division.  For
# example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use -
# as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression
# -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2,
# 1, 2], we cannot write this as 12 + 12.
# 
# 
# 
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: [int]) -> bool:
        if not nums:
            return False
        def dfs(subNums: [float]) -> bool:
            if len(subNums) == 1:
                 return abs(subNums[0]-24) < 1E-6

            for i in range(len(subNums)):
                for j in range(len(subNums)):
                    if i == j: continue
                    tmp = [subNums[k] for k in range(len(subNums)) if k != i and k != j]
                    # for k in range(len(subNums)):
                    #     if k != i and k != j:
                    #         tmp.append(subNums[k])
                    s1 = subNums[i] + subNums[j]
                    s2 = subNums[i] - subNums[j]
                    s3 = subNums[i] * subNums[j]
                    if dfs(tmp+[s1]): return True
                    if dfs(tmp+[s2]): return True
                    if dfs(tmp+[s3]): return True
                    if subNums[j] != 0 and dfs(tmp+[subNums[i]/subNums[j]]): return True
            return False
        return dfs(nums)

    def judgePoint24_with_path(self, nums: [int]) -> str:
        if not nums:
            return False
        def dfs(subNums: [float], path: str, res: [str]) -> bool:
            if len(subNums) == 1:
                if abs(subNums[0]-24) < 1E-6:
                     res[0] = path
                     return True
                return False

            for i in range(len(subNums)):
                for j in range(len(subNums)):
                    if i == j: continue
                    tmp = [subNums[k] for k in range(len(subNums)) if k != i and k != j]
                    # for k in range(len(subNums)):
                    #     if k != i and k != j:
                    #         tmp.append(subNums[k])
                    s1 = subNums[i] + subNums[j]
                    res1 = path + ' ' + str(subNums[i]) + ' + ' + str(subNums[j]) + ' '
                    s2 = subNums[i] - subNums[j]
                    res2 = path + ' ' + str(subNums[i]) + ' - ' + str(subNums[j]) + ' '
                    s3 = subNums[i] * subNums[j]
                    res3 = path + ' ' + str(subNums[i]) + ' * ' + str(subNums[j]) + ' '
                    if dfs(tmp+[s1], res1, res): return True
                    if dfs(tmp+[s2], res2, res): return True
                    if dfs(tmp+[s3], res3, res): return True
                    if subNums[j] != 0:
                        res4 = path + ' ' + str(subNums[i]) + ' / ' + str(subNums[j]) + ' '
                        if dfs(tmp+[subNums[i]/subNums[j]], res4, res): return True
            return False
        res = ['']
        if dfs(nums, '', res):
            return res[0]
        return 'False'
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    # print(s.judgePoint24([4, 1, 8, 7]))
    print(s.judgePoint24_with_path([7,2,6,6]))