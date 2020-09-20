#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (30.62%)
# Likes:    1339
# Dislikes: 82
# Total Accepted:    149.4K
# Total Submissions: 481.9K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        idx = set()
        idx.add((0,0))
        for i in range(1,m+n+1):
            tmp = set()
            for l,r in idx:
                if l < m and s3[i-1] == s1[l]:
                    tmp.add((l+1,r))
                if r < n and s3[i-1] == s2[r]:
                    tmp.add((l,r+1))
            if not tmp:
                return False
            idx = tmp
        return True

    def isInterleave_(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        dp = [set() for _ in range(m+n+1)]
        dp[0].add((0,0))
        for i in range(1,m+n+1):
            for l,r in dp[i-1]:
                if l < m and s3[i-1] == s1[l]:
                    dp[i].add((l+1,r))
                if r < n and s3[i-1] == s2[r]:
                    dp[i].add((l,r+1))
        return len(dp[-1]) > 0

    def isInterleave_SLOW(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False
        dp = [[[False for _ in range(m+n+1)] for _ in range(m+n+1)] for _ in range(m+n+1)]
        dp[0][0][0] = True
        for k in range(1, m+n+1):
            for i in range(1,min(k,m)+1):
                if s3[k-1] == s1[i-1]:
                    dp[k][i][k-i] = dp[k][i][k-i] or dp[k-1][i-1][k-i]
            for j in range(1,min(k,n)+1):
                if s3[k-1] == s2[j-1]:
                    dp[k][k-j][j] = dp[k][k-j][j] or dp[k-1][k-j][j-1]
        return dp[-1][m][n]

    def isInterleave_TLE(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m+n != len(s3):
            return False

        def search(i,j,k) -> bool:
            if i == m+n and j == m and k == n:
                return True
            r1 = r2 = False
            if j < m and s3[i] == s1[j]:
                r1 = search(i+1, j+1, k)
            if k < n and s3[i] == s2[k]:
                r2 = search(i+1, j, k+1)
            return r1 or r2

        res = search(0,0,0)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.isInterleave("cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc","abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb","abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb")
    s.isInterleave("aabcc","dbbca","aadbbbaccc")
    s.isInterleave("aabcc","dbbca","aadbbcbcac")
