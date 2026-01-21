1class Solution:
2    def totalMoney(self, n: int) -> int:
3        amount=0;monday=2;a=1
4        for i in range(1,n+1):
5            amount+=a
6            a+=1
7            if i%7==0:
8                a=monday
9                monday+=1
10        return amount
11
12
13
14