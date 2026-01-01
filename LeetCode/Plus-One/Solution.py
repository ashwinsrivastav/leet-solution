1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        i=1
4        if len(digits)==digits.count(9):
5            n=0
6            digits[:]=[0]*len(digits)
7            digits.insert(0,1)
8        elif digits[-i]==9:
9            while digits[-i]==9 or digits[-i]==10:
10                digits[-i]=0
11                digits[-i-1]+=1
12                i+=1
13                if digits[-i]==9:
14                    return digits
15                elif i==len(digits) and digits[0]==10:
16                    digits[0]+=1 
17                    digits.insert(0,1)
18                elif i==len(digits):
19                    return digits
20        else:
21            digits[-i]+=1
22        return digits
23