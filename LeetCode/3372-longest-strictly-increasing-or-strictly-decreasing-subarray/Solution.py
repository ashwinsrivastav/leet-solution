class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        def incc(i,nums,inc):
            while i<len(nums)-1:
                if nums[i]<nums[i+1]:
                    inc+=1;i+=1
                    continue
                break
            return i,inc
        def decc(i,nums,dec):
            while i<len(nums)-1:
                if nums[i]>nums[i+1]:
                    dec+=1;i+=1
                    continue
                break
            return i,dec
        inc=1;dec=1;i=0;maxx=0
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                i,inc=incc(i,nums,inc)
                if inc>maxx:
                    maxx=inc
                inc=1
            elif nums[i]>nums[i+1]:
                i,dec=decc(i,nums,dec)
                if dec>maxx:
                    maxx=dec
                dec=1
            else:
                i+=1
        return max(maxx,1)