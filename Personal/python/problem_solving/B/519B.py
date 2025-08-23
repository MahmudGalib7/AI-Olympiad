n = int(input())
first_compilation = list(map(int, input().split()))
second_compilation = list(map(int, input().split()))
third_compilation = list(map(int, input().split()))

sum_first = sum(first_compilation)
sum_second = sum(second_compilation)
sum_third = sum(third_compilation)

print(abs(sum_first - sum_second))
print(abs(sum_second - sum_third))