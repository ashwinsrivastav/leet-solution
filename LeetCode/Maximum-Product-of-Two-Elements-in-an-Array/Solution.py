1class Solution:
2    def maxProduct(self, nums: List[int]) -> int:
3        if nums.count(max(nums))>1:
4            return (max(nums)-1)**2
5        else:
6            a=max(nums)
7            nums.remove(a)
8            return ((a-1)*(max(nums)-1))