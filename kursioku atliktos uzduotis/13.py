import numpy as np
import time

N = 5
X = np.zeros((N, 1))
Xspr = np.fromfunction(lambda i, j: i, (N, 1))
error_value = 0.001


def getA(N_value):
    matrix = np.zeros((N_value, N_value), dtype=np.int32)
    np.fill_diagonal(matrix, 3)
    np.fill_diagonal(matrix[1:], 2)
    np.fill_diagonal(matrix[2:], 1)
    np.fill_diagonal(matrix[:, 1:], 2)
    np.fill_diagonal(matrix[:, 2:], 1)

    i = 0
    while i < N_value:
        j = 0
        row_sum = 0
        while j < N_value:
            row_sum += matrix[i][j]
            j += 1
        matrix[i][i] = row_sum
        i += 1

    return matrix


def getB(A_value, X_value):
    return np.matmul(A_value, X_value)


def matMulScalar(matrix1, matrix2):
    i = 0
    result = 0
    while i < len(matrix1):
        j = 0
        while j < len(matrix1[i]):
            result += (matrix1[i][j] * matrix2[i][j])
            j += 1
        i += 1
    return result


def calcZ(A_value, X_value, B_value):
    return np.matmul(A_value, X_value) - B_value


A = getA(N)
B = getB(A, Xspr)

z = calcZ(A, X, B)
scalarZ = matMulScalar(z, z)

k = 1
# startTime = time.time()
error_too_big = True
while error_too_big:
    multipliedAz = np.matmul(A, z)
    scalarDivision = scalarZ / matMulScalar(multipliedAz, z)

    previousX = X
    X = previousX - scalarDivision * z

    print str(k) + ' iteracija: ' + str(X[:,0])
    k += 1
    previousZ = z
    z = previousZ - scalarDivision * multipliedAz
    scalarZ = matMulScalar(z, z)
    error_too_big = np.max(np.abs(previousX - X)) > error_value
    # if k == 2:
    #     print "Viena iteracija " + str(time.time() - startTime)

# print A
print X
