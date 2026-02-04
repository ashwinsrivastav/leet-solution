1from collections import Counter
2class Solution:
3    def findAnagrams(self, s: str, p: str) -> List[int]:
4        pp=Counter(p);res=[]
5        length=len(p)
6        for i in range(len(s)-length+1):
7            temp=s[i:i+length]
8            slider=Counter(temp)
9            if pp==slider:
10                res.append(i)
11        return res
12            
13
14