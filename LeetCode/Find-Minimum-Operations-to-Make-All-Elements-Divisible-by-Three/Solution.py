class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                continue
            a=nums[i]%3
            if a==1:
                nums[i]-=1
            else:
                nums[i]+=1
            count+=1
        return count
