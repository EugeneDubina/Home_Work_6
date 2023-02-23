from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, bonus = argv
    time_work = int(time_work)
    rate = int(rate)
    bonus = int(bonus)
    print((time_work * rate) + bonus)
else:
    time_work = int(input("Введите количество отработанных часов: "))
    rate = int(input("Введите почасовую ставку: "))
    bonus = int(input("Введите размер премии: "))
    print(time_work * rate + bonus)