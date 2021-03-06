import numpy as np
import random

# The results of simulation
# 132.9311, 133.05556, 133.08348, 133.1026, 132.86512
# 132.94688, 133.0523, 132.82804, 133.08372, 133.1261
#

T=50000
N=20

result = []
for t in range(T):
  population = [i for i in range(1,N+1)]
  samples = random.sample(population,N)
  abs_val = abs(np.diff(samples)).sum()
  result.append(abs_val)
res = sum(result)/T
print(res)