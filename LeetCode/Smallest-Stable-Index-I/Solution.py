1class Solution:
2    def firstStableIndex(self, nums: list[int], k: int) -> int:
3        if len(nums)<2:
4            return 0
5        elif len(nums)==2:
6            if nums[0]<=nums[1] or nums[0]-nums[1]<=k:
7                return 0
8            else:
9                return -1
10        for i in range(len(nums)):
11            if max(nums[:i+1:])-min(nums[i::])<=k:
12                return i
13        return -1