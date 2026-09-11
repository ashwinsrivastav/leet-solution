1class Solution:
2    def reverse(self, x: int) -> int:
3        x=str(x)
4        if x[0]=="-":
5            x=x[1:]
6            x=x[::-1]
7            y=int("-"+x)
8        else:
9            y=int(x[::-1])
10        if y<= -2147483648 or y>=2147483647:
11            return 0
12        return y
13        
14        