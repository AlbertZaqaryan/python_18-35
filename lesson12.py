# --------------------------------------------------
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in range(0, len(arr)):
#     if arr[i] % 2 == 0:
#         arr[i] = 1
#     else:
#         arr[i] = arr[i] % 5
# print(arr)
# --------------------------------------------------
# text = 'hqwehrth'
# h_index = [i for i in range(len(text)) if text[i] == 'h']
# print(text[h_index[0] + 1:h_index[1]][::-1])
# --------------------------------------------------
# text = 'Barev Edgar jan'
# print([i for i in text if i in 'aeiouAEIOU'])
# --------------------------------------------------
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([1 if arr[i] % 2 == 0 else arr[i] % 5 for i in range(len(arr))])

# --------------------------------------------------
# text = 'hqwehrty'
# print(text[text.index('h') + 1: text.replace('h', '', 1).index('h') + 1][::-1])
# --------------------------------------------------
# mylist = [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# print([i for i in mylist if i != 0])
# --------------------------------------------------
# mylist = [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
# print([[i, i + 4, i + 8] for i in range(1, 5)])
# --------------------------------------------------
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# print([i for i in nice_list for i in i for i in i])
# for i in nice_list:
#     for j in i:
#         for k in j:
#             print(k)
# --------------------------------------------------
# text = input('Enter text:  ')
# print(''.join([chr(ord(i) + 3) for i in text]))
# --------------------------------------------------
# ------------------------------- dictionary -----------------------------
# user = {
#     "Name":"Sergo", 
#     "age":22
# }
# print(user)


# fb = {
#     'test@gmail.com':'skaskjajkskas',
#     'sergokhachikyan@gmail.com':'iloveFutzal',
# }


# dict_ = {
#     'b':7,
#     'c':10,
#     'e':-8,
#     'd':5,
#     'a':17
# }
# dict2 = {
#     'g':17,
#     'h':77
# }
# dict3 = {
#     'g':17,
#     'h':77
# }
# dict_.update(dict2)
# dict_.update(dict3)
# print(dict_)
# dict_.setdefault('p', 19)
# dict_['p'] = 19
# print(dict_)
# dict_.popitem()
# print(dict_)
# print(dict_['e'])
# print(dict_['Ճ'])
# print(dict_.get('d', 'ՉԿԱ'))
# dict_.pop('a')
# print(dict_)
# del dict_['a']
# print(dict_)
# dict_.clear()
# print(dict_)

# print(dict_.items())
# print(dict_)
# print(dict_.keys())
# print(dict_.values())
# print(dict_)


# dict_ = {
#     "test@gmail.com":{"Name":"Sergo", "age":22},
#     1:'a'
# }


# sampleDict = dict([
#     ('first', 1),
#     ('second', 2),
#     ('third', 3)
# ])
# print(sampleDict)

# dict_ = {
#     'b':7,
#     'c':10,
#     'e':-8,
#     'd':5,
#     'a':17
# }
# print(dict_.items())


# list1 = [1, 2, 3]
# list2 = list1
# print(list2)


# dict_ = {
#     'b':7,
#     'c':10,
#     'e':-8,
#     'd':5,
#     'a':17
# }
# keys = sorted(dict_.keys())
# print(keys)

# values = sorted(dict_.values())
# print(dict_.values())
# print(dict_.get('a'))
# print(dict_.keys())

# keys = sorted(dict_, key=dict_.get)
# print(keys)
# dict_ = {
#     'b':7,
#     'c':10,
# }
# k = 1
# for i in dict_:
#     k *= dict_[i]
# print(k)

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# my_keys = sorted(dict_, key=dict_.get, reverse=True)[:3]
# my_values = sorted(dict_.values(), reverse=True)[:3]
# newdict = {}
# for i, j in zip(my_keys, my_values):
#     newdict[i] = j
# print(newdict)

# dict_ = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# print({i:dict_[i] for i in sorted(dict_, key=dict_.get, reverse=True)})


# students = {
#     'Edgar':0,
#     'Harutyun':9,
#     'Vardan':7,
#     'Srbuhi':9,
#     'Sergo':1
# }
# mijin = 5.7



# s = 'a,2,b,5,c,8,a,4,e,11'
# {'a':6,'b':5,'c':8,'e':11}


# word = 'exercises'






