# def fibonacci(num):
#     if num <= 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibonacci(num - 1) + fibonacci(num - 2)

# num = int(input())
# print(fibonacci(num))

# def divisors(n):
#     divs = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             divs.append(i)
#             if i != n // i: 
#                 divs.append(n // i)
#     return sorted(divs)

# n = int(input())
# for i in divisors(n):
#     print(i)

# def solve(n):
#     if n >= 5 and (n - 2) % 3 == 0:
#         print("Yes")
#     else:
#         print("No")

# while True:
#     try:
#         n_input = int(input())
#         solve(n_input)
#     except EOFError:
#         break
#     except ValueError:
#         print("No")
#     except Exception:
#         print("No")
#         break


# import sys

# def count_extracted_passwords(s):
#     n = len(s)
#     password_count = 0
#     start_index = 0

#     while start_index < n:
#         has_lower = False
#         has_upper = False
#         has_digit = False
#         found_password_in_segment = False

#         for current_index in range(start_index, n):
#             char = s[current_index]

#             if 'a' <= char <= 'z':
#                 has_lower = True
#             elif 'A' <= char <= 'Z':
#                 has_upper = True
#             elif '0' <= char <= '9':
#                 has_digit = True


#             if has_lower and has_upper and has_digit:
#                 password_count += 1
#                 start_index = current_index + 1
#                 found_password_in_segment = True
#                 break 

        
#         if not found_password_in_segment:
#             break

#     return password_count

# for line in sys.stdin:
#     input_string = line.strip()
#     if input_string:
#         result = count_extracted_passwords(input_string)
#         print(result)

# import sys

# def solve():
#     try:
#         a, b, c = map(int, sys.stdin.readline().split())
#         max_h = max(a, b, c)
#         sum_of_all = a + b + c
#         sum_of_two_smaller = sum_of_all - max_h

#         if sum_of_two_smaller >= max_h:
#             print("Yes")
#         else:
#             print("No")

#     except ValueError:
#         # Handle potential errors if input is not three integers
#         print("No")
#     except Exception:

#         print("No")

# try:
#     t = int(sys.stdin.readline())
#     for _ in range(t):
#         solve()

# except ValueError:
#     pass 
# except Exception:
#     pass
