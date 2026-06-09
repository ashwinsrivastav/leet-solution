1class Solution:
2    def maxTotalValue(self, nums: List[int], k: int) -> int:
3        return (max(nums)-min(nums))*k