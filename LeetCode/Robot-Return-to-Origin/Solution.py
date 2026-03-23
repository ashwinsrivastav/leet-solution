1class Solution:
2    def judgeCircle(self, moves: str) -> bool:
3        x=0;y=0
4        for i in moves:
5            if i=="U":
6                y+=1
7            elif i=="R":
8                x+=1
9            elif i=="D":
10                y-=1
11            else:
12                x-=1
13        return (y==0) and (x==0)