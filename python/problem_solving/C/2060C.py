from collections import Counter

# Number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    # Read n (number of elements) and k (target sum for pairs)
    n, k = map(int, input().split())

    # Read the numbers on the board
    a = list(map(int, input().split()))

    # Count frequencies of each number
    freq = Counter(a)

    # Initialize the score (number of valid pairs)
    score = 0

    # Try to pair each number with its complement (k - number)
    for x in list(freq.keys()):
        target = k - x

        # If there's a valid pair (x, target), we can pair them
        if target in freq:
            if x == target:
                # If x == target, we can only form pairs from count[x] // 2
                score += freq[x] // 2
            else:
                # Otherwise, we can form min(freq[x], freq[target]) pairs
                score += min(freq[x], freq[target])

            # After pairing, remove both x and target from the counter
            del freq[x]
            del freq[target]

    # Output the score for the current test case
    print(score)
