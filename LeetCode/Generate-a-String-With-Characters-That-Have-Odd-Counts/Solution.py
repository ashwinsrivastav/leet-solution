1class Solution:
2    def generateTheString(self, n: int) -> str:
3        if n%2==0:
4            return ("h"*(n-1))+"i"
5        else:
6            return "h"*n