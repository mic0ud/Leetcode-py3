#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (50.55%)
# Likes:    422
# Dislikes: 56
# Total Accepted:    29K
# Total Submissions: 56.3K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has a hand of cards, given as an array of integers.
# 
# Now she wants to rearrange the cards into groups so that each group is size
# W, and consists of W consecutive cards.
# 
# Return true if and only if she can.

# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
 
# Note:
# 
# 
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length


# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def isNStraightHand(self, hand: [int], W: int) -> bool:
        n = len(hand)
        if n % W > 0:
            return False
        if W == 1:
            return True
        count = defaultdict(int)
        for c in hand:
            count[c] += 1
        heapq.heapify(hand)
        for i in range(n//W):
            start = heapq.heappop(hand)
            while count[start] == 0:
                start = heapq.heappop(hand)
            for j in range(start, start+W):
                if count[j] <= 0:
                    return False
                count[j] -= 1
        return True

    def isNStraightHand_SLOW(self, hand: [int], W: int) -> bool:
        n = len(hand)
        if n % W > 0:
            return False
        count = defaultdict(int)
        for c in hand:
            count[c] += 1
        taken = 0
        keys = sorted(count.keys())
        while taken < n:
            for k in keys:
                if count[k] > 0:
                    break
            for i in range(k, k+W):
                if count[i] <= 0:
                    return False
                count[i] -= 1
                taken += 1
        return True
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.isNStraightHand([1,2,3,6,2,3,4,7,8,9], 5)
