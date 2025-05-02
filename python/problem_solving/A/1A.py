n, m, a = map(int, input().split())
flagstones_length = (n+a-1) // a
flagstones_width = (m+a-1) // a
print(flagstones_width * flagstones_length)