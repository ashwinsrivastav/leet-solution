class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a=[];b=[];c=[]
        for i in list1:
            if i in list2:
                a.append(list1.index(i)+list2.index(i))
                b.append(i)
        print(a,b)
        for i in range(len(a)):
            if a[i]==min(a):
                c.append(b[i])
        return c