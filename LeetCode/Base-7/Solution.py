1class Solution:
2    def convertToBase7(self, num: int) -> str:
3        neg=0
4        if num==0:
5            return "0"
6        if num<0:
7            num=abs(num)
8            neg=1
9        res=""
10        while num!=0:
11            q=num%7
12            res+=str(q)
13            q=num//7
14            num=q
15        if neg==0:
16            return res[::-1]
17        return "-"+res[::-1]
18        
19
20
21