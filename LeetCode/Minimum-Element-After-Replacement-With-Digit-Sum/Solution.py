1class Solution:
2    def minElement(self, nums: List[int]) -> int:
3        def sum(x):
4            temp=0
5            while x>0:
6                temp+=x%10
7                x=x//10
8            return temp
9        min=999999999
10        for i in nums:
11            temp=sum(i)
12            if min>temp:
13                min=temp
14        return min
15