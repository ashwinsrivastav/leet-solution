1class Solution:
2    def partitionLabels(self, s: str) -> List[int]:
3        freq={}
4        for i in range(len(s)):
5            freq[s[i]]=i
6        i=0;res=[];max=0;last=-1
7        while i<len(s):
8            max=freq[s[i]]
9            while i<=max:
10                if max>=freq[s[i]]:
11                    i+=1
12                else:
13                    max=freq[s[i]]
14                    i+=1
15            res.append(max-last)
16            last=max
17        return res
18            
19        
20        