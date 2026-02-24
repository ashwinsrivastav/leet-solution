1class Solution:
2    def findMissingElements(self, nums: List[int]) -> List[int]:
3        missing=[]
4        for i in range(min(nums),max(nums)):
5            if i not in nums:
6                missing.append(i)
7        return sorted(missing)
8