1class Solution:
2    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
3        x=nums.count(target);reslis=[]
4        for i in range(x):
5            temp=nums.index(target)
6            reslis.append(abs(temp-start))
7            nums[temp]="visited"
8        return min(reslis)
9