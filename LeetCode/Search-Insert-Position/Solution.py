1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        if target in nums:
4            return nums.index(target)
5        else:
6            nums.append(target)
7            return (sorted(nums)).index(target)