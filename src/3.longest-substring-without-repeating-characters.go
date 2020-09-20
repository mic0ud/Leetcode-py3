/*
 * @lc app=leetcode id=3 lang=golang
 *
 * [3] Longest Substring Without Repeating Characters
 *
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 *
 * algorithms
 * Medium (29.13%)
 * Likes:    7000
 * Dislikes: 414
 * Total Accepted:    1.2M
 * Total Submissions: 4.1M
 * Testcase Example:  '"abcabcbb"'
 *
 * Given a string, find the length of the longest substring without repeating
 * characters.
 *
 *
 * Example 1:
 *
 *
 * Input: "abcabcbb"
 * Output: 3
 * Explanation: The answer is "abc", with the length of 3.
 *
 *
 *
 * Example 2:
 *
 *
 * Input: "bbbbb"
 * Output: 1
 * Explanation: The answer is "b", with the length of 1.
 *
 *
 *
 * Example 3:
 *
 *
 * Input: "pwwkew"
 * Output: 3
 * Explanation: The answer is "wke", with the length of 3.
 * ⁠            Note that the answer must be a substring, "pwke" is a
 * subsequence and not a substring.
 */
// @lc code=start
func lengthOfLongestSubstring(s string) int {
	idx := make(map[rune]int)
	res, curr := 0, 0
	for i, c := range s {
		val, ok := idx[c]
		if ok && curr <= val {
			curr = val+1
		} else {
			if i-curr+1 > res {
				res = i - curr+1
			}
		}
		idx[c] = i
	}
	return res
}
// @lc code=end

