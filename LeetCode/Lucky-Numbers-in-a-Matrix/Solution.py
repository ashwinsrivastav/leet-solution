class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        res=[];rmin=0;cmax=[0]*len(matrix[0])
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                if matrix[r][c]>cmax[c]:
                    cmax[c]=matrix[r][c]
        for i in matrix:
            if min(i) in cmax:
                res.append(min(i))
        return res
