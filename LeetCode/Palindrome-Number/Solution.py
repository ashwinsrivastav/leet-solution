1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x=str(x)
4        if (x[-1::-1])==x:
5            return True
6        else:
7            return False 