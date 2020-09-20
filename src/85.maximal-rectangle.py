#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (35.13%)
# Likes:    2044
# Dislikes: 56
# Total Accepted:    149.4K
# Total Submissions: 419.5K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
# 
# 
#

# @lc code=start
class Solution:
    def maximalRectangle(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        row = list(matrix[0])
        res = self.getArea(row)
        for i in range(1, m):
            for j in range(n):
                row[j] = '0' if matrix[i][j] == '0' else str(int(row[j])+int(matrix[i][j]))
            res = max(res, self.getArea(row))
        return res

    def getArea(self, row: [int]) -> int:
        if not row:
            return 0
        stack = []
        res = 0
        for i in range(len(row)):
            if not stack or int(row[i]) > int(row[stack[-1]]):
                stack.append(i)
            else:
                while stack and int(row[i]) <= int(row[stack[-1]]):
                    height = int(row[stack.pop()])
                    tmp = height*i if not stack else height * (i - stack[-1] - 1)
                    res = max(res, tmp)
                stack.append(i)
        while stack:
            height = int(row[stack.pop()])
            tmp = height*len(row) if not stack else height * (len(row) - stack[-1] - 1)
            res = max(res, tmp)
        return res


    def maximalRectangle_SLOW(self, matrix: [[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        row, start= 0, 0
        j = 0
        tmp = 0
        while row < m:
            while j < n:
                while j < n and matrix[row][j] == '0':
                    j += 1
                start = j
                while j < n and matrix[row][j] == '1':
                    j += 1
                tmp = j - start
                for w in range(1, tmp+1):
                    rowCount, i = 1, 1
                    while row+i < m and '0' not in matrix[row+i][start:start+w]:
                        rowCount += 1
                        i += 1
                    i = 1
                    while row-i >= 0 and '0' not in matrix[row-i][start:start+w]:
                        rowCount += 1
                        i += 1
                    res = max(res, w*rowCount)
            j, start, tmp = 0, 0, 0
            row += 1
        return res
# @lc code=end
# ["0","1","1","0","0","1","0","1","0","1"],
# ["0","0","1","0","1","0","1","0","1","0"],
# ["1","0","0","0","0","1","0","1","1","0"],
# ["0","1","1","1","1","1","1","0","1","0"],
# ["0","0","1","1","1","1","1","1","1","0"],
# ["1","1","0","1","0","1","1","1","1","0"],
# ["0","0","0","1","1","0","0","0","1","0"],
# ["1","1","0","1","1","0","0","1","1","1"],
# ["0","1","0","1","1","0","1","0","1","1"]]
# [["1","1"]]
if __name__ == '__main__':
    s = Solution()
    s.maximalRectangle([["1","1"]])
    # s.maximalRectangle([["0","1","1","0","0","1","0","1","0","1"],["0","0","1","0","1","0","1","0","1","0"],["1","0","0","0","0","1","0","1","1","0"],["0","1","1","1","1","1","1","0","1","0"],["0","0","1","1","1","1","1","1","1","0"],["1","1","0","1","0","1","1","1","1","0"],["0","0","0","1","1","0","0","0","1","0"],["1","1","0","1","1","0","0","1","1","1"],["0","1","0","1","1","0","1","0","1","1"]])
