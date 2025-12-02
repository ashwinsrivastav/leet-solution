1class Solution:
2    def addDigits(self, num: int) -> int:
3        sum=0
4        while num%10!=num:
5            while num>0:
6                sum=sum+num%10
7                num=int(num/10)
8            num=sum
9            sum=0
10        return num
11        
12