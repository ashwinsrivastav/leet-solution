class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        mydic={}
        for i in words:
            mydic[i]=mydic.get(i,0)+1
        res=[]
        i=0;dic={}
        for i in mydic.keys():
            dic.setdefault(mydic[i],[]).append(i)
        dic=dict(sorted(dic.items(),reverse=True))
        for i in dic.keys():
            res.extend(sorted(dic[i]))
            if len(res)>=k:
                break
        return res[:k]




