1class Solution:
2    def countCommas(self, n: int) -> int:
3        ans = 0
4        x = 1000
5        while x <= n:
6            ans += n - x + 1
7            x *= 1000
8        return ans