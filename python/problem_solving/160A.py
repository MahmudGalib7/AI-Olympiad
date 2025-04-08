t = int(input())
arr = list(map(int, input().split()))


def min_coins_to_take(n, coins):
    total_sum = sum(coins)
    coins.sort(reverse=True)

    picked_sum = 0
    num_coins = 0

    for coin in coins:
        picked_sum += coin
        num_coins += 1
        if picked_sum > total_sum / 2:
            break

    return num_coins


print(min_coins_to_take(t, arr))
