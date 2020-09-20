#
# @lc app=leetcode id=1125 lang=python3
#
# [1125] Smallest Sufficient Team
#
# https://leetcode.com/problems/smallest-sufficient-team/description/
#
# algorithms
# Hard (44.71%)
# Likes:    240
# Dislikes: 7
# Total Accepted:    5.9K
# Total Submissions: 13K
# Testcase Example:  '["java","nodejs","reactjs"]\n[["java"],["nodejs"],["nodejs","reactjs"]]'
#
# In a project, you have a list of required skills req_skills, and a list of
# people.  The i-th person people[i] contains a list of skills that person
# has.
# 
# Consider a sufficient team: a set of people such that for every required
# skill in req_skills, there is at least one person in the team who has that
# skill.  We can represent these teams by the index of each person: for
# example, team = [0, 1, 3] represents the people with skills people[0],
# people[1], and people[3].
# 
# Return any sufficient team of the smallest possible size, represented by the
# index of each person.
# 
# You may return the answer in any order.  It is guaranteed an answer
# exists.
# 
# 
# Example 1:
# Input: req_skills = ["java","nodejs","reactjs"], people =
# [["java"],["nodejs"],["nodejs","reactjs"]]
# Output: [0,2]
# Example 2:
# Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"],
# people =
# [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
# Output: [1,2]
# 
# 
# Constraints:
# 1 <= req_skills.length <= 16
# 1 <= people.length <= 60
# 1 <= people[i].length, req_skills[i].length, people[i][j].length <= 16
# Elements of req_skills and people[i] are (respectively) distinct.
# req_skills[i][j], people[i][j][k] are lowercase English letters.
# Every skill in people[i] is a skill in req_skills.
# It is guaranteed a sufficient team exists.

# @lc code=start
from collections import defaultdict
class Solution:
    def smallestSufficientTeam(self, req_skills: [str], people: [[str]]) -> [int]:
        m = len(req_skills)
        skillMap = {req_skills[i]: i for i in range(m)}
        dp = {0: []}
        for i,p in enumerate(people):
            skill = 0
            for s in p:
                skill |= 1 << skillMap[s]
            for sk in list(dp.keys()):
                tmp = sk | skill
                if tmp not in dp or len(dp[tmp]) > len(dp[sk])+1:
                    dp[tmp] = dp[sk] + [i]
        return dp[(1 << m)-1]

    def smallestSufficientTeam_SLOW(self, req_skills: [str], people: [[str]]) -> [int]:
        m = len(req_skills)
        dp = {'0'*m: []}
        for i,p in enumerate(people):
            skill = ''.join(['1' if req_skills[i] in p else '0' for i in range(m)])
            for sk in list(dp.keys()):
                tmp = ''.join(['0' if (skill[i] == '0' and sk[i] == '0') else '1' for i in range(m)])
                if tmp not in dp or len(dp[tmp]) > len(dp[sk])+1:
                    dp[tmp] = dp[sk] + [i]
        return dp['1'*m]


    def smallestSufficientTeam_TLE(self, req_skills: [str], people: [[str]]) -> [int]:
        g = defaultdict(list)
        for i,p in enumerate(people):
            for s in p:
                g[s].append(i)
        res = [None]
        def search(i, path:[]):
            if i >= len(req_skills):
                if not res[0] or len(res[0]) > len(path):
                    res[0] = path
                return
            for p in g[req_skills[i]]:
                if p not in path:
                    search(i+1, path+[p])
                else:
                    search(i+1, list(path))
        search(0,[])
        return res[0]
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.smallestSufficientTeam(["algorithms","math","java","reactjs","csharp","aws"], [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]])
    s.smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]])
