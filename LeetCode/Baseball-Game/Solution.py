class Solution:
    def calPoints(self, operations: List[str]) -> int:
        a=[]
        for i in operations:
            if i[0]=='-':
                a.append(int(i))
            elif i.isnumeric():
                a.append(int(i))
            elif i=="+":
                a.append(a[-1]+a[-2])
            elif i=="D":
                a.append(2*a[-1])
            else:
                a.pop()
        return sum(a)