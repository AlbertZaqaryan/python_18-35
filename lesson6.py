# --------------------------------------------------------------------
# import math

# for i in range (0,40):
#     a=round(((1+(math.sqrt(5)))**i-(1-(math.sqrt(5)))**i)/((2**i)*math.sqrt(5)))
#     print(a)
# --------------------------------------------------------------------
# a, b = 0, 1
# print(a, end=', ')
# for i in range(40):
#     a, b = b, a + b
#     print(a, end=', ')
# --------------------------------------------------------------------
# text = input('Enter text:  ')
# number_count = 0
# letter_count = 0
# char_count = 0
# for i in text:
#     if i.isdigit():
#         number_count += 1
#     elif i.isalpha():
#         letter_count += 1
#     else:
#         char_count += 1
# # print(text, "ka\n", number_count, "tiv, ", letter_count, "tar, ",char_count, "char")
# print(f'{text} textum ka\n{number_count}(tiv), {letter_count}(tar) ev {char_count}(nish)')
# --------------------------------------------------------------------
# for i in range(5, 26, 5):
#     price = i - 0.05
#     print(f'real price = ${price} - discount price ${round(price - price * 60 / 100, 2)}')
# --------------------------------------------------------------------
# for i in range(0, 101, 10):
#     print(f'{i}(C) = {i * 1.8 + 32}(F)')
# --------------------------------------------------------------------
# pi = 3
# a, b, c = 2, 3, 4
# for i in range(0, 15):
#     pi += (4 / (a * b * c)) * ((-1) ** i)
#     a, b, c = a + 2, b + 2, c + 2
# print(pi)
# --------------------------------------------------------------------


# text=input("please input text: ").lower().replace(' ', '')
# length=int(input("please input the symbol cout: "))
# direction=int(input("please enter 1 or -1: "))
# for i in text:
#     if direction==1:
#         if ord(i)>=ord("a") and ord(i)<=ord("z")-length:
#             i=ord(i)+length
#             print(chr(i), end='')
#         else:
#             i=ord(i)+length-ord("z")+(ord("a")-1)
#             print(chr(i), end='')
#     else:
#         if ord(i)>=ord("a")+length and ord(i)<=ord("z"):
#             i=ord(i)-length
#             print(chr(i), end='')
#         else:
#             i=ord(i)-length-ord("a")+(ord("z")+1)
#             print(chr(i), end='')

# print(ord('ա'))
# print(chr(76))
# --------------------------------------------------------------------


# text = input('Enter text:  ').replace(' ', '')
# print(text == text[::-1])
# --------------------------------------------------------------------
# import random

# first_number = random.randint(1, 100)
# print(first_number)
# for _ in range(99):
#     random_number = random.randint(1, 100)
#     if random_number > first_number:
#         print(f'{random_number} --- update')
#         first_number = random_number
#     else:
#         print(random_number)
# --------------------------------------------------------------------
# for i in range(1, 7):
#     print(i)
# --------------------------------------------------------------------
# i = 1
# while i < 7:
#     print(i)
#     i += 1
# --------------------------------------------------------------------
# while True:
#     number = int(input('Enter number: '))
#     if number == 28:
#         break
#     else:
#         print(number)
# --------------------------------------------------------------------
# sum_ = 0
# count_ = 0
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     else:
#         sum_ += number
#         count_ += 1
# print(f'Avg ->  {round(sum_ / count_, 2)}')
# --------------------------------------------------------------------
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         number = int(number)
#         print(number)
# --------------------------------------------------------------------
# kassa = 0
# while True:
#     age = input('Enter your age: ')
#     if age == '':
#         print(kassa)
#         break
#     else:
#         age = int(age)
#         if 2 >= age >= 0:
#             continue
#         elif 12 >= age > 2:
#             kassa += 14
#         elif 65 >= age > 12:
#             kassa += 24
#         else:
#             kassa += 18 
# --------------------------------------------------------------------
# number = int(input('Enter number: '))
# bin_code = ""
# while number > 1:
#     bin_code += str(number % 2) 
#     number //= 2
# print('1' + bin_code[::-1])
# --------------------------------------------------------------------
# bin_code = input('Enter binary code:  ')
# bin_code = bin_code[::-1]
# number = 0
# for i in range(0, len(bin_code)):
#     number += 2 ** i * int(bin_code[i])
# print(number)
# --------------------------------------------------------------------
# bin_code = input('Enter binary code:  ')
# number = 0
# for i in range(len(bin_code) - 1, -1, -1):
#     number += 2 ** (len(bin_code) - 1 - i) * int(bin_code[i])
# print(number)
# --------------------------------------------------------------------
# bin_code = input('Enter binary code:  ')
# bin_code = bin_code[::-1]
# number = 0
# i = 0
# while i < len(bin_code):
#     number += 2 ** i * int(bin_code[i])
#     i += 1
# print(number)
# --------------------------------------------------------------------
# import random

# for _ in range(10):
#     count_O = 0
#     count_P = 0
#     s = ""
#     while True:
#         if count_O == 3 or count_P == 3:
#             print(s)
#             break
#         random_ = random.choice('OP')
#         if random_ == 'O':
#             s += random_
#             count_O += 1
#             count_P = 0
#         else:
#             s += random_
#             count_P += 1
#             count_O = 0
# --------------------------------------------------------------------

