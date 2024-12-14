# ---------------------------------------------------
# a, b, c = 7, 5, 3
# for i in range(b):
#     print('=' * a + " " + c * "*" + " " + a * '=')
# ---------------------------------------------------
# import random
# comp_number=random.randint(0,10)
# count_of_attempts=1
# while True:
#     childs_number=int(input("please enter number to guess from 0 to 10: "))
#     if childs_number==comp_number:
#         print(f"you guessed right number,you have tried {count_of_attempts} times.")
#         break
#     else:
#         if childs_number<comp_number:
#             print(f"your number is lower,please try agian")
#             count_of_attempts+=1
#         elif childs_number>comp_number:
#             print(f"your number is higher,please try agian")
#             count_of_attempts+=1
# ---------------------------------------------------
# import random
# left=0
# right=100
# comp_attempts=1
# user_number=int(input("please enter number from 0 to 100: "))
# while True:
#     comp_number=int(random.randint(left,right))
#     print(f"your number is {comp_number}?")
#     user_answer=input("please enter < or > or =")
#     if user_answer=="=":
#         print("finally i guesss your number")
#         break
#     else:
#         if  user_answer=="<":
#             right=comp_number-1
#             comp_attempts+=1
#         elif user_answer==">":
#             left=comp_number+1
#             comp_attempts+=1
# print(f"i guess it after {comp_attempts} attempts")
# ---------------------------------------------------
# for i in range(10,100):
#     if 3*(i//10)*(i%10)==i:
#         print(i)
# ---------------------------------------------------
# x = (7, 8, 6)
# print(type(x))
# for i in x:
#     print(i)
# ---------------------------------------------------


# x = (7, True, 'Barev', (8, 4, 5), 'Sergo Futbolist rozvi hamazgestov')
# ---------------------------------------------------

# y = [7, True, 'Barev', (8, 4, 5), 'Sergo']
# y.sort()
# print(y)
# ---------------------------------------------------

# x = [7, 8, 5.6, 9, 0, -10]
# print(x.sort())
# print(x)
# ---------------------------------------------------

# y = 10
# print(y + 10)
# print(y)
# ---------------------------------------------------
# x = [1, 2, 3]
# x[1] = 10
# print(x)
# ---------------------------------------------------
# a = 10
# b = a
# b += 5
# print(a)
# ---------------------------------------------------
# a = [1, 2, 3]
# b = a.copy()
# # b = a[:]
# # b = a[::]
# b.append(4)
# print(a)
# ---------------------------------------------------
# a = [7, 4, 5, 8, 9, 6]
# a.sort(reverse=True)
# print(a)
# ---------------------------------------------------

# a = ['b', 'd', 'e', 'a']
# a.sort()
# print(a)
# ---------------------------------------------------

# a = ['python', 'pythonchi Sergo', 'Serg', 'Futbol', 'Jabulani gndak']
# a.sort()
# print(a)
# ---------------------------------------------------

# a = ['python', 'pythonchi Sergo', 'Serg', 'Futbol', 'Jabulani gndak']
# a.sort(key=len, reverse=True)
# print(a)
# ---------------------------------------------------

# mylist = [7, 4, 5]
# mylist[0] = -10
# print(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5]
# mylist.append(1)
# mylist.append(8)
# mylist.append(9)
# print(mylist)
# ---------------------------------------------------


# mylist = [7, 4, 5]
# mylist.insert(1, 100)
# print(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5]
# print(len(mylist))
# ---------------------------------------------------

# mylist = [7, 4, 5]
# mylist.remove(5)
# print(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5]
# mylist.pop(2)
# print(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5]
# del mylist[1:]
# print(mylist)
# ---------------------------------------------------


# mylist = [7, 4, 5]
# mylist.pop(1)
# mylist.pop()
# print(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5, 4, 7, 8, 5, 6, 9, 8]
# print(mylist.count(7))
# ---------------------------------------------------


# import random

# mylist = [7, 4, 5, 4, 7, 8, 5, 6, 9, 8]
# print(random.choice(mylist))

# ---------------------------------------------------

# mylist = [7, 4, 5, 4, 7, 8, 5, 6, 9, 8]
# print(mylist.index(4))
# for i in range(0, len(mylist)):
#     if mylist[i] == 4:
#         print(i)
# ---------------------------------------------------


# mylist = [7, 4, 5, 4, 7, 8, 5, 6, 9, 8]
# mylist.clear()
# print(mylist)
# ---------------------------------------------------

# list1 = [1, 2, 3]
# list2 = [8, 9, 6]
# print(list1 + list2)
# list1.extend(list2)
# print(list1)
# ---------------------------------------------------


# text = 'python'
# print(list(text))
# ---------------------------------------------------

# text = 'Sergon siruma futbol'
# text = text.split(' ')
# print(text)
# ---------------------------------------------------

# list1 = ['Sergon', 'siruma', 'futbol']
# print(' '.join(list1))
# ---------------------------------------------------

# print([i ** 2 for i in range(10)])
# ---------------------------------------------------


# mylist = [1, 2, 3]
# newlist = mylist.copy()
# newlist = list(mylist)
# ---------------------------------------------------

# mylist = [7, 4, 5, 1, 2, 6, 3, 9, 8]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append(i)
# print(newlist)
# ---------------------------------------------------

# mylist = [7, 4, 5, 1, 2, 6, 3, 9, 8]
# print([i for i in mylist if i % 2 == 0])
# ---------------------------------------------------


# mylist = [7, 4, 5, 1, 2, 6, 3, 9, 8]
# newlist = []
# for i in mylist:
#     if i % 2 == 0:
#         newlist.append('Even')
#     else:
#         newlist.append('Odd')
# print(newlist)
# ---------------------------------------------------
# mylist = [7, 4, 5, 1, 2, 6, 3, 9, 8]
# print(['Even' if i % 2 == 0 else 'Odd' for i in mylist])
# ---------------------------------------------------
# mylist = [7, 4, 5, 8, 8, 8, 8, 8, 8, 6, 3, 2, 1, 8]
# [7, 4, 5, 8, 6, 3, 2, 1]
# for i in mylist:
#     if mylist.count(i) > 1:
#         mylist.remove(i)
# print(mylist)
# ---------------------------------------------------
# mylist = [7, 4, 5, 8, 8, 8, 8, 8, 8, 6, 3, 2, 1, 8]
# for i in range(len(mylist) -1, -1, -1):
#     if mylist.count(mylist[i]) > 1:
#         mylist.pop(i)
# print(mylist)
# ---------------------------------------------------

# mylist = [4, 7, 5, 6 , 1, 0, 9, 8, 7]
# for _ in range(0, len(mylist)):
#     for j in range(0, len(mylist) - 1):
#         if mylist[j] > mylist[j + 1]:
#             mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
# print(mylist)
# ---------------------------------------------------

# mylist = [4, 7, 5, 6 , 1, 0, 9, 8, 7]
# for i in range(0, len(mylist)):
#     for j in range(i, len(mylist)):
#         if mylist[i] > mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)
# ---------------------------------------------------

# mylist = [4, 7, 5, 6 , 1, 0, 9, 8, 7]
# mylist.sort()
# print(mylist)
# ---------------------------------------------------
