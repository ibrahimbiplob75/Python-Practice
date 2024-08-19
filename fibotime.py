import time
from functools import cache

@cache
def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


start = time.time()
for i in range(37):
    print(i, fibo(i))
end=time.time()

total=(end-start)*1000
print(total)

# with out cache time taken 3471.5774059295654
# with cache time taken 0.2722740173339844