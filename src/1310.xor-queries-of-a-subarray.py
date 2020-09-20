#
# @lc app=leetcode id=1310 lang=python3
#
# [1310] XOR Queries of a Subarray
#
# https://leetcode.com/problems/xor-queries-of-a-subarray/description/
#
# algorithms
# Medium (67.17%)
# Likes:    197
# Dislikes: 10
# Total Accepted:    12.3K
# Total Submissions: 18.2K
# Testcase Example:  '[1,3,4,8]\n[[0,1],[1,2],[0,3],[3,3]]'
#
# Given the array arr of positive integers and the array queries where
# queries[i] = [Li, Ri], for each query i compute the XOR of elements from Li
# to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array
# containing the result for the given queries.
# 
# Example 1:
# 
# 
# Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
# Output: [2,7,14,8] 
# Explanation: 
# The binary representation of the elements in the array are:
# 1 = 0001 
# 3 = 0011 
# 4 = 0100 
# 8 = 1000 
# The XOR values for queries are:
# [0,1] = 1 xor 3 = 2 
# [1,2] = 3 xor 4 = 7 
# [0,3] = 1 xor 3 xor 4 xor 8 = 14 
# [3,3] = 8
# 
# 
# Example 2:
# 
# 
# Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
# Output: [8,0,4,4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 3 * 10^4
# 1 <= arr[i] <= 10^9
# 1 <= queries.length <= 3 * 10^4
# queries[i].length == 2
# 0 <= queries[i][0] <= queries[i][1] < arr.length
# 
#

# @lc code=start
class Solution:
    def xorQueries(self, arr: [int], queries: [[int]]) -> [int]:
        # Xor[0, i] ^ Xor [i, j] = Xor [0, j]
        # Xor[x, y] means xor of all the number from A to B
        # A Xor B Xor B = A
        # if A Xor B = C , then A Xor B Xor B = C Xor B
        # So, Xor[i, j] = Xor[0, j] ^ Xor[0, i]
        pre_xor = [arr[0]]
        for i in range(1,len(arr)):
            pre_xor.append(arr[i] ^ pre_xor[i-1])
        res = []
        for i,j in queries:
            res.append((pre_xor[j] ^ pre_xor[i-1]) if i > 0 else pre_xor[j])
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]])
