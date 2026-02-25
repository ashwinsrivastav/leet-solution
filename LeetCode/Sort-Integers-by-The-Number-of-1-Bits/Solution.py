1class Solution:
2    def sortByBits(self, arr: List[int]) -> List[int]:
3        bits={};res=[]
4        for i in arr:
5            bits.setdefault(bin(i).count("1"),[]).append(i)
6        for i in sorted(bits.keys()):
7            res.extend(sorted(bits[i]))
8        return res
9
10