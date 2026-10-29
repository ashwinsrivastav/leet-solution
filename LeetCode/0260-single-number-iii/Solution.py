class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor=0
        for i in nums:
            xor^=i
        dif= xor & -xor
        a,b=0,0
        for i in nums:
            if i&dif:
                a^=i
            else:
                b^=i
        return [a,b]