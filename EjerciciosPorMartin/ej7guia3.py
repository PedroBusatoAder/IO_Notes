import scipy as scipy
import numpy as np

def objective(x):
    d1 = np.sqrt((x[0]-5)**2 + (x[1]-10)**2)    
    d2 = np.sqrt((x[0]-10)**2 + (x[1]-5)**2)    
    d3 = np.sqrt((x[0]-0)**2 + (x[1]-12)**2)    
    d4 = np.sqrt((x[0]-12)**2 + (x[1]-0)**2)    
    return(d1 * 200 + d2 * 150 + d3 * 200 + d4 * 300)

bounds =[(0, None), [0,None]]

x0 = [(10,10)]

#opt = scipy.optimize.minizie(f =)



