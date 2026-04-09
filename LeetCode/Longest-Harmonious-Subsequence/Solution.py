1class Solution:
2    def findLHS(self, nums: List[int]) -> int:
3        freq={};lis=[0]
4        for i in nums:
5            freq[i]=freq.get(i,0)+1
6        needto=sorted(freq.keys())
7        for i in range(len(needto)-1):
8            if needto[i+1]-needto[i]==1:
9                lis.append(freq[needto[i+1]]+freq[needto[i]])
10        return max(lis)
11        
12