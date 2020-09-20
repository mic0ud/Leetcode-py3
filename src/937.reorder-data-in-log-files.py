#
# @lc app=leetcode id=937 lang=python3
#
# [937] Reorder Data in Log Files
#
# https://leetcode.com/problems/reorder-data-in-log-files/description/
#
# algorithms
# Easy (54.01%)
# Likes:    347
# Dislikes: 1065
# Total Accepted:    66.8K
# Total Submissions: 123.9K
# Testcase Example:  '["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]'
#
# You have an array of logs.  Each log is a space delimited string of words.
# 
# For each log, the first word in each log is an alphanumeric identifier.
# Then, either:
# 
# 
# Each word after the identifier will consist only of lowercase letters,
# or;
# Each word after the identifier will consist only of digits.
# 
# 
# We will call these two varieties of logs letter-logs and digit-logs.  It is
# guaranteed that each log has at least one word after its identifier.
# 
# Reorder the logs so that all of the letter-logs come before any digit-log.
# The letter-logs are ordered lexicographically ignoring identifier, with the
# identifier used in case of ties.  The digit-logs should be put in their
# original order.
# 
# Return the final order of the logs.
# 
# 
# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit
# dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5
# 1","dig2 3 6"]
# 
# 
# Constraints:
# 
# 
# 0 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# logs[i] is guaranteed to have an identifier, and a word after the
# identifier.
# 
# 
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digLogs = []
        letLogs = {}
        for log in logs:
            items = log.split(' ')
            try:
                int(items[1])
                digLogs.append(log)
            except:
                letLogs[' '.join(items[1:])+items[0]] = log
        res = []
        for k in sorted(letLogs.keys()):
            res.append(letLogs[k])
        return res + digLogs
# @lc code=end

# ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]