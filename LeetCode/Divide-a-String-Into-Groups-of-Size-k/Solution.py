class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        extra=k-(len(s)%k)
        if extra!=k:
            s+=fill*extra
        res=[]
        for i in range(0,len(s),k):
            res.append(s[i:i+k])
        return res
