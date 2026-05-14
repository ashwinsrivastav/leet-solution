class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if max(nums)>len(nums):
            return False
        nums.sort()
        for i in range(1,len(nums)):
            if i!=nums[i-1]:
                return False
        if nums[-1]==len(nums)-1:
            return True
        return False
        
