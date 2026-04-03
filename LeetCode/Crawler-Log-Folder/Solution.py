1class Solution:
2    def minOperations(self, logs: List[str]) -> int:
3        count = 0
4        for i in logs:
5            if i=="./":
6                continue
7            elif i=="../" and count!=0:
8                count-=1
9            elif i=="../" and count==0:
10                continue
11            else:
12                count+=1
13        return count