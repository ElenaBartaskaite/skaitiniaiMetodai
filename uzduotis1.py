import math
import numpy
import matplotlib.pylab
from scipy.misc import derivative


#iteracijuskaitiklis
i=0
#artinys
x=[0]
#tikslumo skaiciavimo parametras
epsilion= 0.0001
q=0
#tikimybe
probability=0
probabilityArray=[0]



#g(x)
def g( x ):
   return math.exp(-x**2)/2
   
#g'(x)
def gDerivative( x ):
   return derivative(g,x)


#g(x)
def f( x ):
   return math.exp(-x**2)-2*x
   
#g'(x)
def fDerivative( x ):
   return derivative(f,x)


#max|g'(x)|
def computeMaxAbsoluteDerivativeValue():
    max_value = float("-inf")
    for x in numpy.arange(0, 0.5, 0.00001):#keiciant range keiciu intervala
        res = abs(gDerivative( x ))
        if max_value < res: max_value = res
    return(max_value)

q=computeMaxAbsoluteDerivativeValue()
probability=((1-q)/q)*epsilion

x.append(g(x[0]))
i+=1
probabilityArray.append((x[i]-x[i-1]))

while(abs(x[i]-x[i-1])>=probability):
    x.append(g(x[i]))
    # matplotlib.pylab.scatter(i, x[i])
    i+=1
    probabilityArray.append(abs(x[i]-x[i-1]))


#printing results
print("lygties sprendinys tislumu ",epsilion)
print(x[-2])
print()
print("skaiciavimo iteraciju lentele")
print("i  ","x[i]                ", "x[i]-x[i-1]")
for n in range(0,len(x)):
    print(n,"  ",x[n], probabilityArray[n])


matplotlib.pylab.plot(range(0,len(x)),x )
matplotlib.pylab.show()



#Niutono metodas

#iteracijuskaitiklis
i=0
#artinys
x=[4]

x.append(x[i]-((f(x[i]))/fDerivative(x[i])))
i+=1
fxArray=[]

while(abs(x[i]-x[i-1])>=probability):
    x.append(x[i]-(((x[i]))/fDerivative(x[i])))#blogai reikia derivative taske x[i] surast ir jos nuline reiksme????
    fxArray.append(f(x[i]))
    i+=1

#printing results
print("niutono metodu")
print("lygties sprendinys tislumu ",epsilion)
print(x[-1])

matplotlib.pylab.plot(range(0,len(x)),x )
matplotlib.pylab.show()
# print()
# print("skaiciavimo lentele")
# print("i  ","f(x[i])                ", "x[i]")
# for n in range(0,len(x)):
#     print(n,"  ",fxArray[n], x[n])