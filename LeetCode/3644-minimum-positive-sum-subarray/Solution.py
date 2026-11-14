class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        minsum=999999
        for i in range(l,r+1):
            x=0
            while x<len(nums)-i+1:
                sub=nums[x:i+x]
                if sum(sub)<minsum and sum(sub)>0:
                    minsum=sum(sub)
                x+=1
        return -1 if minsum==999999 else minsum