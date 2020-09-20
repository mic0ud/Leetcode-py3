#
# @lc app=leetcode id=1235 lang=python3
#
# [1235] Maximum Profit in Job Scheduling
#
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/description/
#
# algorithms
# Hard (44.42%)
# Likes:    272
# Dislikes: 4
# Total Accepted:    7.3K
# Total Submissions: 16.6K
# Testcase Example:  '[1,2,3,3]\n[3,4,5,6]\n[50,10,40,70]'
#
# We have n jobs, where every job is scheduled to be done from startTime[i] to
# endTime[i], obtaining a profit of profit[i].
# 
# You're given the startTime , endTime and profit arrays, you need to output
# the maximum profit you can take such that there are no 2 jobs in the subset
# with overlapping time range.
# 
# If you choose a job that ends at time X you will be able to start another job
# that starts at time X.

# Example 1:

# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

# Example 2:

# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit =
# [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
 
# Example 3:
 
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6

# Constraints:
# 
# 
# 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
# 1 <= startTime[i] < endTime[i] <= 10^9
# 1 <= profit[i] <= 10^4


# @lc code=start
from operator import itemgetter
from bisect import bisect_left, bisect_right
class Solution:
    def jobScheduling(self, startTime: [int], endTime: [int], profit: [int]) -> int:
        end, n = [(i, endTime[i]) for i in range(len(endTime))], len(endTime)
        end.sort(key=itemgetter(1))
        # endIdx, endTime = [end[i][0] for i in range(n)], [end[i][1] for i in range(n)]
        startTime, endTime, profit = [startTime[end[i][0]] for i in range(n)], [end[i][1] for i in range(n)], [profit[end[i][0]] for i in range(n)]
        # dp1[i]: profit at i if i selected
        # dp2[i]: profit at i if i NOT selected
        dp1, dp2 = [0 for _ in range(n)], [0 for _ in range(n)]
        dp1[0] = profit[0]
        for i in range(1, n):
            s = startTime[i]
            prev = bisect_right(endTime, s)
            if prev == 0 and endTime[prev] != s:
                prev = - 1
            while prev > 0 and endTime[prev-1] == s:
                prev -= 1
            if prev > 0 and endTime[prev] > s:
                prev -= 1
            if prev < i:
                dp1[i] = profit[i] + max(dp1[prev] if prev >= 0 else 0, dp2[prev] if prev >= 0 else 0)
            else:
                dp1[i] = profit[i] + max(dp1[i-1], dp2[i-1])
            dp2[i] = max(dp1[i-1], dp2[i-1])
        return max(dp1[-1], dp2[-1])
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.jobScheduling([6,15,7,11,1,3,16,2], [19,18,19,16,10,8,19,8], [2,9,1,19,5,7,3,19])
    s.jobScheduling([1,1,1], [2,3,4], [5,6,4])
    s.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
    s.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
