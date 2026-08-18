1class Solution:
2    def largestInteger(self, nums: List[int], k: int) -> int:
3        dic = {}
4        could_be = [-1]
5        for i in nums:
6            dic[i] = dic.get(i, 0) + 1
7        if k < len(nums) and k!=1:
8            if dic[nums[0]] == 1:
9                could_be.append(nums[0])
10            if dic[nums[-1]] == 1:
11                could_be.append(nums[-1])
12        elif k==1:
13            for i in sorted(nums, reverse=True):
14                if dic[i] == 1:
15                    return i
16            else:
17                return -1
18        elif k==len(nums):
19            return max(nums)
20        else:
21            return -1
22        return max(could_be)
23