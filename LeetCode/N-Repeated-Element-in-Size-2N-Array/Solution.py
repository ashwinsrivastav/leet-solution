1class Solution:
2    def repeatedNTimes(self, nums: List[int]) -> int:
3        for x in nums:
4            if nums.count(x)>1:
5                return x