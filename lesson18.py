# def nato(text):
#     phonetic_dict = {
#     'A': 'Alpha',    'J': 'Juliet',    'S': 'Sierra',
#     'B': 'Bravo',    'K': 'Kilo',      'T': 'Tango',
#     'C': 'Charlie',  'L': 'Lima',      'U': 'Uniform',
#     'D': 'Delta',    'M': 'Mike',      'V': 'Victor',
#     'E': 'Echo',     'N': 'November',  'W': 'Whiskey',
#     'F': 'Foxtrot',  'O': 'Oscar',     'X': 'Xray',
#     'G': 'Golf',     'P': 'Papa',      'Y': 'Yankee',
#     'H': 'Hotel',    'Q': 'Quebec',    'Z': 'Zulu',
#     'I': 'India',    'R': 'Romeo'
# }
#     if text == '':
#         return ''
#     else:
#         return phonetic_dict[text[0]] + ' ' + nato(text[1:])

# print(nato("SRBUHI"))
# -------------------------------------------------------------
# def prime_list(mylist):
#     if mylist == []:
#         return []
#     elif type(mylist[0]) == int:
#         return [mylist[0]] + prime_list(mylist[1:])
#     else:
#         return prime_list(mylist[0]) + prime_list(mylist[1:])

# print(prime_list([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
# -------------------------------------------------------------
# def coins(count, amount):
#     if count == 0 or amount == 0:
#         return count == amount
#     return coins(count - 1, amount - 25) or coins(count - 1, amount - 10) or coins(count - 1, amount - 5) or coins(count - 1, amount - 1)
# print(coins(3, 61))
# -------------------------------------------------------------
# mylist = [
#     [0, 1, 0, 0, 0, 1, 1],
#     [1, 0, 1, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 0, 0]
# ]
# -------------------------------------------------------------
# def func(mylist):
#     if mylist == []:
#         return []
#     elif mylist[0] % 2 == 0:
#         return [mylist[0]] + func(mylist[1:])
#     else:
#         return func(mylist[1:])

# print(func([7, 4, 1, 2, 5, 6, 9, 8, 3]))
# -------------------------------------------------------------
# def maxPrefix(mylist, count=1):
#     if count == len(mylist):
#         return mylist[0]
#     elif mylist[0] == mylist[count][:len(mylist[0])]:
#         return maxPrefix(mylist, count + 1)
#     else:
#         mylist[0] = mylist[0][:-1]
#         return maxPrefix(mylist, count)
# print(maxPrefix(['flow', 'flower', 'flight']))
# -------------------------------------------------------------
# def sum_nested(lst):
#     if lst == []:
#         return 0
#     elif type(lst[0]) == int:
#         return lst[0] + sum_nested(lst[1:])
#     else:
#         return sum_nested(lst[0]) + sum_nested(lst[1:])
# print(sum_nested([1, [2, [3, [4]]]]))
# -------------------------------------------------------------
# mylist = [7, 4, 8, 5, 9, 6, 5, 2, 1, 4, 7, 8]



