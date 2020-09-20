#
# @lc app=leetcode id=991 lang=python3
#
# [991] Broken Calculator
#
# https://leetcode.com/problems/broken-calculator/description/
#
# algorithms
# Medium (42.58%)
# Likes:    262
# Dislikes: 61
# Total Accepted:    12.3K
# Total Submissions: 28K
# Testcase Example:  '2\n3'
#
# On a broken calculator that has a number showing on its display, we can
# perform two operations:

# Double: Multiply the number on the display by 2, or;
# Decrement: Subtract 1 from the number on the display.
 
# Initially, the calculator is displaying the number X.
# 
# Return the minimum number of operations needed to display the number Y.
 
# Example 1:

# Input: X = 2, Y = 3
# Output: 2
# Explanation: Use double operation and then decrement operation {2 -> 4 ->
# 3}.

# Example 2:

# Input: X = 5, Y = 8
# Output: 2
# Explanation: Use decrement and then double {5 -> 4 -> 8}.
 
# Example 3:
 
# Input: X = 3, Y = 10
# Output: 3
# Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
 
# Example 4:

# Input: X = 1024, Y = 1
# Output: 1023
# Explanation: Use decrement operations 1023 times.

# Note:

# 1 <= X <= 10^9
# 1 <= Y <= 10^9
# 
#

# @lc code=start
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        else:
            if Y % 2 == 0:
                return self.brokenCalc(X, Y//2) + 1
            else:
                return self.brokenCalc(X, Y//2+1) + 2

    def brokenCalc_SLOW(self, X: int, Y: int) -> int:
        if X >= Y:
            return X - Y
        
        def search(target):
            if target <= X:
                return X - target
            if target == 2*X:
                return 1
            else:
                if target % 2 == 0:
                    return min(search(target//2)+1, search(target//2+1)+3)
                else:
                    return search(target//2+1)+2

        res = search(Y)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.brokenCalc(1,100000000)
