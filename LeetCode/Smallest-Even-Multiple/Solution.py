1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        return n if n%2==0 else 2*n
4