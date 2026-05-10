1class Solution:
2    def getSum(self, a: int, b: int) -> int:
3        res=[];check=0
4        if a>=0 and b>=0:
5            res.extend([1]*(a+b))
6            return len(res)
7        elif a<0 and b<0:
8            res.extend([0]*(abs(a+b)))
9            return -len(res)
10        elif a<0:
11            res.extend([1]*(b))
12            while a<0 and res:
13                res.pop()
14                a+=1
15            if a==0:
16                return len(res)
17            else:
18                return a
19        else:
20            res.extend([1]*(a))
21            while b<0 and res:
22                res.pop()
23                b+=1
24            if b==0:
25                return len(res)
26            else:
27                return b
28
29        
30
31