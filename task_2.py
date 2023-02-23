list_num = [30, 22, 12, 44, 66, 88, 41, 10, 37, 12, 81, 138, 53]
new_list = [list_num[i]
            for i in range(1, len(list_num)) if list_num[i-1] < list_num[i]]
print("Исходные данные: " + str(list_num))
print("Результат сортировки: " + str(new_list))