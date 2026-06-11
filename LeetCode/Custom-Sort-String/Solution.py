class Solution:
    def customSortString(self, order: str, s: str) -> str:
        dic={};res=""
        for i in s:
            dic[i]=dic.get(i,"")+i
        for i in order:
            if i in dic.keys():
                res+=dic[i]
                del dic[i]
        for i in dic.keys():
            res+=dic[i]
        return res
        
