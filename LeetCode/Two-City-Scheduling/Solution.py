1class Solution:
2    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
3        def doessomething(minn,sum,lenn,arr):
4            dic={};j=0
5            for i in arr:
6                dic[j]=abs(i[0]-i[1])
7                j+=1
8            dic=dict(sorted(dic.items(),key=lambda item: item[1]))
9            print(dic)
10            val=list(dic.values());i=0
11            while minn<lenn//2:
12                sum+=val[i]
13                i+=1;minn+=1
14            return sum
15        sum=0;a=[];b=[]
16        for i in costs:
17            if i[0]>i[1]:
18                sum+=i[1]
19                b.append(i)
20                continue
21            sum+=i[0]
22            a.append(i)
23        minn=min(len(a),len(b))
24        if len(a)==len(b):
25            return sum
26        elif len(a)<len(b):
27            return doessomething(minn,sum,len(costs),b)
28        return doessomething(minn,sum,len(costs),a)
29