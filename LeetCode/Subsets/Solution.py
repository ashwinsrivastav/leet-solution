class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def powerset(nums):
            result = [[]]
            for num in nums:
                result += [subset + [num] for subset in result]
            return result
        return powerset(nums)
        
