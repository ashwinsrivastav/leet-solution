class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        lenght=len(nums);i=0;nums.sort()
        while i!=lenght-1:
            if abs(nums[i])>nums[lenght-1]:
                i+=1
            elif abs(nums[i])==nums[lenght-1]:
                if nums[i]<0:
                    return abs(nums[i])
                return -1
            else:
                lenght-=1
        return -1
