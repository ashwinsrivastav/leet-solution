1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        a=nums[0]
4        nums.pop(0)
5        nums.sort()
6        return a+nums[0]+nums[1]