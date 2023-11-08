# name = 'Ivan'
#  #      0123
# print(name[0])
# for element in "Hello", 123, 34.125, True, 'a':
#     print(element)
## 0: element = "Hello"
## 1: element = 123
## 2: element = 34.125
## иттд
# range и for никак между собой не связаны!!!
# range(begin = необязательный(0), end = обязательный(), step = необязательный(+1))
# print(type(range(5)))

# print(*range(5))
# 
# for i in range(5):
#     print(i)

# for i in range(5):
#     print(i, end=' ,')

# print(1, end=', ')
# print(2, end='. ')
# print(3, end='!\n')
# #print() перенос на новую строчку как и \n
# print('Hello')
# print("ivan")

# n = int(input("Input number: "))
# result = 1
# while n > 1:
#     result*= n
#     n-= 1
# print(result)
# 
# 
# n = int(input("Введите число: "))
# first_fib = 0
# second_fib = 1
# i = 2 # первые два числа уже известны
# while second_fib < n:
#     next_fib = first_fib + second_fib
#     first_fib = second_fib

#     second_fib = next_fib
#     i += 1
#     if second_fib > n:
#         i = -1
# print(i)


# n = int(input("Введите количество арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa = min_massa = x
# for i in range(n - 1):
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x:
#         min_massa = x
# print(min_massa, max_massa)

# n = int(input("Введите количество дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите температуру: "))
#     if temp >=0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#          count = 0
# print(max_count)    


   
# n = int(input("Введите количество монеток: "))
# heads = tails = 0

# for i in range(n):
#     coin = int(input("heads(1) or tails(0): "))
#     if coin == 1:
#         heads += 1
       
#     else:
#         tails += 1
# if heads < tails:
#     print('переверните {heads} монет с орла на орешку, их меньше')
# elif heads == tails:
#     print('Количество орлов и решек одинаково')
# else:
#     print('переверните {tails} монет с орла на орешку, их меньше')        

# a = int(input("Введите сумму двух чисел: "))
# b = int(input("Введите произведение двух чисел: "))
# for i in range(a):
#     for j in range(b):
#         if a == i + j and b == i * j:
#             print(f'первое число ="{i}", второе число ="{j}"')
            


# n = int(input("Введите число N: ")) 
# i = 0
# while 2 ** i <= n:
    
# #     print(f'2 в степени {i} равна {2 ** i}')  
# #     i += 1
# n=int(input())
# p=1
# while p<=n:
#     print(p,end=' ')
#     p=p*2
    
# s = int(input("Введите сумму элементов: "))
# p = int(input("Введите произведение элементов: "))
# D = s ** 2 - 4 * p
# y1 = (s - D ** 0.5) / 2
# y2 = (s + D ** 0.5) / 2
# x1 = s - y1
# x2 = s - y2
# print(x1, y1)
# print(x2, y2)


n = int(input("Введите количество монеток: "))
heads = tails = 0