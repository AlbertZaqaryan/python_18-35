# -------------------------------------------------------
# try:
#     x = int(input("Enter number1:  "))
#     y = int(input("Enter number2:  "))
#     print(x / y)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Enter only numbers')
# -------------------------------------------------------
# try:
#     x = int(input("Enter number1:  "))
#     y = int(input("Enter number2:  "))
#     print(x / y)
# except Exception as ex:
#     print(ex.__class__.__name__)
# -------------------------------------------------------
# try:
#     x = int(input("Enter number1:  "))
#     y = int(input("Enter number2:  "))
#     print(x / y)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Enter only numbers')
# else:
#     print('Norm')
# -------------------------------------------------------
# try:
#     x = int(input("Enter number1:  "))
#     y = int(input("Enter number2:  "))
#     print(x / y)
# except ZeroDivisionError:
#     print('Cannot divide by zero')
# except ValueError:
#     print('Enter only numbers')
# finally:
#     print('Norm')
# -------------------------------------------------------
# name = 'Sergo'
# if name == 'Sergo':
#     raise Exception('Pink football shoes exception')
# -------------------------------------------------------
# f = open('armenian_football.txt', 'a')
# print(f.read())
# f.write('\nNo Sergo')
# -------------------------------------------------------
# PATH = 'armenian_football.txt'
# file = open(PATH, 'r')
# names = file.readlines()
# for i in names.copy():
#     if 'Sergo' in i:
#         names.remove(i)
# file.close()
# file = open(PATH, 'w')
# for i in names:
#     file.write(i)
# file.close()
# print(file.read().split('\n'))
# -------------------------------------------------------

# PATH = 'armenian_football.txt'
# with open(PATH, 'r') as file:
#     print(file.read())
# -------------------------------------------------------
# def head(filename):
#     try:
#         with open(filename, 'r') as file:
#             x = file.read()
#         x = x.split('\n')
#         return x[:5]
#     except FileNotFoundError:
#         return "No file"
# filename = input('Enter filename: ')
# print(head(filename))
# -------------------------------------------------------
# with open('Sergo.txt', 'w') as file:
#     file.write('Norm person')
# -------------------------------------------------------
# def cat(file1, file2):
#     try:
#         with open(file1, 'r') as file:
#             info = file.read()
#         with open(file2, 'a') as file:
#             file.write(info)
#         return 'Success'
#     except FileNotFoundError:
#         return 'No file'

# print(cat('armenian_football.txt', 'russian.txt'))
# -------------------------------------------------------
# PATH = 'armenian_football.txt'
# with open(PATH, 'r') as file:
#     x = file.read().split('\n')
# # for i in x:
# #     print(i)
# print(x)
# -------------------------------------------------------
# def numeric(filename1, filename2):
#     try:
#         with open(filename1, 'r') as file:
#             info = file.readlines()
#         with open(filename2, 'a') as file:
#             for i in range(0, len(info)):
#                 file.write(f'{i + 1}). {info[i]}')
#         return "Good"
#     except FileNotFoundError:
#         return "No File"
# print(numeric('armenian_football.txt', 'new.txt'))
# -------------------------------------------------------
# with open('../../kahoot.txt', 'r') as file:
#     print(file.read())
# -------------------------------------------------------
# with open("C:\\Users\\ASUS\\Desktop\\kahoot.txt", 'r') as file:
#     print(file.read())
# -------------------------------------------------------
# import os

# for i in os.listdir('myfiles/'):
#     with open(f'myfiles/{i}', 'r') as file:
#         print(file.read())
# -------------------------------------------------------
# x = [7, 4, 5, 8, 9, 6]
# x.insert(5, 80)

with open('new.txt') as file:
    mylist = file.read().replace('\n', ' ').split(' ')
mylist.sort(key=len)
print(mylist[-1])