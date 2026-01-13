1class Solution:
2    def maximum69Number (self, num: int) -> int:
3        a=''; a=(str(num)).replace("6","9",1)
4        if a=="": return num
5        return int(a)
6        