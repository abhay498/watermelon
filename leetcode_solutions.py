#############################################################
# 566. Reshape the Matrix
# https://leetcode.com/problems/reshape-the-matrix/submissions/ 
  
# M1
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])

        if m * n != r * c:
            return mat
        
        new_matrix = [[0 for _ in range(c)] for _ in range(r)]
        flatten_matrix = []
        
        for i in range(m):
            for j in range(n):
                flatten_matrix.append(mat[i][j])
                
        k = 0
        for i in range(r):
            for j in range(c):
                new_matrix[i][j] = flatten_matrix[k]
                k += 1
                
        return new_matrix



#############################################################
