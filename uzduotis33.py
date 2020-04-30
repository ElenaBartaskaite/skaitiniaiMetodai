from math import sin
import numpy as np
import matplotlib.pyplot as plt

import time
from pprint import pprint

def funkcija (x):
    y= x / (3+ sin(2*x))
    return y

def findX (n):
    x=[0.5*i for i in range(n)]#intervala keisti cia ir mazgu skaiciu tai pat
    return x

def findY (n, x):
    # y[][] is used for difference table 
    # with y[][0] used for input 
    y= [[0 for i in range(n)] 
        for j in range(n)]; 
    for i in range(n):
        y[i][0]= funkcija(x[i])
    return y

# def L4 (x, yMazguMasyvas, xMazguMasyvas):
#     resultatas=yMazguMasyvas[0][0]
#     for i in range(1,5):
#         temp= xLfunkicijoj(x, xMazguMasyvas, i)
#         resultatas= resultatas+ yMazguMasyvas[0][i]* temp

#     return resultatas

# def xLfunkicijoj(x, xn, n):
#     temp= 1
#     for i in range(n-1):
#         temp= (x-xn[i])*temp
#     return temp

# Function to find the product term  
def proterm(i, value, x):  
    pro = 1;  
    for j in range(i):  
        pro = pro * (value - x[j]);  
    return pro;  
  
# Function for calculating  
# divided difference table  
def dividedDiffTable(x, y, n): 
  
    for i in range(1, n):  
        for j in range(n - i):  
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j])); 
    return y; 
  
# Function for applying Newton's  
# divided difference formula  
def applyFormula(value, x, y, n):  
  
    sum = y[0][0];  
  
    for i in range(1, n): 
        sum = sum + (proterm(i, value, x) * y[0][i]);  
      
    return sum;  
  
# Function for displaying divided  
# difference table  
def printDiffTable(y, n):  
  
    for i in range(n):  
        for j in range(n - i):  
            print(round(y[i][j], 4), "\t",  
                               end = " ");  
  
        print("");  
  

# rasti 4 eiles polinoma
# Number of values given 
n = 5
x = findX (n)
y = findY(n,x)
n=5
  
# calculating divided difference table  
y=dividedDiffTable(x, y, n);  
  
# displaying divided difference table  
printDiffTable(y, n);  
  
# value to be interpolated  
value = 7;  
  
# printing the value  
print("\nValue at", value, "is", 
        round(applyFormula(value, x, y, n), 2)) 



tempX = np.asarray(x)
f2 = np.vectorize(funkcija)
# Ln = np.vectorize(L4)

plt.figure()
plt.plot(np.arange(0.0, 10.0, 0.02), f2(np.arange(0.0, 10.0, 0.02)))#funkcijos grafikas
# plt.plot(tempX,y)

# tempX=[0, 0.5, 1, 1.5]
# n=20

# y=dividedDiffTable(x, y, n);  
plt.plot(tempX, applyFormula(tempX, x,y,n),'bo')
# n=5

# y=dividedDiffTable(x, y, n);  
# plt.plot(np.arange(0.0, 10.0, 0.3), applyFormula(np.arange(0.0, 10.0, 0.3), x,y,n))


plt.show()

# # Calculating the forward difference 
# # table 
# for i in range(1, 5): 
#     for j in range(n - i): 
#         y[j][i] = (y[j + 1][i - 1] - y[j][i - 1])/(x[j]-x[j-i]); #i negali buti daugiau 4 KUR DALYBA IS X
  
# # Displaying the forward difference table 
# for i in range(n): 
#     print(x[i], end = "\t"); 
#     for j in range(5): 
#         print(y[i][j], end = "\t"); 
#     print(""); 

# # print(L4(5, y, x))



# # nubraizyti grafika. pazymint mazgus + funkcijos grafika

# # paskaiciuot paklaida bet kuriam taske