class Solution:
    def reverseBits(self, n: int) -> int:
        n=str(format(n,'032b'))
        n=n.removeprefix("0b")
        return int((n[::-1]),2)