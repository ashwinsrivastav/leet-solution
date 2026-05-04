1class Solution:
2    def countAndSay(self, n: int) -> str:
3        if n==1:
4            return "1"
5        def recursive_shit(n,string,x):
6            if x==n-1:
7                return string
8            x+=1
9            count=0;res=""
10            for i in range(len(string)-1):
11                if string[i]==string[i+1]:
12                    count+=1
13                else:
14                    res+= str(count+1)+string[i]
15                    count=0
16            res+=str(count+1)+string[-1]
17            return recursive_shit(n,res,x)
18        return recursive_shit(n,"11",1) 
19