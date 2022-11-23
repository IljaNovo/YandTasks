import time

def is_simple(number):
    if number % 2 == 0 or number % 3 == 0:
        return False
    iterations = int(number ** (0.5))
    for i in range(2, iterations + 1):
        if number % i == 0:
            return False
    return True

start_time = time.time()

n = 5000

print(2, 3, 5, 7, end="")

for i in range(10, n):
    if is_simple(i):
       print(",", i, end="")

print("\ntime %s" % (time.time() - start_time))
