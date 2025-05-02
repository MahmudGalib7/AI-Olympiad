import sys

def solve():
    """Solves a single test case."""
    n, x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    odd_count = 0
    even_count = 0
    for val in a:
        if val % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    possible = False
    # Iterate through all possible ODD numbers of odd elements we can pick (k)
    # Start from k=1, increment by 2
    for k in range(1, odd_count + 1, 2):
        # Number of even elements needed is x - k
        num_even_needed = x - k

        # Check if we have enough even elements
        # num_even_needed must be non-negative and not exceed available even numbers
        if 0 <= num_even_needed <= even_count:
            # If we can pick k odd elements (k <= odd_count is true due to loop range)
            # and x-k even elements, then it's possible.
            possible = True
            break # Found a valid combination

    if possible:
        print("Yes")
    else:
        print("No")


# Read the number of test cases
t = int(sys.stdin.readline())

# Process each test case
for _ in range(t):
    solve()