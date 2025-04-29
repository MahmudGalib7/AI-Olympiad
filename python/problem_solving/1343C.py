def solve():
    n = int(input())
    array = list(map(int, input().split()))
    
    # Initialize result and current segment
    max_sum = 0
    current_max = array[0]
    current_sign = 1 if array[0] > 0 else -1
    
    for i in range(1, n):
        # Get sign of current element
        sign = 1 if array[i] > 0 else -1
        
        # If same sign as current segment, update max value in segment
        if sign == current_sign:
            current_max = max(current_max, array[i])
        # If different sign, add previous max to result and start new segment
        else:
            max_sum += current_max
            current_max = array[i]
            current_sign = sign
    
    # Add the last segment's max
    max_sum += current_max
    return max_sum

t = int(input())
for _ in range(t):
    print(solve())