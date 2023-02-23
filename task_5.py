from functools import reduce
new_list = [i for i in range(100,1000) if i % 2 == 0]
sum = reduce((lambda x, y: x * y), new_list)
print(f'Список чисел из диапазона: {new_list}')
print(f'Сумма всех чисел диапазона: {sum}')