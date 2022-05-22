class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        N,M = len(mat[0]),len(mat)
        T = c * r
        if N * M != T:
            return mat
        output = [[0 for i in range(c)] for j in range(r)]
        
        temp = []
        for i in range(M):
            for j in range(N):
                temp.append(mat[i][j])
        k = 0
        for i in range(r):
            for j in range(c):
                output[i][j] = temp[k]
                k = k + 1
        return output
        
        