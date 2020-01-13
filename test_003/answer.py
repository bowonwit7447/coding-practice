import copy 
def Determinant(A, N):
    total = 0
    if len(A) == 2 and len(A[0]) == 2:
        total = A[0][0] * A[1][1] - A[1][0] * A[0][1]
    else:
        for fc in list(range(N)):
            A2 = copy.copy(A)
            A2 = A2[1:]
            height = len(A2)
            for i in range(height): 
                A2[i] = A2[i][0:fc] + A2[i][fc+1:] 
            sign = (-1) ** (fc % 2) # F) 

            det_return = Determinant(A2, N)
            total += sign * A[0][fc] * det_return 
    return total

A = [
        [9,1,3],
        [4,8,2],
        [5,6,7]
    ]
N = 3
y = Determinant(A,N)
print(y)
