import pandas as pd
import numpy as np
 #creating metrics
A=np.array([
    [1,2],
  [3,4]
]
)
B=np.array([
    [5,6],[7,8]
])

#sum
print("sum of metrics:")
print(A+B)

#difference
print("difference of metrics")
print(A-B)
# Transpose 
print("Transpose of A:")
print(A.T)

print("transpose of B:")
print(B.T)

print("product of A and B:")
print(A@B)

