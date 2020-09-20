#
# @lc app=leetcode id=1024 lang=python3
#
# [1024] Video Stitching
#
# https://leetcode.com/problems/video-stitching/description/
#
# algorithms
# Medium (47.58%)
# Likes:    322
# Dislikes: 16
# Total Accepted:    16.4K
# Total Submissions: 34K
# Testcase Example:  '[[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]\n10'
#
# You are given a series of video clips from a sporting event that lasted T
# seconds.  These video clips can be overlapping with each other and have
# varied lengths.
# 
# Each video clip clips[i] is an interval: it starts at time clips[i][0] and
# ends at time clips[i][1].  We can cut these clips into segments freely: for
# example, a clip [0, 7] can be cut into segments [0, 1] + [1, 3] + [3, 7].
# 
# Return the minimum number of clips needed so that we can cut the clips into
# segments that cover the entire sporting event ([0, T]).  If the task is
# impossible, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], T = 10
# Output: 3
# Explanation: 
# We take the clips [0,2], [8,10], [1,9]; a total of 3 clips.
# Then, we can reconstruct the sporting event as follows:
# We cut [1,9] into segments [1,2] + [2,8] + [8,9].
# Now we have segments [0,2] + [2,8] + [8,10] which cover the sporting event
# [0, 10].
# 
# 
# Example 2:
# 
# 
# Input: clips = [[0,1],[1,2]], T = 5
# Output: -1
# Explanation: 
# We can't cover [0,5] with only [0,1] and [0,2].
# 
# 
# Example 3:
# 
# 
# Input: clips =
# [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]],
# T = 9
# Output: 3
# Explanation: 
# We can take clips [0,4], [4,7], and [6,9].
# 
# 
# Example 4:
# 
# 
# Input: clips = [[0,4],[2,8]], T = 5
# Output: 2
# Explanation: 
# Notice you can have extra video after the event ends.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= clips.length <= 100
# 0 <= clips[i][0], clips[i][1] <= 100
# 0 <= T <= 100
# 
# 
#

# @lc code=start
from collections import defaultdict
from queue import Queue
class Solution:
    def videoStitching(self, clips: [[int]], T: int) -> int:
        g = defaultdict(list)
        maxEnd = 0
        for c in clips:
            maxEnd = max(maxEnd, c[1])
            if not g[c[0]] or g[c[0]][-1] < c[1]:
                g[c[0]] = [i for i in range(c[0]+1, c[1]+1)]
        visited = [False for _ in range(maxEnd+1)]
        q = Queue()
        q.put([0])
        steps = 0
        while not q.empty():            
            ends = q.get()
            next_ = set()
            for e in ends:
                if e == T:
                    return steps
                for v in g[e]:
                    if not visited[v]:
                        next_.add(v)
            if next_:
                steps += 1
                q.put(next_)
        return -1
# @lc code=end
if __name__ == '__main__':
    s = Solution()
    s.videoStitching([[0,4],[2,8]],5)
