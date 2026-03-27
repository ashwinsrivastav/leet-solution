class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        check=0
        for i in arr:
            if i%2!=0:
                check+=1
            else:
                check=0
            if check==3:
                return True
        return False
