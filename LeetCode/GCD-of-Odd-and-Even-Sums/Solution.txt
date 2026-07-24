1class Solution:
2    def gcdOfOddEvenSums(self, n: int) -> int:
3        return n
4        """
5        def gcd(a, b):
6            result = min(a, b)
7            while result > 0:
8                if a % result == 0 and b % result == 0:
9                    break
10                result -= 1
11            return result
12
13        x = n * 2
14        sum = (x * (x + 1)) // 2
15        oddsum = (sum - n) // 2
16        evensum = oddsum + n
17        return gcd(oddsum, evensum)
18        ========time limit exceeded with brute force========
19"""