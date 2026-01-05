from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        re=""
        count=Counter(s)
        for key , value in sorted(count.items(), key=lambda item: item[1], reverse=True):
            re+=(key)*value
        return re




            
