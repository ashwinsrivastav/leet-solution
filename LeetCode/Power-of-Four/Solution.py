import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        a=math.ceil(n**0.5)
        for i in range(a-1):
            if n%4==0:
                n/=4
                continue
            else:
                if n==1:
                    return True
                return False
        return True