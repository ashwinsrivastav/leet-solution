1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        ans=[]
4        for i in nums:
5            for j in str(i):
6                ans.append(int(j))
7        return ans