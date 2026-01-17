1class Solution:
2    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
3        m=[];s=set(nums)
4        for i in range(1,len(nums)+1):
5            if i not in s:
6                 m.append(i)
7        return m
8