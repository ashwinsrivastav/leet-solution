1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        freq = {}
4        #{"1" :2 ,0 :1 :} -> 
5        for num in nums:
6            freq[num] = freq.get(num, 0) + 1  # same as Java getOrDefault(num, 0) + 1
7
8        # filter the one that appears only once
9        for key, value in freq.items():
10            if value == 1:
11                return key