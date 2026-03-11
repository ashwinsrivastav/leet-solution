1class Solution:
2    def bitwiseComplement(self, n: int) -> int:
3        a = bin(n)
4        b = ""
5        for i in a[2:]:
6            if i == "1":
7                b += "0"
8            else:
9                b += "1"
10        return int(b, 2)
11