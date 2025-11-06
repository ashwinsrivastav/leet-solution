class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed)==1:
            if flowerbed[0]==1 and n!=0:
                return False
            return True
        if len(flowerbed)>=2:
            if (flowerbed[0]==0 and flowerbed[1]==0):
                n-=1
                flowerbed[0]=1
            if (flowerbed[-2]==0 and flowerbed[-1]==0):
                n-=1
                flowerbed[-1]=1
        for i in range(len(flowerbed)-2):
            if (flowerbed[i]==0 and flowerbed[i+1]==0 and flowerbed[i+2]==0):
                n-=1
                flowerbed[i+1]=1
        if n<=0:
            return True
        return False