# Bit Wise Operators

a = 7  # In binary: 111
b = 5  # In binary: 101

# Print binary representations of a and b
print("Binary representations:")
print(bin(a)[2:])  # Output: 111
print(bin(b)[2:])  # Output: 101
print("------")

# Bitwise AND
result_and = a & b  # In binary: 101 (which is 5 in decimal)
print("Bitwise AND:")
print(bin(result_and)[2:])  # Output: 101
print(f"{a} & {b} = {result_and}")  # Output: 7 & 5 = 5
print("------")

# Bitwise OR
result_or = a | b  # In binary: 111 (which is 7 in decimal)
print("Bitwise OR:")
print(bin(result_or)[2:])  # Output: 111
print(f"{a} | {b} = {result_or}")  # Output: 7 | 5 = 7
print("------")

# Bitwise XOR
result_xor = a ^ b  # In binary: 010 (which is 2 in decimal)
print("Bitwise XOR:")
print(bin(result_xor)[2:])  # Output: 10
print(f"{a} ^ {b} = {result_xor}")  # Output: 7 ^ 5 = 2
print("------")

# Bitwise NOT
result_not_a = ~a  # In binary: ...11111000 (which is -8 in decimal)
print("Bitwise NOT:")
print(bin(result_not_a)[2:])  # Output: -1000
print(f"~{a} = {result_not_a}")  # Output: ~7 = -8
print("------")

# Left Shift
result_left_shift = a << 2  # In binary: 11100 (which is 28 in decimal)
print("Left Shift:")
print(bin(result_left_shift)[2:])  # Output: 11100
print(f"{a} << 2 = {result_left_shift}")  # Output: 7 << 2 = 28
print("------")

# Right Shift
result_right_shift = a >> 2  # In binary: 1 (which is 1 in decimal)
print("Right Shift:")
print(bin(result_right_shift)[2:])  # Output: 1
print(f"{a} >> 2 = {result_right_shift}")  # Output: 7 >> 2 = 1