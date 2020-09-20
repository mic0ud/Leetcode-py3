#
# @lc app=leetcode id=1157 lang=python3
#
# [1157] Online Majority Element In Subarray
#
# https://leetcode.com/problems/online-majority-element-in-subarray/description/
#
# algorithms
# Hard (33.87%)
# Likes:    155
# Dislikes: 21
# Total Accepted:    5.6K
# Total Submissions: 15K
# Testcase Example:  '["MajorityChecker","query","query","query"]\n' +
#  '[[[1,1,2,2,1,1]],[0,5,4],[0,3,3],[2,3,2]]'
#
# Implementing the class MajorityChecker, which has the following API:

# MajorityChecker(int[] arr) constructs an instance of MajorityChecker with the
# given array arr;
# int query(int left, int right, int threshold) has arguments such
# that:
# 
# 0 <= left <= right < arr.length representing a subarray of arr;
# 2 * threshold > right - left + 1, ie. the threshold is always a strict
# majority of the length of the subarray

# Each query(...) returns the element in arr[left], arr[left+1], ...,
# arr[right] that occurs at least threshold times, or -1 if no such element
# exists.
 
# Example:

# MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
# majorityChecker.query(0,5,4); // returns 1
# majorityChecker.query(0,3,3); // returns -1
# majorityChecker.query(2,3,2); // returns 2

# Constraints:

# 1 <= arr.length <= 20000
# 1 <= arr[i] <= 20000
# For each query, 0 <= left <= right < len(arr)
# For each query, 2 * threshold > right - left + 1
# The number of queries is at most 10000


# @lc code=start
from collections import defaultdict
from random import randint
from bisect import bisect_left, bisect_right
class MajorityChecker:

    def __init__(self, arr: [int]):
        self.idx, self.arr = defaultdict(list), arr
        for i,n in enumerate(arr):
            self.idx[n].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        # randomly pick 10 times from arr[left:right+1]
        for _ in range(10):
            a = self.arr[randint(left, right)]
            l = bisect_left(self.idx[a], left)
            r = bisect_right(self.idx[a], right)
            if r-l >= threshold:
                return a
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end
if __name__ == '__main__':
    s = MajorityChecker([1,1,2,2,1,1])
    s.query(0,5,4)
    s.query(0,3,3)
    s.query(2,3,2)
    s = MajorityChecker([2,3,3,1,3,3,1,3,2,3,3,1,1,1,2,1,2,2,2,3,2,2,2,1,2,1,1,2,2,2,2,3,1,1,1,2,2,2,1,3,2,2,3,2,3,1,2,2,3,2,3,1,3,1,1,2,1,1,3,3,3,1,3,1,3,2,3,1,3,2,3,3,1,3,3,3,1,2,3,3,1,3,2,3,3,3,2,1,2,3,3,3,2,3,3,3,3,1,3,1,2,1,1,1,2,1,3,3,1,1,2,3,2,2,2,1,2,3,2,2,2,1,2,2,3,2,3,2,3,1,3,3,3,2,3,1,2,1,3,1,2,2,1,2,3,2,2,3,2,3,1,2,1,2,2,3,2,2,2,1,2,1,2,2,3,2,1,1,1,1,3,2,1,2,3,3,1,3,1,2,1,2,1,2,2,2,2,3,3,1,1,2,1,3,1,1,3,2,3,3,1,2,1,2,2,1,2,1,2,2,2,3,2,1,3,3,3,2,1,1,1,2,3,1,3,3,3,2,3,2,2,1,1,2,3,1,3,3,3,3,1,3,3,1,2,2,1,2,3,3,2,3,3,1,3,3,3,2,3,1,3,3,3,2,3,3,2,2,3,2,2,2,1,2,2,2,2,2,3,2,2,1,2,3,3,2,2,1,2,1,1,2,2,3,3,2,1,1,1,1,1,1,2,2,2,2,2,3,3,1,1,2,3,2,2,2,2,2,1,3,1,3,2,1,3,1,2,3,3,3,2,1,3,3,1,3,1,1,1,1,1,2,1,3,3,3,1,3,3,1,2,1,2,1,2,3,2,1,1,2,3,2,3,2,2,2,2,3,2,2,1,2,2,1,2,2,2,2,1,1,3,1,3,3,1,2,3,2,3,3,1,3,3,2,3,3,3,1,2,2,1,3,2,3,1,3,2,2,3,3,2,2,2,2,1,2,1,3,2,1,1,3,2,2,1,3,1,3,3,2,3,3,3,3,1,3,1,3,3,3,2,1,2,3,2,3,1,2,1,1,3,3,1,3,1,1,1,3,2,2,3,1,2,3,1,2,1,2,1,2,3,1,2,2,3,2,1,3,3,2,1,2,3,2,1,1,2,1,3,3,1,2,2,2,3,2,3,3,2,1,1,3,1,3,1,3,1,3,2,3,2,2,3,1,1,1,3,2,2,3,2,1,1,1,2,2,2,3,1,3,3,2,2,2,1,2,1,3,1,1,3,3,3,3,1,3,3,3,1,2,3,1,3,2,1,1,1,3,1,3,3,1,3,2,1,1,2,2,3,2,1,2,2,2,3,2,2,2,1,3,3,1,1,1,2,3,1,1,1,3,3,1,1,1,2,2,1,2,1,2,2,2,2,3,1,2,3,1,1,2,1,1,2,3,2,3,2,1,2,1,1,1,1,3,1,3,3,3,1,2,1,2,2,3,3,3,2,3,1,3,3,3,2,2,1,2,1,1,1,3,2,3,2,1,3,2,3,1,1,3,2,2,2,3,1,1,1,2,2,2,2,2,1,3,1,2,3,3,3,1,1,1,3,3,1,1,3,1,3,1,2,1,2,3,1,2,1,2,2,1,2,1,2,2,3,2,1,2,2,1,3,2,1,2,2,1,3,3,1,1,3,2,2,3,1,3,1,2,3,2,2,1,3,1,1,3,1,1,1,2,3,3,1,1,1,1,3,2,1,2,1,1,2,2,1,3,1,3,3,2,2,2,2,2,2,3,3,3,2,3,3,2,1,3,3,2,1,3,3,2,1,3,2,3,2,1,3,2,3,2,2,3,3,2,3,2,2,1,3,2,2,2,3,3,2,3,1,2,2,2,2,3,2,2,2,2,1,1,2,3,3,3,1,3,1,2,1,2,3,1,1,2,3,3,1,2,2,1,3,3,1,1,1,3,3,1,2,1,2,1,2,1,1,2,2,1,1,3,2,2,1,1,2,2,1,2,1,2,3,3,2,1,1,1,3,1,3,2,3,2,3,2,2,3,3,1,3,1,1,1,1,1,3,1,3,1,1,2,1,1,3,2,3,3,2,2,1,1,1,1,3,3,2,1,3,1,1,1,3,3,1,2,1,1,3,3,2,3,3,1,1,3,3,2,3,2,2,1,3,2,3,3,1,1,1,2,2,3,3,1,3,2,2,2,1,3,1,3,3,1,1,2,3,3,1,2,2,1,2,1,1,1,3,1,2,2,2,2,2,1,2,2,1,1,3,2,2,1,3,1,3,1,3,3,2,3,2,2,3,2,3,1,2,2,2,3,1,2,2,2,3,2,2,2,1,3,1,2,1,1,1,3,1,2,2,1,3,3,2,2,2,2,3,1,3,2,3,2,3,3,3,1,1,2,2,3,3,2,3,3,2,1,1,2,3,3,2,2,2,2,3,3,3,2,3,2,1,1,3,2,3,2,2,2,2,3,2,1,3,1,2,3,3,1,2,3,1,3,2,1,2,1,2,3,3,2,2,2,1,1,2,3,3,1,3,2,1,2,2,3,2,3,1,1,1,3,2,2,1,1,3,1,2,3,3,1,3,1,1,2,2,1,2,2,3,3,3,2,1,1,2,2,3,3,3,1,2,2,2,3,3,1,2,2,2,1,1,2,2,3,3,2,3,3,2,1,3,1,3,3,1,2,3,1,3,3,2,3,2,2,1,3,1,2,1,3,2,2,1,3,1,3,2,2,2,1,3,3,2,3,3,3,2,1,2,3,2,1,1,2,3,1,1,2,1,3,2,1,1,3,1,2,2,3,1,1,2,3,2,2,2,1,2,1,3,3,1,3,3,3,1,1,1,1,3,1,1,3,2,3,3,1,3,1,1,3,2,3,1,3,1,1,2,1,2,1,1,2,2,3,3,1,2,2,1,2,3,1,1,1,2,2,3,3,1,2,1,2,2,3,1,1,2,3,1,2,3,3,3,2,2,3,1,2,2,2,3,3,1,1,2,2,3,1,2,1,3,3,2,1,2,1,1,1,2,2,2,2,3,1,2,2,3,3,3,1,2,2,2,3,2,3,2,2,1,2,1,2,1,2,1,2,2,1,2,2,1,2,2,3,2,1,1,2,3,1,2,3,2,2,3,1,2,2,3,2,1,3,3,2,2,1,1,3,2,3,3,2,1,1,1,1,2,3,1,3,1,1,1,1,2,2,1,1,2,2,1,1,2,2,3,2,3,1,1,1,1,2,1,2,2,1,2,1,1,1,1,2,1,3,3,1,2,3,1,2,2,1,1,1,2,1,2,1,2,3,2,1,1,1,2,1,1,2,3,1,2,2,3,1,3,2,2,3,3,2,1,2,3,1,1,1,2,1,2,1,3,2,3,2,3,1,2,3,1,1,1,3,2,2,2,2,2,3,2,3,3,1,1,2,2,1,1,1,3,1,3,1,2,1,1,3,3,3,3,3,3,2,1,2,1,3,3,2,3,3,1,2,1,2,2,2,2,2,1,1,2,2,1,1,1,3,3,1,2,3,2,3,3,2,3,3,2,3,2,2,3,1,1,3,1,3,3,2,1,2,1,3,1,1,3,3,1,2,2,2,3,1,2,1,2,3,3,1,3,3,2,3,2,1,1,1,3,3,3,3,2,3,1,1,3,3,3,3,3,1,2,3,1,1,2,2,3,2,1,3,1,1,3,1,2,3,1,3,1,2,1,3,3,3,3,2,1,2,1,1,1,2,2,3,1,1,1,2,2,3,1,3,3,2,3,3,1,3,2,2,2,1,2,2,1,2,3,3,1,3,3,1,3,2,3,2,3,3,3,2,1,1,1,1,2,2,1,2,3,2,3,1,1,1,3,2,1,1,2,3,1,2,2,3,1,2,2,1,1,1,3,1,3,1,1,3,2,3,1,2,3,3,3,1,3,2,2,1,1,2,2,3,1,1,1,1,2,3,1,2,3,1,1,2,1,1,2,2,3,1,2,1,3,1,3,2,1,1,1,3,1,1,2,1,3,3,1,3,3,1,1,1,1,3,2,1,1,3,2,2,2,1,1,3,3,1,3,1,2,3,3,2,1,2,2,3,1,1,1,2,2,3,2,3,3,1,2,1,2,3,2,3,3,2,1,3,2,1,3,1,3,2,3,1,3,3,2,2,3,3,1,2,2,1,1,3,1,2,1,2,1,2,2,1,1,1,2,2,2,1,1,1,1,3,3,3,2,1,3,1,1,3,1,2,3,3,2,1,2,1,1,1,3,3,2,2,1,3,3,1,2,1,2,1,3,2,1,2,2,1,3,2,2,2,3,2,2,2,3,1,2,1,2,1,1,2,1,3,1,1,3,3,1,1,2,1,1,3,3,1,2,3,3,1,1,2,1,2,3,2,2,1,1,3,1,2,3,2,1,2,3,1,2,2,3,2,1,3,1,3,2,3,1,2,2,3,1,3,2,3,2,2,2,3,3,3,3,3,2,2,2,2,3,2,2,3,1,1,2,1,1,2,3,3,2,3,3,3,2,1,3,3,1,2,3,2,2,1,3,1,2,1,1,3,1,3,2,1,1,1,3,1,3,1,2,1,2,2,1,3,3,2,1,3,1,1,3,3,3,1,2,1,3,2,1,2,2,2,3,3,1,2,2,2,2,1,2,3,3,2,3,1,2,1,3,2,2,2,3,2,1,3,3,3,1,1,3,3,2,2,3,2,2,3,2,1,3,2,1,3,3,3,2,3,1,1,1,3,3,1,1,1,3,2,3,3,1,1,1,2,2,1,2,1,2,2,3,1,1,1,2,2,3,3,1,2,3,2,2,1,2,3,1,3,2,3,1,3,1,3,3,1,3,3,1,1,1,3,2,2,3,3,3,2,1,3,3,2,3,1,2,3,3,1,2,3,2,1,1,3,3,1,2,1,1,2,3,3,3,2,1,3,3,3,1,3,3,1,3,1,3,1,2,1,2,1,1,1,2,1,2,3,3,3,2,2,2,3,3,2,2,3,1,3,2,2,3,1,1,2,3,3,1,1,2,1,1,3,3,1,2,1,1,1,2,2,2,3,1,3,2,2,1,1,1,3,1,2,3,1,2,1,2,3,2,3,3,1,3,1,3,2,2,1,1,2,1,3,1,1,3,3,3,1,3,2,1,1,3,1,2,3,2,3,2,3,3,1,2,1,1,3,2,2,1,1,3,2,3,1,1,1,2,2,1,2,3,2,1,2,1,2,2,2,3,1,2,2,3,1,1,2,3,2,2,2,2,2,2,1,1,1,3,3,1,1,2,3,1,1,2,2,1,1,3,1,1,3,1,2,1,1,2,1,1,1,3,3,1,1,1,3,1,1,3,3,3,3,3,2,3,1,3,3,3,2,2,2,1,1,3,3,1,3,1,3,2,2,2,2,3,2,3,2,3,3,3,1,2,1,1,1,1,2,1,3,1,1,3,3,3,3,1,2,3,2,3,2,3,1,2,2,2,2,2,3,3,1,3,3,2,2,1,3,3,3,3,1,3,2,2,2,3,3,3,3,2,1,3,2,1,1,3,3,3,1,1,3,3,1,2,1,2,1,1,3,3,2,2,2,2,1,2,2,1,1,2,3,3,2,2,2,1,1,3,1,2,3,2,3,2,2,2,2,2,3,3,1,2,1,3,2,2,1,2,3,1,3,3,3,2,3,1,1,1,2,1,3,3,2,1,1,1,2,3,1,3,2,3,2,3,1,2,2,1,2,2,1,2,3,3,1,2,1,1,2,1,1,3,3,3,3,1,2,3,1,1,3,1,3,3,3,1,1,1,2,1,2,2,3,2,3,2,1,3,2,3,1,1,2,3,1,3,3,3,3,3,3,2,2,2,3,2,3,2,2,3,2,1,3,3,3,2,3,2,1,1,2,2,1,2,1,3,1,1,3,2,2,3,2,3,1,3,2,3,1,3,3,3,2,1,2,1,3,3,1,1,3,2,3,3,1,3,3,2,3,2,1,3,1,3,2,3,3,2,2,2,1,3,3,2,2,1,3,1,2,3,1,1,2,3,2,1,3,3,1,1,1,1,3,3,2,1,1,2,3,1,2,2,3,3,2,1,2,3,3,1,2,1,1,2,1,3,3,2,2,2,1,3,3,2,2,1,1,1,3,1,2,3,1,1,3,3,2,2,1,2,1,3,1,3,2,3,3,1,1,3,1,3,3,2,2,1,3,2,2,2,3,2,1,2,3,2,3,2,2,3,1,3,3,3,3,3,3,1,2,2,2,1,2,2,2,2,3,1,3,2,2,2,2,1,2,1,2,3,1,3,1,2,2,3,1,2,3,1,2,2,3,2,1,3,2,1,2,2,2,3,3,1,1,2,2,2,2,1,3,1,2,1,2,3,1,1,2,1,2,3,2,2,3,1,1,1,2,2,1,3,1,1,3,3,1,1,3,1,2,3,2,2,3,1,3,3,2,3,1,1,1,1,1,2,3,3,3,2,3,1,3,1,3,3,3,2,1,1,3,2,3,3,2,1,1,2,3,2,1,1,1,3,2,2,2,2,2,1,3,1,2,3,3,3,1,3,2,2,2,1,1,1,1,3,1,1,2,3,2,2,2,3,2,3,3,2,2,1,1,2,1,3,1,2,2,1,2,2,1,2,1,1,2,2,2,3,3,2,2,2,1,3,3,1,2,3,1,2,3,1,3,1,3,1,2,1,1,3,3,3,2,1,1,2,3,1,3,2,1,1,1,3,3,2,3,3,2,3,2,2,2,1,1,1,2,3,1,2,2,2,2,2,2,2,1,3,3,1,2,2,3,2,2,2,3,3,1])
    arr = [[635,2834,1490],[1352,2436,564],[1784,2140,315],[193,2389,1990],[1928,2365,430],[1362,2988,1572],[2208,2954,600],[1355,2182,491],[279,1974,938],[1304,1377,50],[158,653,249],[26,2622,1484],[159,1461,1025],[2012,2809,779],[135,1234,937],[1635,1651,15],[2468,2731,199],[788,2114,771],[1854,2411,492],[381,2522,1125],[304,641,227],[334,1354,713],[559,620,62],[2621,2813,100],[1415,2189,596],[2474,2947,339],[1103,2175,1039],[41,1193,1099],[1362,2142,528],[2575,2858,228],[23,2653,2008],[134,1164,697],[391,1916,849],[541,2367,1223],[666,2295,1451],[583,1188,477],[1859,2108,139],[882,1566,562],[793,949,97],[469,1150,487],[126,1845,1044],[1532,2440,881],[587,2617,1935],[532,863,249],[374,857,456],[1224,2286,1038],[66,2596,2265],[2060,2969,824],[1487,2147,626],[2075,2115,26],[1591,2234,336],[2020,2146,105],[1258,2964,1450],[864,1992,799],[2154,2398,153],[1066,1359,169],[1266,1324,46],[2280,2675,348],[2145,2689,537],[902,2264,1328],[1697,1862,88],[2053,2517,252],[2082,2512,313],[555,2331,1085],[537,2545,1131],[29,580,293],[690,1779,721],[298,549,200],[963,2222,710],[1917,2425,360],[396,1671,670],[1265,2866,1076],[1371,2185,508],[579,1359,551],[1320,2505,724],[1276,2737,1446],[1278,2984,1047],[1513,2207,388],[907,1279,194],[219,2753,2208],[2348,2955,596],[215,2613,2329],[1019,2683,1562],[1194,2024,703],[452,1316,767],[713,1699,942],[513,2841,2004],[881,1329,227],[1652,1953,274],[1244,2927,1646],[149,1970,1743],[640,861,201],[1179,2498,1162],[813,828,11],[1950,1978,26],[613,809,151],[888,2243,761],[1416,2432,873],[364,2004,1200],[988,2339,1016]]
    for a in arr:
        s.query(a[0],a[1],a[2])
