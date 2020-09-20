#
# @lc app=leetcode id=332 lang=python3
#
# [332] Reconstruct Itinerary
#
# https://leetcode.com/problems/reconstruct-itinerary/description/
#
# algorithms
# Medium (33.23%)
# Likes:    1136
# Dislikes: 723
# Total Accepted:    110.6K
# Total Submissions: 329.6K
# Testcase Example:  '[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]'
#
# Given a list of airline tickets represented by pairs of departure and arrival
# airports [from, to], reconstruct the itinerary in order. All of the tickets
# belong to a man who departs from JFK. Thus, the itinerary must begin with
# JFK.
# 
# Note:
# 
# 
# If there are multiple valid itineraries, you should return the itinerary that
# has the smallest lexical order when read as a single string. For example, the
# itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# All airports are represented by three capital letters (IATA code).
# You may assume all tickets form at least one valid itinerary.
# 
# 
# Example 1:
# 
# 
# Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]
# 
# 
# Example 2:
# 
# 
# Input:
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is
# ["JFK","SFO","ATL","JFK","ATL","SFO"].
# But it is larger in lexical order.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: [[str]]) -> [str]:
        if not tickets:
            return []
        g = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            g[f].append(t)
        res = []
        def visit(d: str):
            while g[d]:
                visit(g[d].pop())
            res.append(d)
        visit('JFK')
        return res[::-1]
# @lc code=end
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
# [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
if __name__ == '__main__':
    s = Solution()
    s.findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
    # s.dfs([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]])
