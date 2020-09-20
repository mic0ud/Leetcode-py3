#
# @lc app=leetcode id=1349 lang=python3
#
# [1349] Maximum Students Taking Exam
#
# https://leetcode.com/problems/maximum-students-taking-exam/description/
#
# algorithms
# Hard (39.46%)
# Likes:    256
# Dislikes: 8
# Total Accepted:    4.8K
# Total Submissions: 12K
# Testcase Example:  '[["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]]'
#
# Given a m * n matrix seats  that represent seats distributions in a
# classroom. If a seat is broken, it is denoted by '#' character otherwise it
# is denoted by a '.' character.
# 
# Students can see the answers of those sitting next to the left, right, upper
# left and upper right, but he cannot see the answers of the student sitting
# directly in front or behind him. Return the maximum number of students that
# can take the exam together without any cheating being possible..
# 
# Students must be placed in seats in good condition.
# 
# 
# Example 1:
# 
# 
# Input: seats = [["#",".","#","#",".","#"],
# [".","#","#","#","#","."],
# ["#",".","#","#",".","#"]]
# Output: 4
# Explanation: Teacher can place 4 students in available seats so they don't
# cheat on the exam. 
# 
# 
# Example 2:
# 
# 
# Input: seats = [[".","#"],
# ["#","#"],
# ["#","."],
# ["#","#"],
# [".","#"]]
# Output: 3
# Explanation: Place all students in available seats. 
# 
# 
# 
# Example 3:
# 
# 
# Input: seats = [["#",".",".",".","#"],
# [".","#",".","#","."],
# [".",".","#",".","."],
# [".","#",".","#","."],
# ["#",".",".",".","#"]]
# Output: 10
# Explanation: Place students in available seats in column 1, 3 and 5.
# 
# 
# 
# Constraints:
# 
# 
# seats contains only characters '.' and'#'.
# m == seats.length
# n == seats[i].length
# 1 <= m <= 8
# 1 <= n <= 8


# @lc code=start
class Solution:
    def maxStudents(self, seats: [[str]]) -> int:
# We can use (x >> i) & 1 to get i-th bit in state x, where >> is the right shift operation. If we are doing this in an if statement (i.e. to check whether the i-th bit is 1), we can also use x & (1 << i), where the << is the left shift operation.
# We can use (x & y) == x to check if x is a subset of y. The subset means every state in x could be 1 only if the corresponding state in y is 1.
# We can use (x & (x >> 1)) == 0 to check if there are no adjancent valid states in x.
        m, n, res = len(seats), len(seats[0]), 0

            
        

    def maxStudents_TLE(self, seats: [[str]]) -> int:
        m, n, res = len(seats), len(seats[0]), [0]
        # using '+' as tag that the seat is taken
        def is_taken(i,j) -> bool:
            if 0 <= i < m and 0 <= j < n:
                return seats[i][j] == '+'
            return False
        def check(i,j) -> bool:
            return not is_taken(i-1,j-1) and not is_taken(i-1,j+1) and not is_taken(i,j-1) and not is_taken(i,j+1)
        def search(i,j,count):
            if i >= m or j >= n:
                res[0] = max(res[0], count)
                return
            if seats[i][j] == '.' and check(i,j):
                seats[i][j] = '+'
                search(i,j+2,count+1) if j+2 < n else search(i+1,0,count+1)
                seats[i][j] = '.'
            search(i,j+1,count) if j+1 < n else search(i+1,0,count)
        search(0,0,0)
        return res[0]
# @lc code=end
# [".",".",".",".","#",".",".","."],
# [".",".",".",".",".",".",".","."]
if __name__ == '__main__':
    s = Solution()
    s.maxStudents([[".",".",".",".","#",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".","#","."],[".",".",".",".",".",".",".","."],[".",".","#",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","#",".",".","#","."]])
    s.maxStudents([["#",".",".",".","#"],[".","#",".","#","."],[".",".","#",".","."],[".","#",".","#","."],["#",".",".",".","#"]])
    s.maxStudents([[".","#"],["#","#"],["#","."],["#","#"],[".","#"]])
    s.maxStudents([["#",".","#","#",".","#"],[".","#","#","#","#","."],["#",".","#","#",".","#"]])
