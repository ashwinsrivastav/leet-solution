1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        error=0;res=[]
4        for i in queries:
5            for j in dictionary:
6                for x in range(len(j)):
7                    if i[x]!=j[x]:
8                        error+=1
9                if error>2:
10                    pass
11                else:
12                    res.append(i)
13                    error=0
14                    break
15                error=0
16        return res
17
18                    
19
20    