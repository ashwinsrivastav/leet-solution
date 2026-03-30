class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat[0])>1:
            sum=0;lenght=len(mat[0])
            for i in range(lenght):
                sum+=mat[i][i]
            for i,j in zip(range(lenght),range(lenght-1,-1,-1)):
                sum+=mat[i][j]
            if lenght%2!=0:
                n=(lenght//2)
                sum-=mat[n][n]
            return sum
        return mat[0][0]
