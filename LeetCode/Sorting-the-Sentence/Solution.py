1class Solution:
2    def sortSentence(self, s: str) -> str:
3        a=[x for x in range(len(s.split())+1)]
4        for i in s.split():
5            a[int(i[-1])]=i[:-1]
6        a.pop(0)
7        return " ".join(a)