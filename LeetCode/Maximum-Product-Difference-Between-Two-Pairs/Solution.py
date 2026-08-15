1class Solution:
2    def maxProductDifference(self, nums: List[int]) -> int:
3        nums.sort()
4        return (nums[-1]*nums[-2])-(nums[0]*nums[1])