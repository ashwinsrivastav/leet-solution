1from collections import defaultdict
2from typing import List
3
4class Solution:
5    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
6        count = defaultdict(int)
7        for row in matrix:
8            comp = tuple(1 - x for x in row)
9            row_tup = tuple(row)
10            key = row_tup if row_tup < comp else comp
11            count[key] += 1
12        return max(count.values())