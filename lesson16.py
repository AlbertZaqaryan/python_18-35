# def calendar(year, month, day):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     summ = 0
#     for i in range(month - 1):
#         summ += day_list[i]
#     summ += day
#     return summ
# year = int(input('Enter year:  '))
# month = int(input('Enter month:  '))
# day = int(input('Enter day:  '))
# print(calendar(year, month, day))
# -------------------------------------------------
# def reverce_calendar(year, day):
#     day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if year % 4 == 0:
#         day_list[1] = 29
#     month = 0
#     while day_list[month] < day:
#         day -= day_list[month]
#         month += 1
#     month += 1
#     return f'{year}:{month}:{day}'
# year = int(input('Enter year:  '))
# day = int(input('Enter day:  '))
# print(reverce_calendar(year, day))
# -------------------------------------------------
# x = lambda a, b:a + b
# print(x(5, 7))
# -------------------------------------------------
# mylist = [160, -1, 180, 170, -1, -1, 190, 150]
# [150, -1, 160, 170, -1, -1, 180, 190]
# -------------------------------------------------
# data = {
#     'Vardan':20,
#     'Sergo':14
# }
# name = input('Enter name: ')
# age = int(input('Enter age: '))
# print(data.get(name) == age)
# -------------------------------------------------

# a = 6
# b = 10
# c = -1
# x1 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)
# x2 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
# print(x1, x2)
# -------------------------------------------------


# a = 5
# b = 4
# c = 3
# p = (a + b + c) / 2
# print((p * (p - a) * (p - b) * (p - a)) ** 0.5)
# -------------------------------------------------

# import random

# user_points = 0
# pc_points = 0
# while True:
#     if user_points == 3:
#         print('WIn user')
#     elif pc_points == 3:
#         print('Win pc')
#     user = input('Rock, Paper, Scissors:  ')
#     pc = random.choice(['Rock', 'Paper', 'Scissors'])
#     if user == 'Rock' and pc == 'Paper' or user == 'Paper' and pc == 'Scissors' or user == 'Scissors' and pc == 'Rock':
#         pc_points += 1
#     else:
#         user_points += 1
# -------------------------------------------------


# list1 = [1, 2, 3]
# list2 = list1[::]
# list2.append(4)
# print(list1)

# -------------------------------------------------

# data = {
#     'Vardan':20,
#     'Sergo':14
# }
# for i in data:
#     print(i)
# -------------------------------------------------

# mydata = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:mydata[i] for i in sorted(mydata, key=mydata.get, reverse=True)[:3]})
# -------------------------------------------------

# set1 = {1, 2, 3}
# set1.add(4)
# set1.discard(3)
# print(set1)
# -------------------------------------------------
# mylist = [160, -1, 180, 170, -1, -1, 190, 150]
# newlist = [i for i in mylist if i != -1]
# newlist.sort()
# i = 0
# j = 0
# while i < len(mylist):
#     if mylist[i] == -1:
#         i += 1
#     else:
#         mylist[i] = newlist[j]
#         i += 1
#         j += 1
# print(mylist)
# -------------------------------------------------
