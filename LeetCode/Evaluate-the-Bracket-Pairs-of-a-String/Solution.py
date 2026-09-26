1class Solution:
2    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
3        pair={}
4        for i in knowledge:
5            pair[i[0]]=i[1]
6        i=0
7        while i<len(s):
8            if s[i]=="(":
9                key=""
10                start=i
11                while s[i+1]!=")":
12                    key+=s[i+1]
13                    i+=1
14                end=i+1
15                if key in pair.keys():
16                    s=s[:start]+pair[key]+s[end+1:]
17                else:
18                    s=s[:start]+"?"+s[end+1:]
19                i=start
20            else:
21                i+=1
22        return s
23    
24
25
26
27        
28