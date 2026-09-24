1class Solution:
2    def smallestIndex(self, nums: List[int]) -> int:
3        def digit_sum(n):
4            sum=0
5            while n>0:
6                temp=n%10
7                sum+=temp
8                n=n//10
9            return sum
10        for i in range(len(nums)):
11            if i==digit_sum(nums[i]):
12                return i
13        return -1