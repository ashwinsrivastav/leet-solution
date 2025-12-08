1class Solution:
2    def isMonotonic(self, nums: List[int]) -> bool:
3        if nums[0]>=nums[-1]:
4            if sorted(nums,reverse=True)==nums: return True
5            return False
6        if sorted(nums)==nums: return True
7        return False