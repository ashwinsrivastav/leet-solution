1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        return nums.index(max(nums))