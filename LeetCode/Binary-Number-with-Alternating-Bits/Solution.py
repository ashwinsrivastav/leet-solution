1class Solution:
2    def hasAlternatingBits(self, n: int) -> bool:
3        a=bin(n)
4        a=a[2:]
5        for i in range(len(a)-1):
6            if a[i]==a[i+1]:
7                return False
8        return True
9        