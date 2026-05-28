1class Solution:
2    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
3        dic={}
4        for i in cpdomains:
5            x=i.split()
6            temp=int(x[0])
7            x.pop(0)
8            x=(str(x[0])).split(".")
9            for j in range(len(x)):
10                dic[".".join(x)]=dic.setdefault(".".join(x),0)+temp
11                x.pop(0)
12        res=[]
13        for i in dic.keys():
14            res.append(str(dic[i])+" "+i)
15        return res
16
17