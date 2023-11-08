# n=5
# print(type(n))
# name = input("Введите свое имя: ")
# print(f'Привет, {name}!')

# n = '234'
# print(int(n) - 10) #int() переводить данные из str в int 

# n = 2.871
# print(int(n))

# n = int(input("Введите число: "))
# print(f'{n} * 2 = {n * 2}')

# n = float(input("Введите дробное число: "))
# print(f'{n} * 2 = {n * 2}')

# n = int(input('Введите целое число: '))
# print(f'{n} + 5 = {n + 5}')  # сложение
# print(f'{n} - 5 = {n - 5}') # Вычитание
# print(f'{n} * 5 = {n * 5}') # Умножение
 
# print(f'{n} : 5 = {n // 5} (остаток {n % 5})') # деление (выведение остатка)
# print(f'{n} : 5 = {n / 5}') # Деление
# print(f'{n}^5 = {n ** 5}') # Возведение в степень
# print(f'{n}^5 = {n ** 0.5})') # квадратный корень

# n = int(input('Введите целое число: '))
# print(int(n > 8))
# bool (boolean) - true (1) or false (0)

# and (&&) - коньюнкция (Логическое умножение)
# or (||) дизъюнкция (логическое сложение)
# not - отрицание
# in ??
# print(n > 8 and n < 17)
# print(n > 8 or n < 4)
# print(not n > 8)


# n = int(input("Введите количество километров, проезжаемое за день: "))
# m = int(input("Введите километраж: "))
# print((m + n - 1)// n)

# Отрицательное диление
# -7 // 2

# a = int(input('Введите количество учеников в первом классе:'))
# b = int(input('Введите количество учеников во втором классе:'))
# c = int(input('Введите количество учеников в третьем классе:'))
# sum1 = a//2 + a % 2
# sum2 = b//2 + b % 2
# sum3 = c//2 + c % 2
# print(sum1 + sum2 + sum3)

# i = int(input('В какой вагон сел Витя:'))
# j = int(input('Какой вагон указан на табличке:'))
# if i == j:
#     print("Нужна дополнительная информация")
# else:
#     print(i + j - 1)

# year = int(input('Введите год:'))
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')
# n = input('Введите трехзначное число: ')
# res = 0
# if len(n) == 3:
#     for i in n:
#         res += int(i)
#     print(res)
# else:
#     print('введено не трехзначное число')

# n = input('Введите трехзначное число: ')
# n1 = int(n[0])
# n2 = int(n[1])
# n3 = int(n[2])
# res = n1 + n2 + n3
# print(res)
# n = 123
# res = n//100 + n//10%10 + n%10
# print(res)
# n = 6

# # Введите ваше решение ниже
# # print(n/6, n/6*4, n/6)

# print(p)

# n = 385916
# a = n//1000
# b = n%1000
# n1 = a//100
# n2 = a%100//10
# n3 = a%10
# sum1 = n1 + n2 + n3
# n4 = b//100
# n5 = b%100//10
# n6 = b%10
# sum2 = n4 + n5 + n6
# if sum1 == sum2:
#     print('yes')
# else:
#     print('no')
a = 3
b = 2
c = 4

if c < a*b and (c%b==0 or c%a==0):
    print('yes')
else:
    print('no')