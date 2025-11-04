def check(dict,a,s,pattern):
    if len(set(a))!=len(set(s)) or len(pattern)!=len(s):
        return False
    for val,i in zip(a,range(len(s))):
        if dict[val]!=s[i]:
            return False
    else:
        return True
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict={};a=[];s=s.split()
        for i,j in zip(pattern,s):
            a.append(i)
            dict[i]=j
        return check(dict,a,s,pattern)