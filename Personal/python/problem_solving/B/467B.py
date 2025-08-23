import sys

# Faster input reading
input = sys.stdin.readline

def solve():
    n, m, k = map(int, input().split())
    
    players_armies = []
    for _ in range(m):
        players_armies.append(int(input()))
        
    fedor_army = int(input())
    
    friend_count = 0
    
    for player_army in players_armies:
        diff = player_army ^ fedor_army
        
        set_bits_count = bin(diff).count('1')
        

        if set_bits_count <= k:
            friend_count += 1
            
    print(friend_count)

# Run the solver function
solve()