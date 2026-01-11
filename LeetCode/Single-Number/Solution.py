1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        freq = {}
4        for num in nums:
5            freq[num] = freq.get(num, 0) + 1  # same as Java getOrDefault(num, 0) + 1
6
7        # filter the one that appears only once
8        for key, value in freq.items():
9            if value == 1:
10                return key