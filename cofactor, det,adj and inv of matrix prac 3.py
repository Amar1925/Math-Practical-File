#cofactor, determinant,adjoint and inverse of matrix
import numpy as np
# determinant
n_array = np.array([[50, 15], [30, 20]])
print("Numpy Matrix is:")
print(n_array)
det = np.linalg.det(n_array)
print("\nDeterminant of given 2X2 matrix:")
print(int(det))
#inverse matrix
print("The inverse matrix is ")
print(np.linalg.inv(n_array))
#cofactor
def matrix_cofactor(matrix):
 
    try:
        determinant = np.linalg.det(matrix)
        if(determinant!=0):
            cofactor = None
            cofactor = np.linalg.inv(matrix).T * determinant
            return cofactor
        else:
            raise Exception("singular matrix")
    except Exception as e:
        print("could not find cofactor matrix due to",e)
print(matrix_cofactor([[1, 2], [3, 4]]))
#adjoint
N=4
A = [[5, -2, 2, 7], [1, 0, 0, 3], [-3, 1, 5, 0], [3, -1, -9, 4]]
def adjoint(A, adj):
 
    if (N == 1):
        adj[0][0] = 1
        return
adj = []
for i in range(N):
    adj.append([None for _ in range(N)])
    adjoint(A, adj)
def display(A):
    for i in range(N):
        for j in range(N):
            print(A[i][j], end=" ")
        print()

adj = [None for _ in range(N)]
print("\nThe Adjoint is :")
adjoint(A, adj)
display(adj)