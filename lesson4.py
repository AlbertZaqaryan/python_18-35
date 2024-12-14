# print(10 > 3)

# if 10 < 3: # True
#     print('good')

# if

# elif

# elif

# elif

# else
    
# if

# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))
# if a > b:
#     print('a is max!!')
# elif a == b:
#     print('equal')
# else: 
#     print('b is max!!')


# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))

# x = int(input('Enter number1:  '))
# y = int(input('Enter number2:  '))

# if a > b:
#     print('a is max')
# elif a == b:
#     print('equal')
# else:
#     print('b is max')

# if x > y:
#     print('x is max')
# elif x == y:
#     print('equal')
# else:
#     print('y is max')
    


# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))

# x = int(input('Enter number1:  '))
# y = int(input('Enter number2:  '))


# if a > b:
#     pass
# if x > y:
#     pass
# else:
#     pass


# ----------------------------------------------------

# x = input('Enter letter: ')
# if x.isdigit():
#     print('Number')
# elif x.isalpha():
#     print('Letter')
# else:
#     print('Xary')

# ----------------------------------------------------
# x = input('Enter letter: ')
# if x.isupper():
#     print('Upper')
# elif x.islower():
#     print('Lower')
# elif x.isdigit():
#     print('ERROR ENTER ONLY LETTERS')
# else:
#     print('Lower and Upper')
# ----------------------------------------------------
# number = int(input('Enter number: '))
# if number % 2 == 0:
#     print('even')
# else:
#     print('odd')
# ----------------------------------------------------
# tar = input('Mutqagreq anglereni inch vor tar:  ').lower()
# anglereni_dzaynavorner = 'aeiou'
# if tar in anglereni_dzaynavorner:
#     print('dzaynavor')
# else:
#     print('baxadzayn')
# ----------------------------------------------------
# year = int(input('Enter year: '))
# if year % 4 == 0:
#     print('Leep')
# else:
#     print('No Leep')
# ----------------------------------------------------
# age = int(input('Enter age:  '))
# if age >= 18:
#     drink = input('Enter your order: ').lower()
#     if drink == 'vodka':
#         print('Bad drink')
#     else:
#         print('Good drink')
# else:
#     print('🤬')
#     pechenin = input('Drink chka qez yntri pecheni: ')
#     if pechenin == 'daronik':
#         print('Lav tarberak')
# ----------------------------------------------------
# import random
# import time


# name = input('Enter your name: ')
# print(f'Hello {name} welcome the best GAME')
# ready = input('Ready?\nYes for continue No for exit\n\t====>').lower()
# if ready == 'yes':
#     print(3)
#     time.sleep(2)
#     print(2)
#     time.sleep(2)
#     print(1)
#     time.sleep(2)
#     print(f'{name} your game is starting...')
#     pc_number = random.randint(0, 5)
#     user_number = int(input('Enter number in range(0, 5):  '))
#     pc_points = 0
#     user_points = 0
#     if user_number == pc_number: # round 1 | user = 1, pc = 0
#         user_points += 1
#         print(f'---> WIN USER <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#         pc_number = random.randint(0, 5)
#         user_number = int(input('Enter number in range(0, 5):  '))
#         if user_number == pc_number: # round 2 | user = 2, pc = 0 END GAME WIN USER
#             user_points += 1
#             print(f'---> WIN USER <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#             print('#################### END GAME WIN USER ########################')
#         else: # round 2 | user = 1, pc = 1
#             pc_points += 1
#             print(f'---> WIN PC <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#             pc_number = random.randint(0, 5)
#             user_number = int(input('Enter number in range(0, 5):  '))
#             if user_number == pc_number: # round 3 | user = 2, pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'---> WIN USER <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('#################### END GAME WIN USER ########################')
#             else: # round 3 | user = 1, pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'---> WIN PC <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('#################### END GAME WIN PC ########################')
#     else: # round 1 | user = 0, pc = 1
#         pc_points += 1
#         print(f'---> WIN PC <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#         pc_number = random.randint(0, 5)
#         user_number = int(input('Enter number in range(0, 5):  '))
#         if user_number == pc_number: # round 2 | user = 1, pc = 1
#             user_points += 1
#             print(f'---> WIN USER <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#             pc_number = random.randint(0, 5)
#             user_number = int(input('Enter number in range(0, 5):  '))
#             if user_number == pc_number: # round 3 | user = 2, pc = 1 END GAME WIN USER
#                 user_points += 1
#                 print(f'---> WIN USER <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('#################### END GAME WIN USER ########################')
#             else: # round 3 | user = 1, pc = 2 END GAME WIN PC
#                 pc_points += 1
#                 print(f'---> WIN PC <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#                 print('#################### END GAME WIN PC ########################')
#         else: # round 2 | user = 0, pc = 2 END GAME WIN PC
#             pc_points += 1
#             print(f'---> WIN PC <---\nuser = {user_number}, pc = {pc_number}\nuser points = {user_points}, pc points = {pc_points}')
#             print('#################### END GAME WIN PC ########################')
# else:
#     print('----------------------------- EXIT -----------------------------')
# ----------------------------------------------------


# dog_age = int(input('Enter age: '))
# if dog_age <= 2:
#     print(f'Human age = {dog_age * 10.5}')
# else:
#     print(f'Human age = {(dog_age - 2) * 4 + 21}')


# cord = input('Enter cord:  ')
# let = cord[0]
# number = int(cord[1])
# if (let in 'aceg' and number % 2 != 0) or (let in 'bdfh' and number % 2 == 0):
#     print('black')
# else:
#     print('white')

# 'A4' 440
# 'A5' 440 * 2
# 'A6' 440 * 2 * 2
# 'A3' 440 / 2
# 'A2' 440 / 2 / 2
