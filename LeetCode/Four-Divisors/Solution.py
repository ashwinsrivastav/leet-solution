def fact(n)-> list:
    factt=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            factt.append(i)
            if n//i != i:
                factt.append(n//i)
    return factt 

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        factors=[];summ=0
        for i in nums:
            factors.extend(fact(i))
            #factors.append(i)
            if len(factors)==4:
                summ+=sum(factors)
            factors.clear()
        return summ
