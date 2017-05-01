import numpy as np
import random

T=1000000
N=10

result = []
for t in range(T):
  population = [i for i in range(1,N+1)]
  samples = random.sample(population,N)
  abs_val = abs(np.diff(samples)).sum()
  result.append(abs_val)
res = np.std(result)
print(res)