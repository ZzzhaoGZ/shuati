# @Time : 2023/8/27 13:43
# @Author : zhaogang
# @Email : zhaogang_1996@163.com
# @File : merge_interval.py
# @Software: PyCharm

# Definition for an interval.
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals[1:]:
            if ans[-1][1] < s:
                ans.append([s, e])
            else:
                ans[-1][1] = max(ans[-1][1], e)
        return ans