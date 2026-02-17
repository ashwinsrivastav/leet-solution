1class Solution:
2    def countAsterisks(self, s: str) -> int:
3        s=s.split("|");count=0
4        for i in range(0,len(s),2):
5            count+=s[i].count("*")
6        return count