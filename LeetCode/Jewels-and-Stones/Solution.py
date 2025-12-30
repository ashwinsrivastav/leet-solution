1class Solution:
2    def numJewelsInStones(self, jewels: str, stones: str) -> int:
3        count=0
4        for i in jewels:
5            count+= stones.count(i)
6        return count