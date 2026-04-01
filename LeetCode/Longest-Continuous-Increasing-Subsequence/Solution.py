1class Solution:
2    def findLengthOfLCIS(self, nums: List[int]) -> int:
3        counter=[];count=1
4        for i in range(len(nums)-1):
5            if nums[i]<nums[i+1]:
6                count+=1
7            else:
8                counter.append(count)
9                count=1
10        counter.append(count)
11        return max(counter)