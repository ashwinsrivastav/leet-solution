class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        a=len(t) 
        for i in s:
            t=t.replace(i,"")
            a-=1
            if a==len(t):
                continue
            else:
                t=t+(i*(a-len(t)))
        return t