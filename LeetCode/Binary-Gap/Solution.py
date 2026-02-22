class Solution:
    def binaryGap(self, n: int) -> int:
        index = []
        n = bin(n)[2:]
        maxx = 0
        for i, j in zip(n, range(len(n))):
            if i == "1":
                index.append(j)
        if len(index) < 2:
            return 0
        for i in range(len(index) - 1):
            if index[i + 1] - index[i] > maxx:
                maxx = index[i + 1] - index[i]
        return maxx
 large;
}
