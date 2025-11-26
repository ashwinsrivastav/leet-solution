1class Solution:
2    def isUgly(self, n: int) -> bool:
3        if n<=0:
4            return False
5        while n>1:
6            if n%2==0:
7                n/=2
8            elif n%3==0:
9                n/=3
10            elif n%5==0:
11                n/=5
12            else:
13                return False
14        return True
15
16
17        