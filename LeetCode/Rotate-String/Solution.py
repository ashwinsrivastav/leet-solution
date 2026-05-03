1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        a=s
4        for i in s:
5            a=a.removeprefix(i)
6            a=a+i
7            print(a)
8            if a==goal:
9                return True
10        return False