#
# @lc app=leetcode id=1268 lang=python3
#
# [1268] Search Suggestions System
#
# https://leetcode.com/problems/search-suggestions-system/description/
#
# algorithms
# Medium (61.70%)
# Likes:    459
# Dislikes: 77
# Total Accepted:    38.4K
# Total Submissions: 61.3K
# Testcase Example:  '["mobile","mouse","moneypot","monitor","mousepad"]\r\n"mouse"\r'
#
# Given an array of strings products and a string searchWord. We want to design
# a system that suggests at most three product names from products after each
# character of searchWord is typed. Suggested products should have common
# prefix with the searchWord. If there are more than three products with a
# common prefix return the three lexicographically minimums products.
# 
# Return list of lists of the suggested products after each character of
# searchWord is typed. 
# 
# 
# Example 1:
# 
# 
# Input: products = ["mobile","mouse","moneypot","monitor","mousepad"],
# searchWord = "mouse"
# Output: [
# ["mobile","moneypot","monitor"],
# ["mobile","moneypot","monitor"],
# ["mouse","mousepad"],
# ["mouse","mousepad"],
# ["mouse","mousepad"]
# ]
# Explanation: products sorted lexicographically =
# ["mobile","moneypot","monitor","mouse","mousepad"]
# After typing m and mo all products match and we show user
# ["mobile","moneypot","monitor"]
# After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
# 
# 
# Example 2:
# 
# 
# Input: products = ["havana"], searchWord = "havana"
# Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]
# 
# 
# Example 3:
# 
# 
# Input: products = ["bags","baggage","banner","box","cloths"], searchWord =
# "bags"
# Output:
# [["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
# 
# 
# Example 4:
# 
# 
# Input: products = ["havana"], searchWord = "tatiana"
# Output: [[],[],[],[],[],[],[]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= products.length <= 1000
# There are no repeated elements in products.
# 1 <= Σ products[i].length <= 2 * 10^4
# All characters of products[i] are lower-case English letters.
# 1 <= searchWord.length <= 1000
# All characters of searchWord are lower-case English letters.
# 
# 
#

# @lc code=start
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.words = []

class Solution:
    def suggestedProducts(self, products: [str], searchWord: str) -> [[str]]:
        root = self.construct(products)
        res = []
        for s in searchWord:
            root = root.nodes[s]
            res.append(root.words[:min(3, len(root.words))])            
        return res

    def construct(self, words: [str]) -> TrieNode:
        words.sort()
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                node = node.nodes[c]
                node.words.append(w)
        return root
# @lc code=end

