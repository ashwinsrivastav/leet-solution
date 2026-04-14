1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        res=0;count=0;mapp={'A' : 1, 'B' : 2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
4        for i in range(len(columnTitle)-1,-1,-1):
5            res+=mapp[columnTitle[i]]*(26**(count))
6            count+=1
7        return res