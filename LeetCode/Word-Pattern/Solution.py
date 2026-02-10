1def check(dict,a,s,pattern):
2    if len(set(a))!=len(set(s)) or len(pattern)!=len(s):
3        return False
4    for val,i in zip(a,range(len(s))):
5        if dict[val]!=s[i]:
6            return False
7    else:
8        return True
9class Solution:
10    def wordPattern(self, pattern: str, s: str) -> bool:
11        dict={};a=[];s=s.split()
12        for i,j in zip(pattern,s):
13            a.append(i)
14            dict[i]=j
15        return check(dict,a,s,pattern)