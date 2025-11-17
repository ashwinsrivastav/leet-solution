class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=1
        if len(digits)==digits.count(9):
            n=0
            digits[:]=[0]*len(digits)
            digits.insert(0,1)
        elif digits[-i]==9:
            while digits[-i]==9 or digits[-i]==10:
                digits[-i]=0
                digits[-i-1]+=1
                i+=1
                if digits[-i]==9:
                    return digits
                elif i==len(digits) and digits[0]==10:
                    digits[0]+=1 
                    digits.insert(0,1)
                elif i==len(digits):
                    return digits
        else:
            digits[-i]+=1
        return digits
