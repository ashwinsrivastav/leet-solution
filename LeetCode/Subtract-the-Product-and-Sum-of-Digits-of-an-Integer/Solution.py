1class Solution:
2    def subtractProductAndSum(self, n: int) -> int:
3        prod=1
4        sum=0
5        for i in str(n):
6            prod*=int(i)
7            sum+=int(i)
8        return prod-sum