1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        arr=sorted(nums);ans=[]
4        for i in nums:
5            ans.append(arr.index(i))
6        return ans
7
8        
9
10