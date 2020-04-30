from math import sqrt
import numpy as np

import time
from pprint import pprint
 
def cholesky(A):
    n = len(A)

    # Create zero matrix for L and Lt
    L = [[0.0] * n for i in range(n)]
    Lt = [[0.0] * n for i in range(n)]

    # Perform the Cholesky decomposition
    for i in range(n):
        for k in range(i+1):
            tmp_sum = sum(L[i][j] * L[k][j] for j in range(k))
            
            if (i == k): # istrizaine
                L[i][k] = sqrt(A[i][i] - tmp_sum)
            else:
                L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))

    for i in range(n):
        for j in range (n):
            Lt[i][j]=L[j][i]

    return (L,Lt)

def createMatrixA(n):
    matrix = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i==j):
                matrix[i][j]=30
            elif (matrix[i][j-1]==30):
                matrix[i][j]=-16
            elif (matrix[i][j-1]==-16):
                matrix[i][j]=1
            elif (matrix[i-1][j]==30):
                matrix[i][j]=-16
            elif (matrix[i-1][j]==-16):
                matrix[i][j]=1
            else:
                matrix[i][j]=0
    return matrix

def C(n):
    return 1/(n+1)**2

def createVectorX(n):
    vector = [1 for i in range(n)]
    return vector

def calculateY(L, B):
    n= len(L)
    y =  [0 for i in range(n)]
    i = 0
    while i < n:
        j = 0
        rowSum = 0
        while j < i:
            rowSum += L[i][j] * y[j]
            j += 1
        temp = (B[i] - rowSum) 
        y[i] =temp/ L[i][i]
        i += 1

    return y


def calculateX(Lt, y):
    n= len(Lt)
    i = n - 1
    x = [0 for i in range(n)]
    while i >= 0:
        j = n - 1
        rowSum = 0
        while j > i:
            rowSum += Lt[i][j] * x[j]
            j -= 1
        x[i] = (y[i] - rowSum) / Lt[i][i]
        i -= 1

    return x

def calculateVectorB(n, x):
    vector = [1 for i in range(n)]
    for i in range(n):
        if (i==0):
            vector[i]=C(n) + 2* (x[i+1] - 0)**2
        elif (i==n-1):
           vector[i]=C(n) + 2* (0 - x[i-1])**2
        else:
           vector[i]=C(n) + 2* (x[i+1] - x[i-1])**2
    return vector

def guessXValuesAs0 (N):
    return [0 for i in range(N)]

def matrixMultiplication (X, Y):
    result = [[0.0] * len(Y) for i in range(len(X))]#MIght be wrong
    # iterate through rows of X
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

def calculateError (oldX, x):
    max= 0
    for i in range(len(x)):
        if (abs(oldX[i]-x[i])>max):
            max = abs(oldX[i]-x[i])
    return max

def doThings(N):
    epsilion= 0
    A = createMatrixA(N)
    #susikuriu x nulini
    x = createVectorX(N)
    startTime = time.time()
    choleskyLs = cholesky(A)
    endTime = time.time()
    L = choleskyLs[0]
    Lt = choleskyLs[1]
    error = float('inf')
    iteration=0

    while(error>epsilion):
        print('iteracija:')
        print(iteration)
        print("x:")
        pprint(x)
        #xk
        oldX=x
        #f(xk)
        
        startTimeL = time.time()
        B = calculateVectorB(N, x)
        Y = calculateY(L, B)
        x = calculateX(Lt,Y)
        endTimeL = time.time()
        
        print ('Lygciu sprendimo laikas: ' + str(endTimeL - startTimeL))
        error= calculateError(oldX, x)
        iteration=iteration+1

    print("N:")
    print(N)
    print("final x:")
    pprint(x)
    print ('Cholesky darbo laikas: ' + str(endTime - startTime))

N = 5
startTime = time.time()
doThings(N)
endTime = time.time()
print ('Darbo laikas: ' + str(endTime - startTime))
    

# print ("A:")
# pprint(A)

# print ("B:")
# pprint(B)