class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        j=0
        for i in sorted(nums):
            if i!=j:
               return j
            elif i==j:
                j+=1
        else:
            return len(nums)