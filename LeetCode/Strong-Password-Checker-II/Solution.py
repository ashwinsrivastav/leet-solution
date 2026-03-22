1class Solution:
2    def strongPasswordCheckerII(self, password: str) -> bool:
3        if len(password)<8: return False 
4        stack='';check=0
5        for i in password:
6            if i not in stack:
7                stack=''
8                stack+=i
9            else:
10                return False
11        password=set(password)
12        dic={'upper':False,'lower':False,'digit':False,'special':False}
13        for i in password:
14            if i.isupper():
15                dic['upper']=True
16            elif i.islower():
17                dic['lower']=True
18            elif i in "0123456789":
19                dic['digit']=True
20            elif i in "!@#$%^&*()-+":
21                dic['special']=True
22        print(dic)
23        for i in dic.keys():
24            print(i)
25            if dic[i]==False:
26                return False
27        return True
28
29