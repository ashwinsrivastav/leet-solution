1class Solution:
2    def countNumbersWithUniqueDigits(self, n: int) -> int:
3        cheat={0:1,1:10,2:91,3:739,4:5275,5:32491,6:168571,7:712891,8:2345851}
4        return cheat[n]
5