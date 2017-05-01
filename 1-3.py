import numpy as np
import random

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