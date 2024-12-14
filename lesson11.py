# mylist = []
# while True:
#     number = int(input('Enter number: '))
#     if number == 0:
#         mylist.sort()
#         print(mylist)
#         break
#     else:
#         mylist.append(number)
# ------------------------------------------------------------

# mylist = []
# while True:
#     number = int(input('Enter number:  '))
#     if number == 0:
#         break
#     else:
#         mylist.append(number)
# if len(mylist) < 4:
#     print('ERROR')
# else:
#     print(mylist)
#     mylist.remove(min(mylist))
#     mylist.remove(max(mylist))
#     print(mylist)

# ------------------------------------------------------------

# list1=[]
# n=int(input("please enter number: "))
# while n!=0:
#     list1.append(n)
#     n=int(input("please enter number: "))
# else:
#     if len(list1)<4:
#         print("Error you have entered few aguments")
#     else:
#         list1.sort()
#         print(list1)  
# new_list=list1.copy()
# new_list.remove(max(new_list))
# new_list.remove(min(new_list))
# print(new_list)
# ------------------------------------------------------------

# mylist1 = []
# mylist2 = []
# mylist3 = []
# while True:
#     number = input('Enter number: ')
#     if number == '':
#         break
#     else:
#         number = int(number)
#         if number < 0:
#             mylist1.append(number)
#         elif number == 0:
#             mylist2.append(number)
#         else:
#             mylist3.append(number)
# print(mylist1 + mylist2 + mylist3)
# ------------------------------------------------------------
# n = int(input("please enter number: "))
# new_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         new_list.append(i)
# print(new_list)
# ------------------------------------------------------------
# import random

# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# kalod = []
# for i in master:
#     for j in karter:
#         kalod.append(i + j)
# nor_kalod = []
# while kalod != []:
#     random_card = random.choice(kalod)
#     nor_kalod.append(random_card)
#     kalod.remove(random_card)
# users = [input('Enter your name:  ') for i in range(4)]
# for i in users:
#     print(f'{i} ---> {nor_kalod[:8]}')
#     nor_kalod = nor_kalod[8:]
# ------------------------------------------------------------
# mylist = ['flower', 'flow', 'flight']
# mylist.sort(key=len)
# index = 1
# while index < len(mylist):
#     if mylist[0] == mylist[index][:len(mylist[0])]:
#         index += 1
#     else:
#         mylist[0] = mylist[0][:-1]
# print(mylist[0])
# ------------------------------------------------------------
# mylist = [4, 7, 10, 15, 30, 45, 70, 85, 125, 260, 312, 445, 968, 1020, 2450, 6380, 9650]

# n = 968
# start = 0
# stop = len(mylist)
# while True:
#     mid = (start + stop) // 2
#     if n == mylist[mid]:
#         print(mid)
#         break
#     elif n > mylist[mid]:
#         start = mid + 1
#     else:
#         stop = mid - 1
# ------------------------------------------------------------
# mylist = [4, 5, 7, 8, 9]
# mylist.insert(2, 10)
# ------------------------------------------------------------
# mylist = [3, 0, 1, 1, 1, 4]
# jump = 0
# while True:
#     if jump >= len(mylist):
#         print(False)
#         break
#     elif jump == len(mylist) - 1:
#         print(True)
#         break
#     if mylist[jump] == 0:
#         print(False)
#         break
#     jump += mylist[jump]
# ------------------------------------------------------------
# --------------------------- HOME ---------------------------
# -------------------------> TASK 1 <-------------------------
# text = 'hello'
# >>> 4
# ----
# text = 'zzz'
# >>> 1
# ----
# -------------------------> TASK 2 <-------------------------
# mylist = [1, 2, 3, 4]
# step = 2
# >> [3, 4, 1, 2]
# -------------------------> TASK 3 <-------------------------





