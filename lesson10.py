# link = "https://www.youtube.com/watch?v=RRW2aUSw5vU"

# print(link[link.index('=') + 1:])
# link = link.split('=')
# print(link[1])
# ------------------------------------------------------
# text = 'python'
# print(list(text))
# ------------------------------------------------------
# numbers = input('Enter 5 numbers:  ')
# mylist = numbers.split(' ')
# for i in mylist:
#     if int(i) % 2 == 0:
#         print(i)
# ------------------------------------------------------
#excersise 9-այստեղ էլ չի ստացվում
# import random
# group = ["alen", "karen", "sam", "mike", "anna"]
# while group:
#     name = input("Please enter your name: ")
#     group_without_self = [person for person in group if person != name]
#     choosed_name = random.choice(group_without_self)
#     print(f"{name}, your choice is {choosed_name}")
#     group.remove(choosed_name)
# ------------------------------------------------------
# import random

# group1 = ["alen", "karen", "sam", "mike", "anna"]
# group2 = ["alen", "karen", "sam", "mike", "anna"]
# final_list = []
# while group1 != []:
#     u1 = random.choice(group1)
#     u2 = random.choice(group2)
#     if u1 == u2:
#         if len(group1) == 1 == len(group2):
#             group1 = ["alen", "karen", "sam", "mike", "anna"]
#             group2 = ["alen", "karen", "sam", "mike", "anna"]
#             final_list = []
#             continue
#         continue
#     else:
#         final_list.append(f'{u1} --- {u2}')
#         group1.remove(u1)
#         group2.remove(u2)
# for i in final_list:
#     print(i)
# ------------------------------------------------------
# number = int(input('Enter number: '))
# mylist = []
# for i in range(1, number + 1):
#     if number % i == 0:
#         mylist.append(i)
# print(mylist)
# ------------------------------------------------------
# number = int(input('Enter number: '))
# print([i for i in range(1, number + 1) if number % i == 0])
# ------------------------------------------------------
# mylist = [7, 4, 1, 1, 1, 5, 6, 9, 8, 1, 1, 2, 3, 7, 8, 6, 5, 4]
# for i in range(len(mylist)):
#     for j in range(len(mylist)):
#         if mylist[i] == mylist[j] and i != j:
#             break
#     else:
#         print(mylist[i])
# ------------------------------------------------------
# for i in mylist:
#     if mylist.count(i) == 1:
#         print(i)
# ------------------------------------------------------
# print([i for i in mylist if mylist.count(i) == 1])
# ------------------------------------------------------
# mylist = [7, 4, 1, 1, 1, 5, 6, 9, 8, 1, 1, 2, 3, 7, 8, 6, 5, 4]
# mylist.sort()
# if mylist[0] != mylist[1]:
#     print(mylist[0])
# if mylist[-1] != mylist[-2]:
#     print(mylist[-1])
# for i in range(1, len(mylist) - 1):
#     if mylist[i - 1] == mylist[i] or mylist[i] == mylist[i + 1]:
#         continue
#     else:
#         print(mylist[i])
# ------------------------------------------------------
# mylist = [7, 4, 1, 1, 1, 5, 6, 9, 8, 1, 1, 2, 3, 7, 8, 6, 5, 4]
# mylist.sort()
# for i in range(len(mylist) - 2, 0, -1):
#     if mylist[i] == mylist[i + 1]:
#         mylist.pop(i + 1)
#     if mylist[i] == mylist[i - 1]:
#         mylist.pop(i)
# print(mylist)
# ------------------------------------------------------
# mylist = [1, 2, 3, 4]
# newlist = []
# for i in range(len(mylist)):
#     for j in range(i + 1, len(mylist) + 1):
#         newlist.append(mylist[i:j])
# newlist.sort(key=len)
# print(newlist)
# ------------------------------------------------------
# mylist = [1, 2, 3, 4]
# newlist = [mylist[i:j] for i in range(len(mylist)) for j in range(i + 1, len(mylist) + 1)]
# newlist.sort(key=len)
# print(newlist)
# ------------------------------------------------------
# master = ['♥', '♦', '♣', '♠']
# karter = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# ------------------------------------------------------
mylist = ['flower', 'flow', 'flight']

