class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res=[];length=len(code)
        if k>0:
            for i in range(length):
                sum=0
                for l in range(i+1,k+i+1):
                    sum+=code[l%length]
                res.append(sum)
            return res
        elif k<0:
            for i in range(length):
                sum=0
                for l in range(i-1,i+k-1,-1):
                    sum+=code[l%length]
                res.append(sum)
            return res
        else:
            return [0]*len(code)
