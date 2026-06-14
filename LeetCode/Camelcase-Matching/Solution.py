1class Solution:
2    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
3        res=[];upper=[];upper2=[]
4        for i in pattern:
5            if i.isupper():
6                upper.append(i)
7        for i in queries:
8            temp=list(pattern)
9            temp.append(0)
10            for j in i:
11                if j==temp[0]:
12                    temp.pop(0)
13            if temp[0]==0:
14                for j in i:
15                    if j.isupper():
16                        upper2.append(j)
17            else:
18                res.append(False)
19                continue
20            if len(upper)==len(upper2):
21                for i in range(len(upper)):
22                    if upper[i]!=upper2[i]:
23                        res.append(False)
24                        break
25                else:
26                    res.append(True)
27            else:
28                res.append(False)
29            upper2.clear()
30        return res
31
32
33
34