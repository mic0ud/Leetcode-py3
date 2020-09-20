#
# @lc app=leetcode id=676 lang=python3
#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (52.64%)
# Likes:    459
# Dislikes: 110
# Total Accepted:    31.8K
# Total Submissions: 60.3K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n' +
#  '[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
# 
# Implement a magic directory with buildDict, and search methods.
# 
# 
# 
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
# 
# 
# 
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
# 
# 
# Example 1:
# 
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
# 
# 
# 
# Note:
# 
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
# 
# 
#

# @lc code=start
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.nodes = defaultdict(dict)
        self.end = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def buildDict(self, wordDict: [str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for s in wordDict:
            self._insert(s)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        curr = self.root
        return self._search2(word, curr)

    def _search2(self, word: str, curr: TrieNode) -> bool:
        if not word or not curr.nodes:
            return False
        if word[0] in curr.nodes:
            for k,n in curr.nodes.items():
                if k != word[0] and self._search(k+word[1:], curr):
                    return True
            return self._search2(word[1:], curr.nodes[word[0]])
        else:
            for n in curr.nodes.values():
                if self._search(word[1:], n):
                    return True
            return False
        
        
    def _insert(self, word: str):
        curr = self.root
        for w in word:
            if w not in curr.nodes:
                curr.nodes[w] = TrieNode()
            curr = curr.nodes[w]
        curr.end = True

    def _search(self, s, node) -> bool:
        curr = node
        for c in s:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.end

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
# @lc code=end
# ["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
if __name__ == '__main__':
    s = MagicDictionary()
    s.buildDict(["hello","leetcode", "hallo"])
    print(s.search("hello"))
