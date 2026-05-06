1class Solution:
2    def maximumGap(self, nums: List[int]) -> int:
3        nums.sort();max=0
4        for i in range(len(nums)-1):
5            if nums[i+1]-nums[i]>max:
6                max=nums[i+1]-nums[i]
7        return max