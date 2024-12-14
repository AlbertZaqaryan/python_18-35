# import random


# user_points = 0
# pc_points = 0
# while True:
#     if user_points == 2:
#         print('Win user')
#         break
#     elif pc_points == 2:
#         print('Win pc')
#         break
#     pc = random.choice(('Rock', 'Paper', 'Scissors'))
#     user = input('Enter Rock or Paper or Scissors:  ')
#     if (user == 'Rock' and pc == 'Scissors') or (user == 'Paper' and pc == 'Rock') or (user == 'Scissors' and pc == 'Paper'):
#         user_points += 1
#     elif (pc == 'Rock' and user == 'Scissors') or (pc == 'Paper' and user == 'Rock') or (pc == 'Scissors' and user == 'Paper'):
#         pc_points += 1

# ---------------------------------------------------------  
# x = int(input('Enter number: '))
# print('Good' if x == 5 else 'Bad')
# ---------------------------------------------------------  
# for i in 'abc':
#     for j in range(1, 4):
#         print(i, j, end=' ')
#     print()

# ---------------------------------------------------------  
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f'{i * j:>4}', end='')
#     print()
# ---------------------------------------------------------  
# for i in range(0, 6):
#     for j in range(0, 11, 2):
#         print(f'{i + j:>3}', end='')
#     print()

# ---------------------------------------------------------  
# n = int(input('Enter n: '))
# for i in range(1, n + 1):
#     for _ in range(i):
#         print(i, end=' ')
#     print()
# ---------------------------------------------------------  
# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if j == 0 or j == n:
#             print('|', end='')
#         elif i == 0 or i == n:
#             print('-' * 2, end='')
#         else:
#             print(' ' * 2, end='')
#     print()
# ---------------------------------------------------------  
# n = int(input('Enter n: '))
# for i in range(n + 1):
#     for j in range(n + 1):
#         if n == i + j or i == j:
#             print('^', end='')
#         else:
#             print(' ', end='')
#     print()
# ---------------------------------------------------------  
# n = int(input('Enter number: ')) # 17
# for i in range(2, int(n ** 0.5) + 1):
#     if n % i == 0:
#         print(False)
#         break
# else:
#     print(True)


# n = int(input('Enter number: ')) # 17
# k = True
# for i in range(2, n):
#     if n % i == 0:
#         k = False

# if k == True:
#     print('Parz')
# else:
#     print('Baxadryal')


