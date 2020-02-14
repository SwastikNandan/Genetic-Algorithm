import numpy as ny
import random
import math
from matplotlib import pyplot as plt
from random import randint
x=ny.linspace(-.5,1,20000)
y=[None]*20000
tuple_list=[None]*20000
for i in range(20000):
    y[i]=x[i]*math.sin(3.14*10*x[i])+1
    tup=(y[i],x[i])
    tuple_list[i]=tup
ordered_tuple=sorted(tuple_list, key= lambda x: x[0], reverse=True)
m=ordered_tuple[0][0]
n=ordered_tuple[0][1]
print (m)
print (n)
