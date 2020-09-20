#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (41.99%)
# Likes:    2223
# Dislikes: 40
# Total Accepted:    230.6K
# Total Submissions: 536.6K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
# 
# Example:
# 
# 
# Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true
# 
# 
# Note:
# 
# 
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # g[0] is the root
        # g[0] = {a:({}, True), b:({}, False)}
        self.g = defaultdict(dict)     

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return
        # tmp: {a: [{b: [{}, False]}, True]}
        tmp = self.g[0]
        for i in range(len(word)):
            if word[i] not in tmp:
                tmp[word[i]] = [defaultdict(dict), False]
            if i < len(word) - 1:
                tmp = tmp[word[i]][0]
        tmp[word[-1]][1] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return False
        tmp = self.g[0]
        for i in range(len(word)):
            if word[i] not in tmp:
                return False
            if i < len(word) - 1:
                tmp = tmp[word[i]][0]
        # print(tmp)
        return tmp[word[-1]][1]

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return False
        tmp = self.g[0]
        for i in range(len(prefix)):
            if prefix[i] not in tmp:
                return False
            if i < len(prefix) - 1:
                tmp = tmp[prefix[i]][0]
        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end
# ["Trie","insert","search","startsWith"]\n[[],["a"],["a"],["a"]]
# ["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]\n[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
