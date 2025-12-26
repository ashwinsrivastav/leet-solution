1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x=str(x)
4        return (x[::-1])==x