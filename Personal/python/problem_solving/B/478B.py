n, m = map(int, input().split())

min_pair_frnd = 0
max_pair_frnd = 0

def pairs(k):
    if k < 2:
        return 0
    return k * (k - 1) // 2

k_large = n-m+1
max_pair_frnd = pairs(k_large)

base_size = n // m
remainder = n % m

pairs_base = pairs(base_size)
count_base = m - remainder

pairs_extra = pairs(base_size + 1)
count_extra = remainder

min_pair_frnd = count_base * pairs_base + count_extra * pairs_extra

print(min_pair_frnd, max_pair_frnd)