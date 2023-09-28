import picos
import numpy as np

p = picos.Problem()

x = picos.RealVariable('x', (4,4), lower = 0)

c = np.array([],
             [],
             [],
             [])