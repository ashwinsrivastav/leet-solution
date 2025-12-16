1class Solution:
2    def peakIndexInMountainArray(self, arr: List[int]) -> int:
3        return arr.index(max(arr))