#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (46.96%)
# Likes:    864
# Dislikes: 18
# Total Accepted:    24.5K
# Total Submissions: 51.8K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
# 
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# 
# Return the number of good subarrays of A.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
#

# @lc code=start
from collections import deque, defaultdict, Counter
class Solution:
    def subarraysWithKDistinct(self, A: [int], K: int) -> int:
        return self.at_most_k(A,K) - self.at_most_k(A,K-1)

    def at_most_k(self, A, K) -> int:
        c = Counter()
        res = i = 0
        for j,a in enumerate(A):
            if c[a] == 0: 
                K -= 1
            c[a] += 1
            while K < 0:
                c[A[i]] -= 1
                if c[A[i]] == 0: 
                    K += 1
                i += 1
            res += j-i+1
        return res

    def subarraysWithKDistinct_TLE(self, A: [int], K: int) -> int:
        idx= {}
        i, j, res, n = 0, 0, 0, len(A)
        while i < n and j < n:
            while len(idx) < K and j < n:
                if A[j] not in idx:
                    idx[A[j]] = deque()
                idx[A[j]].append(j)
                j += 1   
            while j < n and A[j] in idx:
                idx[A[j]].append(j)
                j += 1
            if len(idx) == K:          
                res += self.helper(A[i:j])
            while len(idx) == K:
                idx[A[i]].popleft()
                if not idx[A[i]]:
                    idx.pop(A[i])
                i += 1
        return res if res < float('inf') else 0

    def helper(self, s: str) -> int:
        idx = defaultdict(deque) # indices of keys
        res, i, n, keys = 0, 0, len(s), set(s)
        for j,c in enumerate(s):
            idx[c].append(j)
            if all([idx[k] for k in keys]):
                # from left
                res += min([idx[k][-1] for k in keys])-i
                # to right
                res += n-j
                idx[s[i]].popleft()         
                i += 1   
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    # s.subarraysWithKDistinct([1,2,1,3,4], 3)
    s.subarraysWithKDistinct([1,2,1,2,3], 2)
