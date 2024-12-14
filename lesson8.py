# -------------------------------------------------
# n = int(input('Enter number: '))
# for i in range(n):
#     for j in range(2 * n - 1):
#         if j < (2 * n - 1) // 2 - i or j > (2 * n - 1) // 2 + i:
#            print(' ', end='')
#         else:
#             print('#', end='')
#     print()
# -------------------------------------------------
# n = int(input("Please enter a number: "))
# size = n * 2 - 1
# middle = size // 2
# current_number = 1
# for i in range(n):
#     for j in range(size):
#         if middle - i <= j <= middle + i:
#             if (j - (middle - i)) % 2 == 0:  
#                 print(f"{current_number:>2}", end="")
#                 current_number += 2  
#             else:
#                 print(" ", end="")  
#         else:
#             print(" ", end="")  
#     print() 
# -------------------------------------------------
# 'p'
# 'py'
# 'pyt'
# 'pyth'
# 'pytho'
# 'python'
# 'pytho'
# 'pyth'
# 'pyt'
# 'py'
# 'p'
# text = 'python'
# for i in range(1, len(text)):
#     print(text[:i])
# for i in range(len(text), 0, -1):
#     print(text[:i])
# -------------------------------------------------
# text1 = 'abc'
# text2 = '123'
# text3 = 'defakjsalksla'
# for i, j, k in zip(text1, text2, text3):
#     print(i, j, k)
# -------------------------------------------------
# if -3:
#     print('ok')
# -------------------------------------------------
# text = 'ssbbsbsbsssssssbs'
# temp_count = 1
# max_count = 0
# for i in range(0, len(text) - 1):
#     if text[i] == text[i + 1]:
#         temp_count += 1
#     else:
#         if temp_count > max_count:
#             max_count = temp_count
#             temp_count = 1
#         else:
#             temp_count = 1
# print(max_count) 
# -------------------------------------------------
# text = 'ssbbsbsbsssssssbs'
# new_text = 's' * len(text)
# while new_text not in text:
#     new_text = new_text[:-1]
# print(len(new_text))
# -------------------------------------------------
# n = int(input('Enter n: '))
# summ = 0
# for i in range(n + 1):
#     summ += (-1) ** i * 2 ** (-i)
# print(summ)
# -------------------------------------------------
# x = int(input('Enter x:  '))
# res_1 = 1
# res_2 = 1
# for i in range(1, 65):
#     if i % 2 != 0:
#         res_1 *= (x - i)
#     else:
#         res_2 *= (x - i)
# print(res_1 / res_2)
# -------------------------------------------------

