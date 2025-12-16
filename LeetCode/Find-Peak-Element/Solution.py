class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if mid - 1 >= low and mid + 1 <= high and nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            elif  mid + 1 <= high and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1

        return low