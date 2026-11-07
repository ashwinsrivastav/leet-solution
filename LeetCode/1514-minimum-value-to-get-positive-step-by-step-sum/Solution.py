class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        minn = float("inf")
        running = 0
        for i in nums:
            running += i
            minn = min(minn, running)
        return abs(minn) + 1 if minn < 1 else 1
