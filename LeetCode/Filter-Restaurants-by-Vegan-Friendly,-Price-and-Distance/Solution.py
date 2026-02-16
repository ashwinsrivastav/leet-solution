1class Solution:
2    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
3        dec={};res=[]
4        if veganFriendly==0:
5            restaurants=list(filter(lambda x: x[3]<=maxPrice and x[4]<=maxDistance , restaurants))
6            for i in restaurants:
7                dec[i[1]]=dec.get(i[1],[])+[i[0]]
8            for i in sorted(dec.keys(),reverse=True):
9                res.extend(sorted(dec[i],reverse=True))
10            return res
11        else:
12            restaurants=list(filter(lambda x: x[2]==1 and (x[3]<=maxPrice and x[4]<=maxDistance) , restaurants))
13            for i in restaurants:
14                dec[i[1]]=dec.get(i[1],[])+[i[0]]
15            for i in sorted(dec.keys(),reverse=True):
16                res.extend(sorted(dec[i],reverse=True))
17            return res
18
19            
20            
21