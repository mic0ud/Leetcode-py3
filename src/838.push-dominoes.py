#
# @lc app=leetcode id=838 lang=python3
#
# [838] Push Dominoes
#
# https://leetcode.com/problems/push-dominoes/description/
#
# algorithms
# Medium (45.82%)
# Likes:    415
# Dislikes: 47
# Total Accepted:    16.8K
# Total Submissions: 36.2K
# Testcase Example:  '".L.R...LR..L.."'
#
# There are N dominoes in a line, and we place each domino vertically upright.
# 
# In the beginning, we simultaneously push some of the dominoes either to the
# left or to the right.
# 
# 
# 
# After each second, each domino that is falling to the left pushes the
# adjacent domino on the left.
# 
# Similarly, the dominoes falling to the right push their adjacent dominoes
# standing on the right.
# 
# When a vertical domino has dominoes falling on it from both sides, it stays
# still due to the balance of the forces.
# 
# For the purposes of this question, we will consider that a falling domino
# expends no additional force to a falling or already fallen domino.
# 
# Given a string "S" representing the initial state. S[i] = 'L', if the i-th
# domino has been pushed to the left; S[i] = 'R', if the i-th domino has been
# pushed to the right; S[i] = '.', if the i-th domino has not been pushed.
# 
# Return a string representing the final state. 
# 
# Example 1:
# 
# 
# Input: ".L.R...LR..L.."
# Output: "LL.RR.LLRRLL.."
#         'LL.RR.LLRRLL..'
# 
# Example 2:
# 
# 
# Input: "RR.L"
# Output: "RR.L"
# Explanation: The first domino expends no additional force on the second
# domino.
# 
# 
# Note:
# 
# 
# 0 <= N <= 10^5
# String dominoes contains only 'L', 'R' and '.'


# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        res = ['.' for _ in range(len(dominoes))]
        i, j, n = 0, 0, len(dominoes)
        while j < n:
            while j < n and dominoes[j] == '.':
                j += 1
            if j >= n:
                break
            res[j] = dominoes[j]
            if dominoes[i] == '.':
                if i == 0 and dominoes[j] == 'L':
                    for k in range(i,j):
                        res[k] = 'L'
            elif dominoes[i] == 'L':
                if dominoes[j] == 'L':
                    for k in range(i,j):
                        res[k] = 'L'
            else: # dominoes[i] == 'R'
                if dominoes[j] == 'R':
                    for k in range(i+1,j):
                        res[k] = 'R'
                elif dominoes[j] == 'L':
                    k1, k2 = i, j
                    while k1+1 < k2-1:
                        res[k1+1] = 'R'
                        res[k2-1] = 'L'
                        k1 += 1
                        k2 -= 1
            i = j
            j += 1
        if dominoes[i] == 'R':
            for k in range(i,n):
                res[k] = 'R'
        return ''.join(res)
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.pushDominoes("..R..")
    # s.pushDominoes("RR.L")
    # s.pushDominoes(".L.R...LR..L..")
    s.pushDominoes("LR")
