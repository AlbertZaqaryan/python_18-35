# n = 5
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)
# -----------------------------------------
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#     #          5 * 4 * 3 * 2 * 1
# print(fact(5))
# -----------------------------------------
# 0, 1, 1, 2, 3, 5, 8
# n1 = 0
# n2 = 1
# for i in range(6):
#     n1, n2 = n2, n1 + n2
# print(n1)
# -----------------------------------------
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 2) + fib(n - 1)
#     # fib(4) + fib(5)
#     # fib(2) + fib(3) + fib(5)
#     # fib(0) + fib(1) + fib(3) + fib(5)
#     # 0 + 1 + fib(1) + fib(2) + fib(5)
#     # 0 + 1 + 1 + fib(0) + fib(1) + fib(5)
#     # 0 + 1 + 1 + 0 + 1 + fib(3) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(4)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(2) + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(3)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + fib(1) + fib(2)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
#     # 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8
# print(fib(6))
# -----------------------------------------
# def summ():
#     n = int(input('Enter number: '))
#     if n == 0:
#         return 0
#     else:
#         return n + summ()
#     #       5 + 4 + 8 + 0
# print(summ())
# -----------------------------------------
# def func(x):
#     if x == []:
#         return []
#     else:
#         return [x[0]] * x[1] + func(x[2:])
    #         ['A'] * 12 + func(["B", 4, "A", 6, "B", 1]])
    # ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'] + ['B'] * 4 + []

# print(func(["A", 12, "B", 4, "A", 6, "B", 1]))
# ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
# -----------------------------------------


# def func(mylist, count=1):
#     if len(mylist) == mylist.count(mylist[0]):
#         return [mylist[0], len(mylist)]
#     elif mylist[0] == mylist[1]:
#         return func(mylist[1:], count + 1)
#     else:
#         return [mylist[0], count] + func(mylist[1:], count = 1)
# print(func(["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]))
# -----------------------------------------
# def dec_to_bin(number):
#     if number == 1:
#         return '1'
#     else:
#         return dec_to_bin(number // 2) + str(number % 2)
# print(dec_to_bin(13))
# -----------------------------------------
# def prime_list(mylist):
#     pass

# print(prime_list([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]