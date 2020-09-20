#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (43.75%)
# Likes:    3094
# Dislikes: 362
# Total Accepted:    519.4K
# Total Submissions: 1.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
# 
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# 
# Example:
# 
# 
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# 
# 
# Note:
# 
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
# 
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> [str]:
        if not digits:
            return []

        m = {'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res = []

        def search(i, s, res:[]):
            if i >= len(digits):
                res.append(s)
                return
            for c in m[digits[i]]:
                search(i+1, s+c, res)

        search(0, '', res)
        return res
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.letterCombinations('23')
