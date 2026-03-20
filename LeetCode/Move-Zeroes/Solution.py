1class Solution:
2    def moveZeroes(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        count=0
7        for i in sorted(nums, reverse=True):
8            if i==0:
9                nums.remove(i)
10                count+=1
11        for i in range(count):
12            nums.append(0)