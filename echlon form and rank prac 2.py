import numpy as np
from sympy import *
B=np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Matrix')
for row in B:
    print(row)
rank=np.linalg.matrix_rank(B)
print("Rank of matrix is: ",rank)
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print("Matrix : {} ".format(M))
   
# Use sympy.rref() method 
M_rref = M.rref()  
      
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))  