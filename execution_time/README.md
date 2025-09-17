## Measuring Execution Time in Python ⏱️

When testing performance, it’s useful to know how long a piece of code takes to run.  
Here are several ways to measure execution time in Python:

---

### 1. `time.perf_counter()`  
Best for **precise elapsed time measurements**.

```python
from time import perf_counter

start = perf_counter()
for i in range(10_000_000):
    pass
end = perf_counter()

print(f"Elapsed time: {end - start:.4f} seconds")

time.time() - Simpler. Good for longer tasks:

import time

start = time.time()
time.sleep(2)
end = time.time()

print(f"Elapsed time: {end - start:.4f} seconds")

timeit module - Best for benchmarking small code snippets:

import timeit

execution_time = timeit.timeit("sum(range(100))", number=1_000_000)
print(f"Execution time: {execution_time:.4f} seconds")


Context Manager:

from time import perf_counter
from contextlib import contextmanager

@contextmanager
def timer():
    start = perf_counter()
    yield
    end = perf_counter()
    print(f"Elapsed: {end - start:.4f} sec")

with timer():
    sum([i for i in range(1_000_000)])

