import math
import numpy as np

arr = [(-0.14917819923738845, 0.002040902387923124), (-0.13924049835076222, 0.002040902387923124), (-0.05980036749297862, 0.002040902387923124), (-0.04476750186478564, 0.002040902387923124), (-0.020940876209023532, 0.002040902387923124), (0.12636929323409446, 0.002040902387923124), (-0.0201511155999885, 0.002040902387923124), (-0.05393929568324125, 0.002040902387923124), (-0.1357313746271772, 0.002040902387923124), (-0.0592088992238985, 0.002040902387923124), (-0.020796149064532265, 0.002040902387923124), (-0.11100187715714362, 0.002040902387923124), (-0.049639841945751925, 0.002040902387923124), (-0.07697905104895453, 0.002040902387923124), (-0.2828261624957652, 0.002040902387923124), (-0.08285074790399355, 0.002040902387923124), (0.14464111154274656, 0.002040902387923124), (0.22606685480179028, 0.002040902387923124), (-0.18894124739413976, 0.002040902387923124), (-0.07727045780593302, 0.002040902387923124), (0.09273860863879888, 0.002040902387923124), (0.0680690840645945, 0.002040902387923124), (0.29568049519515044, 0.002040902387923124), (0.08243337870287532, 0.002040902387923124), (0.10354233257439267, 0.002040902387923124), (0.25425023476738073, 0.002040902387923124), (-0.13334635392499788, 0.002040902387923124), (0.028661104221486964, 0.002040902387923124), (0.06332756718730259, 0.002040902387923124), (0.05196876193348896, 0.002040902387923124)]

xValues = [a[0] for a in arr]
def ackleyFunc(xSet):  #xSet: list[float] -> float
    c1 = 20
    c2 = 0.2
    c3 = 2 * math.pi
    n = len(xSet)

    firstSum = 0
    for i in range(0, n):
        firstSum = firstSum + (xSet[i] ** 2)
    firstBlock = -c1 * math.exp(-c2 * math.sqrt(firstSum / n))

    secondSum = 0
    for i in range(0, n):
        secondSum += math.cos(c3 * xSet[i])
    secondBlock = -math.exp(secondSum / n)

    finalResult = firstBlock + secondBlock + c1 + 1
    return finalResult

def ackley_function_range(x_range_array):
  #returns an array of values for the given x range of values
  value = np.empty([len(x_range_array[0])])
  for i in range(len(x_range_array[0])):
    
    #returns the point value of the given coordinate
    part_1 = -0.2*math.sqrt(0.5*(x_range_array[0][i]*x_range_array[0][i] + x_range_array[1][i]*x_range_array[1][i]))
    part_2 = 0.5*(math.cos(2*math.pi*x_range_array[0][i]) + math.cos(2*math.pi*x_range_array[1][i]))
    
    value_point = math.exp(1) + 20 -20*math.exp(part_1) - math.exp(part_2)
    value[i] = value_point
  #returning the value array
  return value

from numpy import abs, cos, exp, mean, pi, prod, sin, sqrt, sum

def ackley( x, a=20, b=0.2, c=2*pi ):
    x = np.asarray_chkfinite(x)  # ValueError if any NaN or Inf
    n = len(x)
    s1 = sum( x**2 )
    s2 = sum( cos( c * x ))
    return -a*exp( -b*sqrt( s1 / n )) - exp( s2 / n ) + a + exp(1)

def run():
    print(ackleyFunc(xValues))
    print(ackley(xValues))