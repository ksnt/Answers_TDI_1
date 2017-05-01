import numpy as np
import random

# Simulation result (I just did run this program many times)
# 17.5657752412, 17.4920228255, 17.4964793138, 17.4930030729, 17.5605304392
# 17.5422113598, 17.5419766711, 17.4951097404, 17.4555344357, 17.4493655531
# The average is 17.50920087

T=100000
N=20

result = []
for t in range(T):
  population = [i for i in range(1,N+1)]
  samples = random.sample(population,N)
  abs_val = abs(np.diff(samples)).sum()
  result.append(abs_val)
res = np.std(result)
print(res)