import sys

def solve():
    n_count = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))

    b = sorted(a)

    l,r = -1, -1
    for i in range(n_count):
        if a[i] != b[i]:
            if l == -1:
                l = i
            r = i
    if l == -1:
        print("yes")
        print(1, 1)
        return
    
    segment_to_reverse = a[l:r+1]
    segment_to_reverse.reverse()

    potentially_sorted = a[:l] + segment_to_reverse + a[r+1:]
    if potentially_sorted == b:
        print("yes")
        print(l + 1, r + 1)
    else:
        print("no")

solve()