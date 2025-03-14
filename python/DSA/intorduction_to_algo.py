import random
import time 

# Algo1
def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x-y))

    return result

# Algo2
def max_Diff(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]

# Algo3
def Max_diff(numbers):
    return max(numbers) - min(numbers)

n = 1000
print("n:", n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
result = Max_diff(numbers)
end_time = time.time()

print("result:", result)
print("time:", round(end_time - start_time, 2), "s")

