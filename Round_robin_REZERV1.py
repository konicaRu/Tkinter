from tkinter import *
import random
import time

root = Tk()
root.title('Round robin')  # надпись на верху
root.geometry('850x500+300+200')  # ширина=500, высота=400, x=300, y=200 размер окна
root.resizable(True, False)  # размер окна может быть изменён только по горизонтали
timer_after_id = ''  # переменная таймера ведет счет
count_timer = 0  # счетчик таймера


class WindowUnit():
    def __init__(self, main):
        self.listbox = Listbox(main, height=25, width=35, selectmode=EXTENDED)  # список с пунктами из листа list_performer список исполнителей и задач
        self.field_call = Label(main, text='Список исполнителей', width=18, font=10, justify=LEFT)
        self.field_call.grid(row=0, column=0)
        self.listbox.grid(row=1, column=0)

        self.listbox_ready_task = Listbox(main, height=25, width=35, selectmode=EXTENDED)  # список выполненных задач с пунктами из листа list
        self.field_call_ready_task = Label(main, text='Выполненные задачи', width=17, font=10, justify=LEFT)
        self.field_call_ready_task.grid(row=0, column=2)
        self.listbox_ready_task.grid(row=1, column=2)

        self.button_new = Button(main, text='New', width=16, font=10, command=self.unit_and_task_arr)  # кнопка New на первом листе
        self.button_new.grid(row=3, column=0, sticky='s')  # расположение кнопки New
        self.button_pause = Button(main, text='Pause', width=16, font=10, command=self.pause_timer)
        self.button_pause.grid(row=3, column=1)
        self.unit = Unit()  # ссылка на класс исполнители
        self.task = Task()  # ссылка на класс задачи
        # self.timer_after_id = '' # переменная таймера ведет счет
        # self.count_timer = 0  # счетчик таймера
        self.trigger_time = 2  # время срабатывания
        self.list_unit_and_task = {}  # массив для хранения исполнителей и задач
        self.count_work_unit = 0  # счетчик остатка задач в функции work_unit


    def unit_and_task_arr(self):  # формируем  два списока исполнителей и задач self.list_unit_and_task-для работы и self.list_unit_and_task_to_display для отображения
        self.unit.unit_generate()  # запускаем в классе Unit функцию unit_generate(), формируем список исполнителей
        self.task.task_generate()  # # запускаем в классе Task функцию task_generate(), формируем список задач
        shift = 0
        for keys in self.unit.arr_unit:  # формируем рабочий словарь  self.list_unit_and_task вида {'Ivan 7': ['Пашет', 'Лудит', 'Закапывает'], 'Vasya 5': ['Сеет', 'Паяяет', 'Откапывает']}
            self.list_unit_and_task[keys] = [self.task.arr_task[val] for val in range(shift, len(self.task.arr_task), len(self.unit.arr_unit))]  # генератор списков в словаре
            # Первому ключу из self.unit.arr_unit присваивается первое значение из self.task.arr_task,
            # второму -- вторая и т. д. N+1 - я задача снова назначается первому ключу, и так далее по кругу.
            shift += 1
        # формируем отдельный словарь для отображения в программе  исполнитель и первая завдача в списке
        int_arr_unit = []
        for key in self.list_unit_and_task:  # формируем список из ключей
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:  # формируем список из первых задач
            int_arr_task.append(self.list_unit_and_task[key][0])
        self.list_unit_and_task_to_display = []
        for i in range(len(int_arr_unit)):  # обьеденяем два списка в один вложенный список [['Алекс 8', 'Выпил 8'], ['Абросимова 9', 'Сьел 9'], [' Алекс 7', ' Вдохнул 7']]
            inter_arr_displey = str(int_arr_unit[i]) + ' ' + str(int_arr_task[i])
            self.list_unit_and_task_to_display.append(inter_arr_displey)
        # это обьединялка в один словарь self.list_unit_and_task_to_display{}
        for unit in self.list_unit_and_task_to_display:  # пробегаем по словарю передаем в программу
            self.listbox.insert(END, unit)
        self.timer()  # запускаем функцию работу таймера

    def update_display (self): # обновляем отображение в первом окне при срабатывани таймера
        self.listbox.delete(0, END) # очищаем self.listbox чтобы заново заполнить его
        int_arr_unit = []
        for key in self.list_unit_and_task:  # формируем список из ключей
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:  # формируем список из первых задач
            int_arr_task.append(self.list_unit_and_task[key][0])
        self.list_unit_and_task_to_display = []
        for i in range(len(int_arr_unit)):  # обьеденяем два списка в один вложенный список [['Алекс 8', 'Выпил 8'], ['Абросимова 9', 'Сьел 9'], [' Алекс 7', ' Вдохнул 7']]
            inter_arr_displey = str(int_arr_unit[i]) + ' ' + str(int_arr_task[i])
            self.list_unit_and_task_to_display.append(inter_arr_displey)
        # это обьединялка в один словарь self.list_unit_and_task_to_display{}
        for unit in self.list_unit_and_task_to_display:  # пробегаем по словарю передаем в программу
            self.listbox.insert(END, unit)

    def timer(self):
        global timer_after_id, count_timer
        timer_after_id = root.after(1000, self.timer) # таймер срабатывет каждые 1000 миллисекунд или 1 секунда
        count_timer += 1
        print(count_timer)
        if count_timer == self.trigger_time: #
            self.work_unit()
            for key in self.list_unit_and_task:  # бежим по словарю проверяем остались  ли не выполненные задачи остались ли не пустые value
                if self.list_unit_and_task[key] != []:  # останавливаем работу когда все задачи удалены
                    self.count_work_unit += 1
                    print('turn on')
                if self.count_work_unit == 0: # если 0 значит задач нет
                    root.after_cancel(timer_after_id) # останавливаем работу когда все задачи удалены
                    print('turn off')
                count_timer = 0
                self.update_display()
                self.count_work_unit = 0


    def work_unit(self):  # моделируем работу # на каждое срабатывание таймера бежим по рабочему словарю вычитаем из сложности первой задачи производительность юнита

        for key in self.list_unit_and_task:  # бежим по словарю
            if self.list_unit_and_task[key] == []:
                continue
            lvl_unit = int(key[-2:])  # вытаскиваем из кей значения производительности юнита от строка поэтому тащим срез
            lvl_first_task = int(self.list_unit_and_task[key][0][-3:])  # вытаскиваем производительность задачи , она тоже строка поэтому срез
            rest_of_task = lvl_first_task - lvl_unit  # минусуем из сложности производительность
            if rest_of_task <= 0:  # если задача выполнена те сложность меньше нуля
                self.list_ready_task = []
                self.list_ready_task.append('Исполнитель' + ' ' + key + ' ' + 'Задача' + ' ' + self.list_unit_and_task[key][0])
                for i in self.list_ready_task:
                    self.listbox_ready_task.insert(END, i)
                print(self.list_ready_task)
                self.list_unit_and_task[key].pop(0)  # удаляем задачу , она первая в массиве
            if rest_of_task > 0:
                inter_list_unit_and_task = self.list_unit_and_task[key][0][:-3]
                inter_list_unit_and_task_1 = inter_list_unit_and_task + ' ' + str(rest_of_task)
                self.list_unit_and_task[key][0] = inter_list_unit_and_task_1

    def pause_timer(self):
        root.after_cancel(timer_after_id)


class WindowTask():
    def __init__(self, main):
        self.field_result = Label(main, height=25, width=55)  # список с пуктами из листа list
        self.field_call = Label(main, text='Список задач', width=18, font=10, justify=LEFT)
        self.field_call.grid(row=0, column=1)
        self.field_result.grid(row=1, column=1)
        self.window_unit = WindowUnit(main)
        main.bind('<Button-1>', self.click_on_key)

    def click_on_key(self, event):
        cursor = list(self.window_unit.listbox.curselection())  # Метод   curselection()   позволяет   получить   в   виде   кортежа   индексы   выбранных   элементов экземпляра Listbox.
        for keys in cursor:
            # чтобы сделать в столбик вместо  Label работать с классом Listbox
            inter_list_unit_and_task = list(self.window_unit.list_unit_and_task.values())  # можно отобразить список задач без {} фигурных скобок инф в Tkinter2
            if True:
                self.field_result['text'] = inter_list_unit_and_task[keys]


# class WindowWork():
#     def __init__(self, main):
#         self.listbox_ready_task = Listbox(main, height=25, width=35, selectmode=EXTENDED)  # список с пунктами из листа list
#         self.list_ready_task = []  # список пунктов в списке
#         for i in self.list_ready_task:
#             self.listbox_ready_task.insert(END, i)
#         self.field_call_ready_task = Label(main, text='Выполненные задачи', width=17, font=10, justify=LEFT)
#         self.field_call_ready_task.grid(row=0, column=2)
#         self.listbox_ready_task.grid(row=1, column=2)


class Unit():  # класс исполнитель
    def __init__(self, sum=3, min_speed=30, max_speed=99):
        self.sum_unit = sum  # количество исполнителей
        self.min_speed_unit = min_speed  # мин производительность
        self.max_speed_unit = max_speed  # макс производительность

    def unit_generate(self):  # генерируем список исполнитерлей вида "Вася 5" случайным образом, где вася имя спонителя а 5 его производительность
        unit_names = ('Варвара', 'Вася', 'Наталья', 'Лидия', 'Федор', 'Петя', 'Агафона', 'Алла', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Пол', 'Мария', 'Тор')
        self.arr_unit = []
        for i in range(self.sum_unit):
            self.arr_unit.append("".join(random.choice(unit_names) + " " + str(random.randint(self.min_speed_unit, self.max_speed_unit))))


class Task():  # класс задачи
    def __init__(self, sum=10, min_complex=200, max_complex=250):
        self.sum_task = sum  # количество задач
        self.min_complexity_task = min_complex  # мин сложность задачи
        self.max_complexity_task = max_complex  # макс сложность задачи

    def task_generate(self):  # генерируем список задач вида "лудит  5" случайным образом, где Лудит вид задачи а 5 ее сложность
        task_names = ('Пашет', 'Сеет', 'Собирает', 'Починяет', 'Лудит', 'Паяяет', 'Культивирует', 'Копает', 'Закапывает', 'Откапывает', 'Режет', 'Чистит', 'Полирует', 'Выращивает')
        self.arr_task = []
        for i in range(self.sum_task):
            self.arr_task.append("".join(random.choice(task_names) + " " + str(random.randint(self.min_complexity_task, self.max_complexity_task))))


class Setting():  # окно настройка
    def __init__(self, main):
        self.button_set = Button(main, text='Setting', width=16, font=10, command=self.window_setting)
        self.button_set.grid(row=3, column=2)

    def window_setting(self):  # открываем окно с настройкаами
        self.window_open = Toplevel()  # инициализируем новое окно
        self.window_open.title('Setting')  # титул окна
        self.window_open.geometry('800x200')  # размер окна
        # время срабатывания таймера
        self.field_timer_trigger = Label(self.window_open, text='Время срабатывания таймера. сек ', borderwidth=3, width=40, font=10).grid(row=0, column=0)  # название поля ввода
        self.entry_timer_trigger = Entry(self.window_open, width=8, font=15).grid(row=0, column=1)  # создаем окно ввода
        # минимальное и максимальное количество исполнителей
        self.field_number_unit_max = Label(self.window_open, text='Количество исполнителей. Максимальное:', justify='left', borderwidth=3, width=40, font=10).grid(row=1, column=0)  # название поля ввода
        self.field_number_unit_max = Entry(self.window_open, width=8, font=15).grid(row=1, column=1)  # создаем окно ввода
        self.field_number_unit_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right').grid(row=1, column=2)  # название поля ввода
        self.field_number_unit_min = Entry(self.window_open, width=8, font=15).grid(row=1, column=3)  # создаем окно ввода
        # минимальная и максимальная производительность исполнителя
        self.field_level_perform_max = Label(self.window_open, text='Производительность исполнителя. Макс:', borderwidth=3, width=40, font=10, justify='right').grid(row=2, column=0)  # название поля ввода
        self.field_level_perform_max = Entry(self.window_open, width=8, font=15).grid(row=2, column=1)  # создаем окно ввода
        self.field_level_perform_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right').grid(row=2, column=2)  # название поля ввода
        self.field_level_perform_min = Entry(self.window_open, width=8, font=15).grid(row=2, column=3)  # создаем окно ввода
        # минимальное и максимальное количество задач
        self.field_amount_task_max = Label(self.window_open, text='Количество задач. Макс:', borderwidth=3, width=40, font=10, justify='right').grid(row=3, column=0)  # название поля ввода
        self.field_amount_task_max = Entry(self.window_open, width=8, font=15).grid(row=3, column=1)  # создаем окно ввода
        self.field_amount_task_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right').grid(row=3, column=2)  # название поля ввода
        self.field_amount_task_min = Entry(self.window_open, width=8, font=15).grid(row=3, column=3)  # создаем окно ввода
        # минимальная и максимальная сложность задачи
        self.field_complexity_task_max = Label(self.window_open, text='Сложность задач. Макс:', borderwidth=3, width=40, font=10, justify='right').grid(row=4, column=0)  # название поля ввода
        self.field_complexity_task_max = Entry(self.window_open, width=8, font=15).grid(row=4, column=1)  # создаем окно ввода
        self.field_complexity_task_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right').grid(row=4, column=2)  # название поля ввода
        self.field_complexity_task_min = Entry(self.window_open, width=8, font=15).grid(row=4, column=3)  # создаем окно ввода
        # кнопки ок и кенсел
        self.button_ok = Button(self.window_open, text='OK', width=16, font=10).grid(row=5, column=0)  # создаем кнопку ОК
        self.button_cancel = Button(self.window_open, text='Cancel', width=16, font=10, command=self.close_win_setting).grid(row=5, column=1)  # создаем кнопку кенсел с командой закрытия окна

    def close_win_setting(self):  # функция закрывающая окно по кнопке cancel
        self.close_win_setting = self.window_open.destroy()  # команда закрывающая окно


window_unit = WindowUnit(root)
WindowTask = WindowTask(root)
#WindowWork = WindowWork(root)
ButtonSetting = Setting(root)

root.mainloop()

""" 1. формируем словарь ключи название юнита плюс его производительность
2. К ключу маассив с обьектами задач
3. Включаем таймер когда срабатывает, бежим по списку извлекаем производительность из ключа минусуем из сложности которую тоже извлекаем перезаписывааем элемпент массива """
