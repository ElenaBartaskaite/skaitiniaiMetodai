import numpy as np
import time

N = 100
X = np.ones((N, 1))
error_value = 0.01


def getA(N_value):
    matrix = np.zeros((N_value, N_value), dtype=np.int32)
    np.fill_diagonal(matrix, 30)
    np.fill_diagonal(matrix[1:], -16)
    np.fill_diagonal(matrix[2:], 1)
    np.fill_diagonal(matrix[:, 1:], -16)
    np.fill_diagonal(matrix[:, 2:], 1)

    return matrix


def getF(N_value, X_value):
    c = 1. / ((N_value + 1) ** 2)
    X_value = np.append(X_value, 0)
    X_value = np.insert(X_value, 0, 0)

    func = lambda i, j: c + 2 * (X_value[int(i) + 2] - X_value[int(i)]) ** 2
    func = np.vectorize(func)

    matrix = np.fromfunction(func, (N_value, 1))

    return matrix


def cholesky(A_value, N_value):
    cholesky_composition = np.zeros((N_value, N_value))

    for i in xrange(N_value):
        for k in xrange(i + 1):
            tmp_sum = sum(cholesky_composition[i][j] * cholesky_composition[k][j] for j in xrange(k))

            if i == k:
                cholesky_composition[i][k] = np.sqrt(A_value[i][i] - tmp_sum)
            else:
                cholesky_composition[i][k] = (1. / cholesky_composition[k][k] * (A_value[i][k] - tmp_sum))
    return cholesky_composition


def findY(choleskyTriangle, B, N_value):
    i = 0
    matrixVariable = np.zeros((N, 1))
    while i < N_value:
        j = 0
        rowSum = 0
        while j < i:
            rowSum += choleskyTriangle[i][j] * matrixVariable[j][0]
            j += 1

        value = (B[i][0] - rowSum) / choleskyTriangle[i][i]
        matrixVariable[i][0] = value
        i += 1

    return matrixVariable


def findX(transposedCholeskyTriangle, Y_value, N_value):
    i = N_value - 1
    matrixVariable = np.zeros((N, 1))
    while i >= 0:
        j = N_value - 1
        rowSum = 0
        while j > i:
            rowSum += transposedCholeskyTriangle[i][j] * matrixVariable[j][0]
            j -= 1

        value = (Y_value[i][0] - rowSum) / transposedCholeskyTriangle[i][i]
        matrixVariable[i][0] = value
        i -= 1

    return matrixVariable


# A = LLt
A = getA(N)

# startTime = time.time()
choleskyA = cholesky(A, N)
# print choleskyA
# print np.linalg.cholesky(A)
# endTime = time.time()
# print 'Cholesky: ' + str(endTime - startTime)

transposedCholeskyA = np.transpose(choleskyA)

# print np.matmul(choleskyA, transposedCholeskyA)

k = 0
error_too_big = True
startTime = time.time()
while error_too_big:
    previousX = X
    F = getF(N, X)
    i = 0
    Y = np.zeros((N, 1))
    # LY = B
    Y = findY(choleskyA, F, N)
    # LtX = Y
    X = findX(transposedCholeskyA, Y, N)
    k += 1
    error_too_big = np.max(np.abs(previousX - X)) > error_value
    print str(k) + ' iteracija: ' + str(X[:,0])
    # if k == 1:
    #     print "Viena iteracija: " + str(time.time() - startTime)

print X
print np.linalg.solve(A, Y)

# print np.matmul(A, X)
# print getF(N, X)