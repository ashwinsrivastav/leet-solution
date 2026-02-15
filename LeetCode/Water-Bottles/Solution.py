class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drink=numBottles
        while numBottles//numExchange>=1:
            drink+=numBottles//numExchange
            numBottles=(numBottles%numExchange)+(numBottles//numExchange)
        return drink
            
