#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (55.57%)
# Likes:    660
# Dislikes: 130
# Total Accepted:    52.8K
# Total Submissions: 94.3K
# Testcase Example:  '["cat","bat","rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# You need to output the sentence after the replacement.
# 
# 
# Example 1:
# 
# 
# Input: dict = ["cat","bat","rat"], sentence = "the cattle was rattled by the
# battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# Constraints:
# 
# 
# The input will only have lower-case letters.
# 1 <= dict.length <= 1000
# 1 <= dict[i].length <= 100
# 1 <= sentence words number <= 1000
# 1 <= sentence words length <= 1000
# 
# 
#

# @lc code=start
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(TrieNode)
        self.word = None

class Solution:
    def replaceWords(self, dict: [str], sentence: str) -> str:
        root = self.construct_trie(dict)
        res = sentence.split(' ')
        for i in range(len(res)):
            w = self.search(root, res[i])
            if w:
                res[i] = w
        return ' '.join(res)
        
    def construct_trie(self, strs: [str]) -> TrieNode:
        root = TrieNode()
        for s in strs:
            node = root
            for c in s:
                node = node.nodes[c]
            node.word = s
        return root

    def search(self, root, s) -> str:
        node = root
        for c in s:
            node = node.nodes[c]
            if node.word:
                return node.word
        return None
# @lc code=end

