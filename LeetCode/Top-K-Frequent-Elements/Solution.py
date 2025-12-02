1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        freq={};ret=[];count=1
4        for i in nums:
5            freq[i] = freq.get(i, 0) + 1
6        c=sorted(list(freq.values()))
7        while True:
8            for key,value in freq.items():
9                if value==c[-count]:
10                    ret.append(key)
11                    count+=1
12                if count==k+1:
13                    return ret
14            count=len(ret)+1
15            if count==k+1:
16                return ret
17            