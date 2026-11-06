class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        top=0;current=0
        for i in gain:
            current+=i
            if top<current:
                top=current
        return top
