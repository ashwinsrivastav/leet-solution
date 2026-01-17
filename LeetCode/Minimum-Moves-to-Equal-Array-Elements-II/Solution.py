1class Solution:
2    def minMoves2(self, nums: List[int]) -> int:
3        chosen_one=sorted(nums)[(len(nums)//2)];moves=0
4        for i in nums:
5            moves+=abs(i-chosen_one)
6        return moves
7