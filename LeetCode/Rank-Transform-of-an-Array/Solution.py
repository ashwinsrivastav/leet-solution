1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        arrr=list(set(arr));a=1;rank=[];print(len(arr))
4        arrr.sort();dic={}
5        for i in arrr:
6            dic[i]=a
7            a+=1
8        for i in arr:
9            rank.append(dic[i])
10        return rank
11
12
13
14