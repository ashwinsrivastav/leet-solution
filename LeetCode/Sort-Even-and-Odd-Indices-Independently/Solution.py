1class Solution:
2    def sortEvenOdd(self, nums: List[int]) -> List[int]:
3        res=[0]*len(nums)
4        odd=sorted([nums[x] for x in range(1,len(nums),2)],reverse=True)
5        even=sorted([nums[x] for x in range(0,len(nums),2)])
6        for i in range(len(even)):
7            res[i*2]=even[i]
8        for i in range(len(odd)):
9            res[i*2+1]=odd[i]
10        return res
11