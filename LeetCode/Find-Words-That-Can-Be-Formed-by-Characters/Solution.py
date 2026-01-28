1from collections import Counter
2class Solution:
3    def countCharacters(self, words: List[str], chars: str) -> int:
4        char=Counter(chars);res=0;stopper=0
5        for k in words:
6            a=Counter(k)
7            for i,p in a.items():
8                if a[i]<=char[i]:
9                    pass
10                else:
11                    stopper=1
12            if stopper==0:
13                res+=len(k)
14            stopper=0
15        return res