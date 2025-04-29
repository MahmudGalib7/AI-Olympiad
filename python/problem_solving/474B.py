import bisect
import sys

# Faster input reading
input = sys.stdin.readline

def solve():
    # Read number of piles
    n = int(input())
    
    # Read worm counts per pile
    a = list(map(int, input().split()))
    
    # Calculate prefix sums (cumulative worm counts)
    # pile_end_labels[i] stores the label of the last worm in pile i+1
    pile_end_labels = [0] * n
    current_sum = 0
    for i in range(n):
        current_sum += a[i]
        pile_end_labels[i] = current_sum
        
    # Read number of juicy worms
    m = int(input())
    
    # Read juicy worm labels
    q = list(map(int, input().split()))
    
    # Process each query
    results = []
    for worm_label in q:
        # bisect_left finds the insertion point for worm_label,
        # which is the index of the first pile whose end label
        # is >= worm_label.
        pile_index_0_based = bisect.bisect_left(pile_end_labels, worm_label)
        
        # Convert 0-based index to 1-based pile number
        results.append(str(pile_index_0_based + 1))
        
    # Print all results
    print("\n".join(results))

# Run the solver function
solve()