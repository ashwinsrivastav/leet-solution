from itertools import batched
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res=[];lis=[]
        dic={}
        for i in range(len(groupSizes)):
            dic.setdefault(groupSizes[i],[]).append(i)
        for i in dic.keys():
            if len(dic[i])//i==1:
                res.append(dic[i])
            else:
                lis=list(batched(dic[i],i))
                for j in lis:
                    res.append(list(j))
        return res
