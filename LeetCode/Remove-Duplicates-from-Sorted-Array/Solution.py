1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        if not nums:
4            return 0
5        
6        k = 1
7        for i in range(1, len(nums)):
8            if nums[i] != nums[i - 1]:
9                nums[k] = nums[i]
10                k += 1
11        
12        return k
13