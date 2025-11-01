class Solution:
    def climbStairs(self, n: int) -> int:
        prev=0; curr=1
        for i in range(n):
            curr=prev+curr
            prev=curr-prev
        return curr