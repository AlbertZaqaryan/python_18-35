# import math

# a = int(input('Enter number1:  '))
# b = int(input('Enter number2:  '))
# print(a + b)
# print(a - b)
# print(a * b)
# print(a // b)
# print(a % b)
# print(math.log10(a))
# print(a ** b)
# ---------------------------------------------------------------------
# import time

# start = time.time()
# print([i for i in range(100000)])
# finish = time.time()
# print(finish - start)

# print(time.time())
# ---------------------------------------------------------------------

# import time

# print(3)
# time.sleep(2)
# print(2)
# time.sleep(2)
# print(1)
# time.sleep(3)
# print('Start game..')
# ---------------------------------------------------------------------
# import datetime

# print(datetime.datetime.now())
# ---------------------------------------------------------------------
# import calendar

# print(calendar.calendar(2024))
# ---------------------------------------------------------------------
# import random

# random.seed(3)
# print(random.randint(1, 24))


# print(random.random())
# print(random.randint(-50, 6))
# print(random.randrange(1, 20, 4))

# print(random.choice('python'))
# print(random.choice(('Rock', 'Scissors', 'Paper')))
# ---------------------------------------------------------------------
# and or not is in

# print(5 > 4 and 10 < 3)
# print(10 < 3 and 5 > 4)
# print(10 < 3 or 5 > 4)
# ---------------------------------------------------------------------


# x = 10
# y = 7
# print(x <= y and x != y or y < x)
#     False  and True  or True
#           False  or  True
#               True

# ---------------------------------------------------------------------

# x = 10
# y = 7
# print(x <= y and (x != y or y < x))
#     False and (True or True)
#     False and True
#         False
# ---------------------------------------------------------------------


# x = 5
# y = 5
# print(x is y)
# print(id(x))
# print(id(y))

# print(5 == 5)
# ---------------------------------------------------------------------

# x = 7
# y = 4
# print(x is not y)
# ---------------------------------------------------------------------

# text = 'python'
# print('opy' in text)
# print('o' in text and 'p' in text and 'y' in text)
# print('k' not in text)
# ---------------------------------------------------------------------

# text = 'python'
# print(text[0])
# print(text[-2])
# print(text[2])
# print(len(text))
# ---------------------------------------------------------------------


# text = 'python'
# print(text[1:3])
# print(text[0:4])
# print(text[:4])
# print(text[:6])
# print(text[2:len(text)])
# print(text[2:])
# print(text[-3:])
# print(text[-1:-3:-1])
# print(text[5:2:-1])
# print(text[::2])
# print(text[::-2])
# print(text[::-1])
# ---------------------------------------------------------------------

# text = 'barev'
# print(text.upper())
# ---------------------------------------------------------------------

# a = 'BAREV'
# print(a.lower())
# ---------------------------------------------------------------------

# text = 'barev python'
# print(text.capitalize())
# ---------------------------------------------------------------------

# text = 'barev python'
# print(text.title())
# ---------------------------------------------------------------------

# text = 'python'
# print(text.index('o'))
# ---------------------------------------------------------------------

# text = 'pythoooooon'
# print(text.count('o'))
# ---------------------------------------------------------------------

# text = 'barev'
# print(text.isupper())
# print(text.islower())
# ---------------------------------------------------------------------

# x = 'asnakjsjaskja'
# print(x.isalpha())
# ---------------------------------------------------------------------

# x = '7'
# print(x.isdigit())
# ---------------------------------------------------------------------

# a = '785a saqw'
# print(a.isalnum())
# ---------------------------------------------------------------------

# print(10 > 4)

# ---------------------------------------------------------------------
# print(len('python') > len('java'))
# print('python' > 'pyjava')
# ---------------------------------------------------------------------

# print(chr(13895))

# print(ord('ա'))
# ---------------------------------------------------------------------
# q1 = input('What is python?\na) Programming language, b) Interpreter\nc) Math modul, d) Game\n\tAnswer===>')
# q2 = input('What is java?\na) Programming language, b) Interpreter\nc) Compiler, d) Game\n\tAnswer===>')
# print(q1 == 'b' and q2 == 'c')
# ---------------------------------------------------------------------

# cars = "BMW", "MERS" 
# years = 2020, 2015
# dream_car_model = input('Enter car model:  ')
# dream_car_year = int(input('Enter car year:  '))
# print(dream_car_model in cars and dream_car_year in years)
# ---------------------------------------------------------------------


# import random

# number = input('Enter 5 numbers:  ')
# print(str(random.randint(1, 10)) in number)
# ---------------------------------------------------------------------

# '7' in '47856'

# import math

# number = int(input('Enter number: '))
# print(math.factorial(number))
# ---------------------------------------------------------------------
# tobacco = int(input('Enter tobacco in grams: '))
# print('Sigaret cout =', tobacco // 20)
# ---------------------------------------------------------------------
