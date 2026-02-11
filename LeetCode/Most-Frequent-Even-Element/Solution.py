1class Solution:
2    def mostFrequentEven(self, nums: List[int]) -> int:
3        nums=list(filter(lambda x:x%2==0,nums)) ;dec={}
4        if len(nums)>0:
5            for x in nums:
6                dec[x]=dec.get(x,0)+1
7            maxx=max(dec.values())
8            nums=[]
9            for i in dec.keys():
10                if dec[i]==maxx:
11                    nums.append(i)
12            return min(nums)
13        return -1