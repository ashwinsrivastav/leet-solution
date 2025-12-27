1import numpy as np
2class Solution:
3    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
4       a=np.array(matrix)
5       return (a.T).tolist()
6        