# list1=[0,2,3,0,1,0,2,4]
# new_list2=[]
# for i in range (len(list1)):
#     for j in range(len(list1)):
#         if list1[i]>list1[j]:
#             new_list2.append(list1[j]*(j-i))
#         else:
#             new_list2.append(list1[i]*(j-i))
# print(max(new_list2))

# def x():
#     for i in range(10):
#         print(i)


# x()
# x()
# x()
# x()
# x()
# x()
# x()
# x()
# x()
# x()
# x()


# def test():
#     print(10)

# x = test() + 5
# print(x)


# def test():
#     return 10

# x = test() + 5
# print(x)


# def myfunc():
#     for i in range(1, 10):
#         print(i)
# myfunc()


# import math

# print(math.sqrt(25))


# def armat(tiv):
#     return tiv ** 0.5

# number = int(input('Enter number: '))
# print(armat(number))


# def gumar(a, b):
#     return a + b

# print(gumar(4, 6))
# print(gumar(10, -3))
# print(gumar(5, 10))


# def test1(x):
#     return x ** 2


# def test2(a, b):
#     result = a + b
#     return test1(result)

# print(test2(5, 3))


# def test():
#     print(10)

# print(test() + 5)

# def test():
#     return 10

# print(test() + 25)


# def myfunc():
#     for i in range(10):
#         print(i)
# myfunc()


# def armat(tiv):
#     return tiv ** 0.5

# print(armat(25))
# print(armat(64))
# print(armat(17))

# def summ(a, b):
#     return a + b

# print(summ(int(input('Enter a: ')), int(input('Enter b: '))))
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(summ(a, b))

# number1 = int(input('Enter a: '))
# number2 = int(input('Enter b: '))
# print(summ(number1, number2))

# def test(a=50):
#     return a
# print(test(70))

# def test(a=3, b=8):
#     return a, b
# print(test(b=6, a=9))

# def test(a, b):
#     return a, b
# print(test(5, b=6))


# def func(*args):
#     return args

# print(func())

# def test(**kwargs):
#     return kwargs
# print(test(a=7, b=8))


# x = 10

# def func():
#     global x
#     x += 5
#     return x

# print(func())


# import matem

# print(matem.armat(65))


# import matem

# print(matem.armat(25))


# def yandex(m):
#     return round(4 + 0.25 * (m / 140), 2)

# distance = int(input('Enter dicstance: '))
# print('$', yandex(distance))



def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

print(next_prime(17))