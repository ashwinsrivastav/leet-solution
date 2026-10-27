class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res=["."+"#"*(n-1)]*(m-1)
        res.append("."*n)
        return res
                
