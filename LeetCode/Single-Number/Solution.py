class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        #{"1" :2 ,0 :1 :} -> 
        for num in nums:
            freq[num] = freq.get(num, 0) + 1  # same as Java getOrDefault(num, 0) + 1

        # filter the one that appears only once
        for key, value in freq.items():
            if value == 1:
                return key