class Solution:
    def findComplement(self, num: int) -> int:
        num=bin(num)[2:];b=''
        for i in num:
            if i=='0':
                b=b+'1'
            else:
                b=b+'0'
        return int(b,2)
