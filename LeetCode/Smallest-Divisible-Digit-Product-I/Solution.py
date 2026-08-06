class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        if n>9:
            last=n%10;first=(n//10)%10;count=-1
            for i in range(last,10):
                count+=1
                if (i*first)%t==0:
                    return n+count
            return int(str(first+1)+"0")
        for i in range(n,n+10):
            if i%t==0 or i==10:
                return i
