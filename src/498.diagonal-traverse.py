#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (46.27%)
# Likes:    562
# Dislikes: 280
# Total Accepted:    65.1K
# Total Submissions: 139.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.

# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:

# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.

# @lc code=start
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, matrix: [[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []
        M, N = len(matrix), len(matrix[0])
        dd = defaultdict(list)
        for i in range(M):
            for j in range(N):
                dd[i+j+1].append(matrix[i][j])
        res = []
        for k in sorted(dd.keys()):
            res += dd[k] if k%2 == 0 else dd[k][::-1]
        return res

    def findDiagonalOrder_SLOW(self, matrix: [[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []
        M, N = len(matrix), len(matrix[0])
        if M == 1:
            return matrix[0]
        if N == 1:
            return [matrix[i][0] for i in range(M)]
        down = False
        i, j, res = 0, 0, []
        while i < M-1 or j < N-1:
            if down:
                while j >= 0:
                    if 0 <= i < M and 0 <= j < N:
                        res.append(matrix[i][j])		
                    i += 1
                    j -= 1
                j += 1
                if i >= M:
                    j += i-(M-1)
                    i = M-1
            else:
                while i >= 0:
                    if 0 <= i < M and 0 <= j < N:
                        res.append(matrix[i][j])
                    i -= 1
                    j += 1
                i += 1
                if j >= N:
                    i += j-(N-1)
                    j = N-1
            down = not down
        res.append(matrix[M-1][N-1])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.findDiagonalOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
