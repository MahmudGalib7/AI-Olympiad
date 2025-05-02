a, b = map(int, input().split())
hours = a
burned = a

while burned >= b:
    new_candles = burned // b
    hours += new_candles
    burned = burned % b + new_candles
print(hours)
