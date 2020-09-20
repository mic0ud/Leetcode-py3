#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (43.99%)
# Likes:    923
# Dislikes: 238
# Total Accepted:    54.7K
# Total Submissions: 122.3K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
# "johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
# "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#

# @lc code=start
class Solution:
    # def accountsMerge(self, accounts: [[str]]) -> [[str]]:
    #     return

    def accountsMerge(self, accounts: [[str]]) -> [[str]]:
        if not accounts or not accounts[0]:
            return []
        n = len(accounts)
        adj = [[i] for i in range(n)]
        for i in range(n):
            for k in range(i+1, len(accounts)):
                if not set(accounts[i][1:]).isdisjoint(accounts[k][1:]):
                    adj[i].append(k)                        
                    adj[k].append(i)                        
        
        visited = [False for _ in range(n)]
        def dfs(i: int, tmpRes: [int]):
            if visited[i]:
                return
            visited[i] = True
            tmpRes += accounts[i][1:]
            for a in adj[i]:
                dfs(a, tmpRes)
                
        res = []
        for i in range(len(accounts)):
            if not visited[i]:
                tmpRes = []
                dfs(i, tmpRes)
                res.append([accounts[i][0]]+sorted(list(set(tmpRes))))
        return res
# @lc code=end
# [["David","David0@m.co","David1@m.co"],
# ["David","David3@m.co","David4@m.co"],
# ["David","David4@m.co","David5@m.co"],
# ["David","David2@m.co","David3@m.co"],
# ["David","David1@m.co","David2@m.co"]]
if __name__ == '__main__':
    b = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John","johnnybravo@mail.com"], ["John", "johnsmith@mail.com","john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    a = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
    s = Solution()
    s.accountsMergeTLE(a)
