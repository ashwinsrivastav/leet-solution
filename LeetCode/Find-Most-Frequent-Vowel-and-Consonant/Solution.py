class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel=('a', 'e', 'i', 'o','u')
        Vfeq={1:0};Cfeq={1:0}
        for i in s:
            if i in vowel:
                Vfeq[i]=Vfeq.get(i,0)+1
            else:
                Cfeq[i]=Cfeq.get(i,0)+1
        return max(Vfeq.values()) + max(Cfeq.values())
