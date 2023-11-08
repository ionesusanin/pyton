#  array - массив  -- содержит один тип данных
# list - список, содержит разные типы данных

# example = [1, 2.0, 'Ivan', True]

# # import array
# # import numpy 
# print(example[2])

# print(*example) убирает скобки и запятые
# set_1 = set()
# for i in 3, 56, 13, 26, 18, 9, 23:
#     set_1.add(i)
# print(set_1)

# list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# print(tuple(list_1))
# print(set(list_1))
# print(len(set(list_1)))

# list_1 = [45, 23, 1, 5, 31]
# # print(list_1[begin=0; end=j,обязательный параметр; step=+1])
# k = int(input("Введите количество сдвигов: ")) % len(list_1)
# if k == 0:
#     print(list_1)
# else:
#     print(list_1[-k:] + list_1[:len(list_1)- k])

# Dictionary
# data = {}
# data_second = dict()
# # key: value
# data['Кирилл'] = 23
# data['Марина'] = 20
# print(data['Кирилл'])
# print(data)
# # print(data.keys())
# # print(list(data.keys()))
# # print(list(data.values()))
# for i in data: # <-> data.keys
#     print(i)
# for i in data.values():
#     print(i)


# Напишите программу для печати всех уникальных значений в словаре. 

# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
#          {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}] 

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


# # Примечание: Список словарей задан изначально. Пользователь его не вводит
# data = [{"V": "S001"}, {"V": "S002"},
#           {"VI": "S001"}, {"VI": "S005"},
#           {"VII": "S005"}, {"V":"S009"},
#           {"VIII":"S007"}]
# # print(data[0])
# set_values = set()
# for i in data:
#     print(i)
#     set_values.add(list(i.values())[0])
# print(set_values)



# Дан массив, состоящий из целых чисел. Напишите программу,
# которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 


# Input: [0, -1, 5, 2, 3]


# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)


# Примечание: Пользователь может вводить 
# значения списка или список задан изначально.

data = [0, -1, 5, 2, 3]
count = 0
for i in range(1, len(data)):
    if data[i - 1] < data[i]:
        count +=1
         
print(count)

