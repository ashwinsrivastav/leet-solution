1class Solution:
2    def singleNonDuplicate(self, nums: List[int]) -> int:
3        for i in range(0,len(nums)-2,2):
4            if nums[i]==nums[i+1]:
5                pass
6            else:
7                return nums[i]
8        return nums[-1]