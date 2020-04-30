from math import sqrt
import numpy as np
import time
from pprint import pprint

def createMatrixA(n):
    matrix = [[0.0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (i==j):
                matrix[i][j]=10
            elif (matrix[i][j-1]==10):
                matrix[i][j]=2
            elif (matrix[i][j-1]==2):
                matrix[i][j]=1
            elif (matrix[i-1][j]==10):
                matrix[i][j]=2
            elif (matrix[i-1][j]==2):
                matrix[i][j]=1
            else:
                matrix[i][j]=0
    return matrix

def createVectorX(n):
    vector = [1 for i in range(n)]
    return vector

def calculateVectorB(n, x, a):
    vector = [1 for i in range(n)]
    for i in range(n):
        sum= 0
        for j in range(n):
            sum= sum + a[i][j]*x[j]
        vector[i]= sum
    return vector

def guessXValuesAs0 (N):
    return [0 for i in range(N)]

def calculateError (oldX, x):
    max= 0
    return max

def solve(N):
    epsilion= 0.01
    A = createMatrixA(N)
    x = createVectorX(N)
    B= calculateVectorB(N, x, A)
    x= guessXValuesAs0(N)
    Lmax= max(x)

    for i in range(N):
        x[i]= B[i]
        for j in range(N):
            if(i!=j):
                x[i]= x[i] - A[i][j]*x[j]
        x[i]= x[i]/A[i][i]

    while (abs(Lmax-max(x))>epsilion):
        Lmax=max(x)
        for i in range(N):
            x[i]= B[i]
            for j in range(N):
                if(i!=j):
                    x[i]= x[i] - A[i][j]*x[j]
            x[i]= x[i]/A[i][i]


    pprint(A)
    pprint(B)
    print("x:")
    pprint(x)

N = 5
startTime = time.time()
solve(N)
endTime = time.time()
print ('Darbo laikas: ' + str(endTime - startTime))