import numpy as np
import math 
def Func(i):
    M=6
    g=((math.exp(math.cos(i)**M))*(math.sin(i**2)/math.cos(i**2)))
    f=((M/9)*i)+i**(3/2)
    func=abs(g/f)
    print(np.log(func)/np.log(2*i))
Func(1)
Func(5)
Func(10)
Func(100)

import matplotlib.pyplot as plt
plt.axis([0,15,0,43])
plt.title(' plot')
plt.plot([0,1,2,3,4,6,7,8,9,10,11,12,13,14,15],[0,3.92,5.52,8.41,11.02,13.54,16.48,19.98,22.56,25.30,27.87,30.36,35.64,38.31,41.73],'ro')
plt.show()