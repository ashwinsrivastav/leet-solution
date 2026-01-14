1class Solution:
2    def minSubsequence(self, nums: List[int]) -> List[int]:
3        res=[]
4        for i in sorted(nums, reverse=True):
5            res.append(i)
6            if (sum(nums)-sum(res))-sum(res)<0:
7                return res
8            
9