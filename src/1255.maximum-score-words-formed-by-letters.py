#
# @lc app=leetcode id=1255 lang=python3
#
# [1255] Maximum Score Words Formed by Letters
#
# https://leetcode.com/problems/maximum-score-words-formed-by-letters/description/
#
# algorithms
# Hard (70.94%)
# Likes:    105
# Dislikes: 7
# Total Accepted:    5.8K
# Total Submissions: 8.4K
# Testcase Example:  '["dog","cat","dad","good"]\n["a","a","c","d","d","d","g","o","o"]\n[1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]'
#
# Given a list of words, list of  single letters (might be repeating) and score
# of every character.
# 
# Return the maximum score of any valid set of words formed by using the given
# letters (words[i] cannot be used two or more times).
# 
# It is not necessary to use all characters in letters and each letter can only
# be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0],
# score[1], ... , score[25] respectively.
# 
# 
# Example 1:
# 
# 
# Input: words = ["dog","cat","dad","good"], letters =
# ["a","a","c","d","d","d","g","o","o"], score =
# [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with
# a score of 23.
# Words "dad" and "dog" only get a score of 21.
# 
# Example 2:
# 
# 
# Input: words = ["xxxz","ax","bx","cx"], letters =
# ["z","a","b","c","x","x","x"], score =
# [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5)
# with a score of 27.
# Word "xxxz" only get a score of 25.
# 
# Example 3:
# 
# 
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score =
# [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 14
# 1 <= words[i].length <= 15
# 1 <= letters.length <= 100
# letters[i].length == 1
# score.length == 26
# 0 <= score[i] <= 10
# words[i], letters[i] contains only lower case English letters.


# @lc code=start
from collections import Counter
class Solution:
    def maxScoreWords(self, words: [str], letters: [str], score: [int]) -> int:
        count, res = Counter(letters), []
        def dfs(i, path):
            if i >= len(words):
                res.append(path)
                return
            take = True
            for w in words[i]:
                count[w] -= 1
                if count[w] < 0:
                    take = False
            if take:
                dfs(i+1,path+[words[i]])
            for w in words[i]:
                count[w] += 1
            dfs(i+1, list(path))
        dfs(0,[])
        maxScore = 0
        res = [Counter(''.join(path)) for path in res]
        for r in res:
            tmp = 0
            for k in r:
                tmp += score[ord(k)-97] * r[k]
            maxScore = max(maxScore, tmp)
        return maxScore        
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.maxScoreWords(["leetcode"], ["l","e","t","c","o","d"], [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0])
    s.maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])
    s.maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])
