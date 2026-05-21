1class Solution:
2    def buildArray(self, target: List[int], n: int) -> List[str]:
3        i=0;stack=[];count=1;last=target[-1]
4        while i<len(target):
5            x=target[i]
6            if count<x:
7                stack.append("Push")
8                stack.append("Pop")
9                count+=1
10            else:
11                stack.append("Push")
12                i+=1
13                count+=1
14        return stack
15            
16