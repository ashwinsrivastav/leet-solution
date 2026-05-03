1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        a=s
4        for i in s:
5            a=a.removeprefix(i)
6            a=a+i
7            if a==goal:
8                return True
9        return False