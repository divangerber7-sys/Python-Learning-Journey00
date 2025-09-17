"""
Lesson: Measuring Execution Time in Python
------------------------------------------
This script demonstrates different ways to measure how long
a block of code takes to execute.
"""

import time
import timeit
from time import perf_counter
from contextlib import contextmanager

# 1. Using time.perf_counter() (high resolution)
print("=== perf_counter() ===")
start = perf_counter()
for i in range(10_000_000):
    pass
end = perf_counter()
print(f"Elapsed time: {end - start:.4f} seconds\n")


# 2. Using time.time() (system clock, less precise)
print("=== time.time() ===")
start = time.time()
time.sleep(1)  # simulate long operation
end = time.time()
print(f"Elapsed time: {end - start:.4f} seconds\n")


# 3. Using timeit module (best for small snippets)
print("=== timeit ===")
execution_time = timeit.timeit("sum(range(100))", number=1_000_000)
print(f"Execution time (timeit): {execution_time:.4f} seconds\n")


# 4. Using a custom context manager (clean style)
print("=== context manager ===")

@contextmanager
def timer():
    start = perf_counter()
    yield
    end = perf_counter()
    print(f"Elapsed: {end - start:.4f} sec")

with timer():
    sum([i for i in range(1_000_000)])
