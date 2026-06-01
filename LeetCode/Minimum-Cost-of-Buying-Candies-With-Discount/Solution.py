1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse=True);freeturn=1;totalcost=0
4        for i in cost:
5            if freeturn%3==0:
6                freeturn+=1
7                continue
8            freeturn+=1
9            totalcost+=i
10        return totalcost