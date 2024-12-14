# import random

# pc_followers = random.randint(1, 100000)
# user_followers = int(input('Enter your followers count:  '))
# if pc_followers >= user_followers + user_followers * 20 / 100:
#     print('Pc is blogger')
# elif user_followers >= pc_followers + pc_followers * 20 / 100:
#     print('User is blogger')
# else:
#     print('Blogger none')
# ----------------------------------------------------------------
# import random

# user = input('Enter Rock or Paper or Scissors:  ')
# pc = random.choice(('Rock', 'Paper', 'Scissors'))
# if (user == 'Rock' and pc == 'Paper') or (user == 'Paper' and pc == 'Scissors') or (user == 'Scissors' and pc == 'Rock'):
#     print('Win pc')
# elif (pc == 'Rock' and user == 'Paper') or (pc == 'Paper' and user == 'Scissors') or (pc == 'Scissors' and user == 'Rock'):
#     print('Win user')
# else:
#     print('Equal')
# ----------------------------------------------------------------
# ------------------------ for loop ------------------------------
# ----------------------------------------------------------------
# for i in range(1, 15):
#     print(i)
# ----------------------------------------------------------------

# range(1, 10)
# (1, 2, 3, 4, 5, 6, 7, 8, 9)
# ----------------------------------------------------------------

# for i in range(5, 15, 2):
#     print(i)
# ----------------------------------------------------------------

# for i in range(10, -1, -5):
#     print(i)
# ----------------------------------------------------------------

# (10, -1, -5)
# 10, 5, 0
# ----------------------------------------------------------------

# print(range(10))

# n1 = 12
# n2 = 15


# for i in range(1, 10):
#     if i == 7:
#         break
#     else:
#         print(i)
# ----------------------------------------------------------------


# for i in range(14, 100):
#     if i == 7:
#         print('7 y tranq')
#         continue
#     else:
#         print(i)
# ----------------------------------------------------------------


# n = 74561
# for i in range(n):
#     print(i)
# ----------------------------------------------------------------


# n = int(input('Enter interval: '))
# count = 0
# for i in range(n):
#     if i % 5 == 0:
#         count += 1
# print(count)
# ----------------------------------------------------------------


# for i in range(14, 100):
#     if i == 7:
#         print('Gta banalin')
#         break
# else:
#     print('Chgta banalin')
# ----------------------------------------------------------------


# payman = True
# for i in range(1, 100):
#     if i == 7:
#         print('Gta banalin')
#         payman = False
#         break

# if payman == True:
#     print('Chgta')
# ----------------------------------------------------------------


# text = 'python 3.12'
# for Ճ in text:
#     print(Ճ)

# ----------------------------------------------------------------

# text = input('Enter text: ')
# count_number = 0
# count_letter = 0
# count_char = 0
# for i in text:
#     if i.isdigit():
#         count_number += 1
#     elif i.isalpha():
#         count_letter += 1
#     else:
#         count_char += 1
# print(f'int {text} text have {count_letter} count letter, {count_number} count digit, {count_char} count char') 
# ----------------------------------------------------------------


# text = 'python'
#       012345
# for i in text:
#     print(i)
# for i in range(0, len(text)):
#     print(text[i])
# ----------------------------------------------------------------

# text = 'python programming'
# for i in range(0, len(text)):
#     if text[i] == 'o':
#         print(i)
# ----------------------------------------------------------------

# text = 'python'
# for i in range(0, len(text) - 2):
#     print(text[i] + text[i + 1] + text[i + 2])
# ----------------------------------------------------------------

# n1 = int(input('Enter number1:  '))
# n2 = int(input('Enter number2:  '))
# if n1 > n2:
#     for i in range(n1, n1 * n2 + 1, n1):
#         if i % n2 == 0:
#             print(i)
#             break
# elif n2 > n1:
#     for i in range(n2, n1 * n2 + 1, n2):
#         if i % n1 == 0:
#             print(i)
#             break
# else:
#     print(n1)
# ----------------------------------------------------------------


# n1 = int(input('Enter number1:  '))
# n2 = int(input('Enter number2:  '))
# for i in range(max(n1, n2), n1 * n2 + 1, max(n1, n2)):
#     if i % min(n1, n2) == 0:
#         print(i)
#         break
# ----------------------------------------------------------------

# n = int(input('Enter number: '))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)
# ----------------------------------------------------------------
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz-Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)
# ----------------------------------------------------------------
# number = int(input('Enter number: '))
# summ = 0
# for i in str(number):
#     summ += int(i)
# print(summ)
# ----------------------------------------------------------------
# number = int(input('Enter number: '))
# number = str(number)
# x = int(number[::-1]
# ----------------------------------------------------------------
