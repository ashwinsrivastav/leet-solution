1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        nums=sorted(nums)
4        for i in nums:
5            nums.remove(i)
6            if i not in nums:
7                return i