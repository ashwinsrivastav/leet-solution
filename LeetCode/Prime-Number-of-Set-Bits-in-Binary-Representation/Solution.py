class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            if n<3:
               return True if n==2 else False
            for i in range(2,n):
                if n%i==0:
                    return False
            return True
        count=0
        for i in range(left,right+1):
            n=bin(i).count("1")
            if prime(n):
                count+=1
        return count
