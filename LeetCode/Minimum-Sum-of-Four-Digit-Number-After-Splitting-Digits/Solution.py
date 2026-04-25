1class Solution:
2    def minimumSum(self, num: int) -> int:
3        num=sorted(str(num))
4        return (int(num[0]+num[2])+int(num[1]+num[3]))
5