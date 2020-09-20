#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#
# https://leetcode.com/problems/race-car/description/
#
# algorithms
# Hard (37.14%)
# Likes:    367
# Dislikes: 43
# Total Accepted:    14.3K
# Total Submissions: 38.5K
# Testcase Example:  '3'
#
# Your car starts at position 0 and speed +1 on an infinite number line.  (Your
# car can go into negative positions.)
# 
# Your car drives automatically according to a sequence of instructions A
# (accelerate) and R (reverse).
# 
# When you get an instruction "A", your car does the following: position +=
# speed, speed *= 2.
# 
# When you get an instruction "R", your car does the following: if your speed
# is positive then speed = -1 , otherwise speed = 1.  (Your position stays the
# same.)
# 
# For example, after commands "AAR", your car goes to positions 0->1->3->3, and
# your speed goes to 1->2->4->-1.
# 
# Now for some target position, say the length of the shortest sequence of
# instructions to get there.
# 
# 
# Example 1:
# Input: 
# target = 3
# Output: 2
# Explanation: 
# The shortest instruction sequence is "AA".
# Your position goes from 0->1->3.
# 
# 
# 
# Example 2:
# Input: 
# target = 6
# Output: 5
# Explanation: 
# The shortest instruction sequence is "AAARA".
# Your position goes from 0->1->3->7->7->6.
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= target <= 10000.
# 
# 
#

# @lc code=start
from queue import Queue
import math
class Solution:
    def racecar(self, target: int) -> int:
        if target <= 0:
            return 0
        n = math.ceil(math.log(target,2))  # n: n accelerates to pass target
 
        # dp[i]: min instructions for position i, d[i][0] for + speed, dp[i][1] for - speed
        dp = [[float('inf'),float('inf')] for _ in range(2**n)]
        dp[0] = [0, 1]  
        for i in range(1, n+1):
            dp[2**i-1][0] = i
            dp[2**i-1][1] = i + 1    

        for i in range(2, target+1):
            p = math.ceil(math.log(i,2))
            if i == 2**p - 1: continue

            dp[i][0] = p + 1 + min(dp[2**p-1-i][1], dp[2**p-1-i][0]+1)
            dp[i][1] = p + 1 + min(dp[2**p-1-i][0], dp[2**p-1-i][1]+1)
            for j in range(1,i):
                dp[i][0] = min(dp[i][0], dp[j][0]+2+dp[i-j][0], dp[j][1]+1+dp[i-j][1])
                dp[i][1] = min(dp[i][1], dp[j][1]+1+dp[i-j][1], dp[j][0]+2+dp[i-j][1])
        return min(dp[target])

    def racecar_DP_1(self, target: int) -> int:
        if target <= 0:
            return 0
        # dp[i]: min instructions for position i
        dp = [-1 for _ in range(target+1)]
        dp[0] = 0
        dp[1] = 1

        def search(t: int) -> int:
            if dp[t] != -1:
                return dp[t]
            n = 0 # n: n accelerates to pass target
            while 2 ** n <= t:
                n += 1
            if t == 2**n - 1:
                dp[t] = n
                return n
            dp[t] = n + 1 + search(2**n - 1 - t)
            for i in range(n-1):
                currPos = 2**(n-1) - 1 - (2 ** i - 1)
                dp[t] = min(dp[t], n-1+i+2+search(t - currPos))
            return dp[t]
        res = search(target)
        return res

    def racecar_NOT_WORKING(self, target: int) -> int:
        if target <= 0:
            return 0
        dp = [float('inf') for _ in range(4*abs(target)+1)]
        speed = [[] for _ in range(4*abs(target)+1)]
        shift = 2*abs(target)
        dp[shift] = 0
        speed[shift] = [1]
        q = Queue()
        q.put([shift])
        while not q.empty():
            ps = q.get()
            tmp = []
            for i in ps:
                for s in speed[i]:
                    # accelerate
                    nextPosition1 = i+s
                    newSpeed1 = 2*s
                    if 0 <= nextPosition1 <= 4*abs(target):
                        if dp[nextPosition1] > dp[i] + 1:
                            dp[nextPosition1] = dp[i] + 1
                            speed[nextPosition1] = [newSpeed1]
                            tmp.append(nextPosition1)
                        elif dp[nextPosition1] == dp[i] + 1 and newSpeed1 not in speed[nextPosition1]:
                            speed[nextPosition1].append(newSpeed1)
                            tmp.append(nextPosition1)
                    # reverse and accelerate
                    nextPosition2 = i + (1 if s < 0 else -1)
                    newSpeed2 = 2 if s < 0 else -2
                    if 0 <= nextPosition2 <= 4*abs(target):
                        if dp[nextPosition2] > dp[i] + 2:
                            dp[nextPosition2] = dp[i] + 2                
                            speed[nextPosition2] = [newSpeed2]
                            tmp.append(nextPosition2)
                        elif dp[nextPosition2] == dp[i] + 2 and newSpeed2 not in speed[nextPosition2]:
                            speed[nextPosition2].append(newSpeed2)
                            tmp.append(nextPosition2)
            if tmp:
                q.put(tmp)
        return dp[target+shift]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.racecar(300)
