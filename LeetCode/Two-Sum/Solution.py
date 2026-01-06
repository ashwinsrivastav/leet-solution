1from numpy import *
2class Solution:
3    def twoSum(self, nums: List[int], target: int) -> List[int]:
4        for i in range(len(nums)):
5            for j in range(len(nums)):
6                if nums[i]+nums[j]==target:
7                    if i!=j:
8                     break
9            if j!=len(nums)-1:
10                break
11        return [j,i]
12
13        