class Solution:
    def check(self, nums: List[int]) -> bool:
        a = deque(nums)
        index = nums.index(min(nums))
        a.rotate(-index)
        if list(a) == sorted(list(a)):
            return True
        else:
            while a[0] == a[-1]:
                a.rotate(1)
        return list(a) == sorted(list(a))
