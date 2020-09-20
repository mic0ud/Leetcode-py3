#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (51.43%)
# Likes:    111
# Dislikes: 32
# Total Accepted:    7.5K
# Total Submissions: 14.3K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:

# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.

# Since the answer may be too large, return it modulo 10^9 + 7.

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

# Example 2:

# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".

# Example 3: 

# Input: n = 5
# Output: 68

# Constraints:

# 1 <= n <= 2 * 10^4

# @lc code=start
from collections import defaultdict
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # Each vowel allows some number of subsequent characters. These transitions are like a tree. 
        # This problem is asking, "what's the width of the tree with height n?"
        # My solution keeps track of the number of each vowel at a level in this tree. 
        # To calculate say 'A', we calculate how many nodes in the previous level produce 'A'. 
        # This is the number of 'E', 'I', and 'U' nodes.
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n-1):
            a, e, i, o, u = e+i+u, a+i, e+o, i, i+o
        return (a+e+i+o+u) % (10**9 + 7)

    def countVowelPermutation_SLOW(self, n: int) -> int:
        # dp[i][j]: count for words end with i and length j
        dp, vowels, follow = defaultdict(list), ["a", "e", "i" , "o", "u"], {'a': ['e','i','u'], 'e': ['a','i'], 'i': ['e','o'], 'o': ['i'], 'u': ['i','o']}
        for v in vowels:
            dp[v] = [0 for _ in range(n+1)]
            dp[v][1] = 1
        for i in range(2, n+1):
            for v in vowels:
                for prev in follow[v]:
                    dp[v][i] += dp[prev][i-1]
        res = sum([dp[v][n] for v in vowels]) % (10**9 + 7)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.countVowelPermutation(100)
