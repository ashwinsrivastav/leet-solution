class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res=[];st=""
        for i in range(m-1):
            st="."
            st=st+"#"*(n-1)
            res.append(st)
        res.append("."*n)
        return res
                
