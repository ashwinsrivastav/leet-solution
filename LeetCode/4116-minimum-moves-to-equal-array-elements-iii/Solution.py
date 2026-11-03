class Solution:
    def minMoves(self, nums: List[int]) -> int:
        highest=max(nums);moves=0
        for i in nums:
            moves+=(highest-i)
        return moves
