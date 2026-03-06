1class Solution:
2    def checkOnesSegment(self, s: str) -> bool:
3        i=0;s=s+"0"
4        while i<len(s) and s[i]=="1":
5            i+=1
6        s=s[i:]
7        return int(s)==0
8        