1class Solution:
2    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
3        res=[0]*len(nums);even=0;odd=1
4        for i in nums:
5            if i%2==0:
6                res[even]=i
7                even+=2
8            else:
9                res[odd]=i
10                odd+=2
11        return res
12        