1class Solution:
2    def findContentChildren(self, g: List[int], s: List[int]) -> int:
3        hap=0;g.sort();s.sort();count=0
4        for i in s:
5            if i>=g[count]:
6                hap+=1
7                if count<len(g)-1:
8                    count+=1
9                else:
10                    return hap
11        return hap
12
13
14
15       