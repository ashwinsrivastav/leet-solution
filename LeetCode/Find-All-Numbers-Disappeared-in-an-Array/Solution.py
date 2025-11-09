class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = sorted(set(range(1, len(nums)+1)) - set(nums))
        return missing