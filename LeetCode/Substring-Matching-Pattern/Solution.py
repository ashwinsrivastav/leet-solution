class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p=list(filter(None,p.split("*")));k=s
        for i in p:
            if i in k:
                cut=k.index(i)
                k=k[cut+len(i):]
            else:
                return False
        return True
