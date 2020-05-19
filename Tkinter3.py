# import random
# first_names = ('Варвара', 'Вася', 'Наталья', 'Лидия', 'Федор', 'Петя', 'Агафона', 'Алла', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Пол', 'Мария', 'Тор')
# res = []
# for i in range(3):
#  res.append ("".join(random.choice(first_names)+" "+ str(random.randint(1,20))))
#
# print(res)
import time

def timer():
    count_timer = 0
    trigger_time = 1
    work_unit()
    while True:
        time.sleep(1)  # in seconds
        count_timer += 1
        print(count_timer)
        if count_timer == trigger_time:
            count_timer = 0
            work_unit()

def work_unit():  # моделируем работу # на каждое срабатывание таймера бежим по рабочему словарю вычитаем из сложности первой задачи производительность юнита
    count = 0
    for key in list_unit_and_task:  # бежим по словарю
        if list_unit_and_task[key] != []:  # останавливаем работу когда все задачи удалены
            count += 1
        if count == 0:
            break
    for key in list_unit_and_task:  # бежим по словарю
        if list_unit_and_task[key] == []:
            continue
        lvl_unit = int(key[-2:])  # вытаскиваем из кей значения производительности юнита от строка поэтому тащим срез
        lvl_first_task = int(list_unit_and_task[key][0][-3:])  # вытаскиваем производительность задачи , она тоже строка поэтому срез
        rest_of_task = lvl_first_task - lvl_unit  # минусуем из сложности производительность
        if rest_of_task <= 0:  # если задача выполнена те сложность меньше нуля
            list_unit_and_task[key].pop(0)  # удаляем задачу , она первая в массиве
        print(list_unit_and_task)
        if rest_of_task > 0:
            inter_list_unit_and_task = list_unit_and_task[key][0][:-3]
            inter_list_unit_and_task_1 = inter_list_unit_and_task + ' ' + str(rest_of_task)
            list_unit_and_task[key][0] = inter_list_unit_and_task_1
            print(list_unit_and_task)

list_unit_and_task = {'Вася 15': ['1 Вешаем   43','Пашем   117', 'Курим   50'], 'Петя   18': ['2 Повешаем   43','Лудим   17', 'Паяем   119'], 'Оля 10': ['1 Пошьем   43','Шьем   17', 'Вешаем   19']}
print(timer())
