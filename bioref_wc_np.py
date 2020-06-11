"""
f1 = liquid intlet, f2 = liquid outlet
f3 = gas inlet, f4 = gas outlet

1-water, 2-ammonia, 3-nitrogen, 4-hydrogen

wij- mass fraction of component i in stream j
mw-molecular weight matrix
"""
import numpy as np
mw = np.array([18, 17, 2, 28])
w3 = np.zeros((4,1))
w4 = np.zeros((4,1))
R = np.divide(np.multiply(3,mw[2]),mw[3])
print(R)
w4 = R*w3
w = np.array([[1, 0.99, 0, 0], [0, 0.01, 0.1, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
print(w)
f = np.array([[200], [0], [100], [0]])
print(f)

null = np.array([[0], [0], [0], [0]])
rhs = null
unit = np.array([[1], [1], [1], [1]])


ans = np.linalg.solve(w,f)
print(ans)

