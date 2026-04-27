1class Solution:
2    def addStrings(self, num1: str, num2: str) -> str:
3        i, j = len(num1) - 1, len(num2) - 1
4        carry = 0
5        result = []
6
7        while i >= 0 or j >= 0 or carry:
8            n1 = ord(num1[i]) - ord('0') if i >= 0 else 0
9            n2 = ord(num2[j]) - ord('0') if j >= 0 else 0
10
11            total = n1 + n2 + carry
12            carry = total // 10
13            result.append(str(total % 10))
14
15            i -= 1
16            j -= 1
17
18        return ''.join(result[::-1])
19        