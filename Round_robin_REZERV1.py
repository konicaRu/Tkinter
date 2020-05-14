from tkinter import *
import random
import time

root = Tk()
root.title('Round robin')  # надпись на верху
root.geometry('600x300+300+200')  # ширина=500, высота=400, x=300, y=200 размер окна
root.resizable(True, False)  # размер окна может быть изменён только по горизонтали


class WindowUnit():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list_performer
        self.field_call = Label(main, text='Список исполнителей', width=18, font=10, justify=LEFT)
        self.field_call.grid(row=0, column=0)
        self.listbox.grid(row=1, column=0)

        self.button_new = Button(main, text='New', width=16, font=10, command=self.unit_and_task_arr)  # кнопка New на первом листе
        self.button_new.grid(row=3, column=0, sticky='s')  # расположение кнопки New
        self.unit = Unit()  # ссылка на класс исполнители
        self.task = Task()  # ссылка на класс задачи
        self.list_unit_and_task = {}  # массив для хранения исполнителей и задач

    def unit_and_task_arr(self): # формируем  два списока исполнителей и задач self.list_unit_and_task-для работы и self.list_unit_and_task_to_display для отображения
        self.unit.unit_generate()  # запускаем в классе Unit функцию unit_generate(), формируем список исполнителей
        self.task.task_generate()  # # запускаем в классе Task функцию task_generate(), формируем список задач
        shift = 0
        for keys in self.unit.arr_unit:  # формируем рабочий словарь  self.list_unit_and_task вида {'Ivan 7': ['Пашет', 'Лудит', 'Закапывает'], 'Vasya 5': ['Сеет', 'Паяяет', 'Откапывает']}
            self.list_unit_and_task[keys] = [self.task.arr_task[val] for val in range(shift, len(self.task.arr_task), len(self.unit.arr_unit))]  # генератор списков в словаре
            shift += 1
        # формируем отдельный словарь для отображения в программе  исполнитель и первая завдача в списке
        int_arr_unit = []
        for key in self.list_unit_and_task:  # формируем список из ключей
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:  # формируем список из первых задач
            int_arr_task.append(self.list_unit_and_task[key][0])  # обьеденяем два списка в словарь
        self.list_unit_and_task_to_display = []
        for i in range(len(int_arr_unit)):
            inter_arr_displey =[str(int_arr_unit[i]) +' '+ str(int_arr_task[i])]
            self.list_unit_and_task_to_display.append(inter_arr_displey)
           # это обьединялка в один словарь self.list_unit_and_task_to_display{}
        for unit in self.list_unit_and_task_to_display:  # пробегаем по словарю передаем в программу
            self.listbox.insert(END, unit)


class WindowTask():
    def __init__(self, main):
        self.field_result = Label(main, height=5, width=25)  # список с пуктами из листа list
        self.field_call = Label(main, text='Список задач', width=18, font=10, justify=LEFT)
        self.field_call.grid(row=0, column=1)
        self.field_result.grid(row=1, column=1)
        self.window_unit = WindowUnit(main)
        main.bind('<Button-1>', self.click_on_key)

    def click_on_key(self, event):
        cursor = list(self.window_unit.listbox.curselection())  # Метод   curselection()   позволяет   получить   в   виде   кортежа   индексы   выбранных   элементов экземпляра Listbox.
        for keys in cursor:
            print(cursor)
            print(keys)
            inter_list_unit_and_task = list(self.window_unit.list_unit_and_task.values())
            if True :
                self.field_result['text'] = inter_list_unit_and_task[keys]



class WindowWork():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пунктами из листа list
        self.list = []  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список работ', width=15, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=2)
        self.listbox.grid(row=1, column=2)


# class New():
#     def __init__(self, main):
#         self.button_new = Button(main, text='New', width=16, font=10, command=self.unit_arr)
#         self.button_new.grid(row=3, column=0, sticky='s')
#         self.arr_unit = Window_performer(main).list_performer
#
#     def unit_arr(self):
#         for i in range(8):
#             self.arr_unit.insert(END, i)


class Unit():  # класс исполнитель
    def __init__(self, sum=3, min_speed=1, max_speed=6):
        self.sum_unit = sum  # количество исполнителей
        self.min_speed_unit = min_speed  # мин производительность
        self.max_speed_unit = max_speed  # макс производительность

    def unit_generate(self):  # генерируем список исполнитерлей вида "Вася 5" случайным образом, где вася имя спонителя а 5 его производительность
        unit_names = ('Варвара', 'Вася', 'Наталья', 'Лидия', 'Федор', 'Петя', 'Агафона', 'Алла', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Пол', 'Мария', 'Тор')
        self.arr_unit = []
        for i in range(self.sum_unit):
            self.arr_unit.append("".join(random.choice(unit_names) + " " + str(random.randint(self.min_speed_unit, self.max_speed_unit))))


class Task():  # класс задачи
    def __init__(self, sum=10, min_complex=50, max_complex=300):
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


class Timer():  # класс таймер
    def __init__(self, main):
        self.count_timer = 0
        self.response_time = 5

    def timer(self):
        while self.count_timer < self.response_time:
            time.sleep(1)  # in seconds
            self.count_timer += 1
            print(self.count_timer, type(self.count_timer), type(self.response_time))


# class GenereteRandom():
#     first_names = ('Варвара', 'Анникова', 'Наталья', 'Лидия', 'Федор', 'Якуба', 'Агафона', 'Римма', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Ким', 'Мария', 'Марфа')
#
#     last_names = ('Юневича', 'Гайдукова', 'Мухова', 'Левченко', 'Щербатыха', 'Львова', 'Щитта', 'Яндуткина', 'Шелыгина', 'Ахременко', 'Абросимова', 'Аронова', 'Трухина', 'Оспищева')
#
#     name_group = "".join(random.choice(first_names) + " " + random.choice(last_names))
#     # group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3)) генерировать количество
#     # group=[" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))] генерировать количество в массив
#
#     task_first_names = ('Пашет', 'Сеет', 'Собирает', 'Починяет', 'Лудит', 'Паяяет', 'Культивирует', 'Копает', 'Закапывает', 'Откапывает', 'Режет', 'Чистит', 'Полирует', 'Выращивает', 'Боронует', 'Удобряет')
#     task_last_names = ('рис', 'гречку', 'яблоки', 'примус', 'картошку', 'яму', 'землю', 'помидоры', 'огурцы', 'детали', 'репку', 'машину', 'трактор', 'вишню')
#
#     task_group = "".join(random.choice(task_first_names) + " " + random.choice(task_last_names))
#     # group=" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3)) генерировать количество
#     # group=[" ".join(random.choice(first_names)+" "+random.choice(last_names) for _ in range(3))] генерировать количество в массив
#     print(name_group, task_group)
# ButtonNew = New(root)
windowsper = WindowUnit(root)
WindowTask = WindowTask(root)
WindowWork = WindowWork(root)

ButtonSetting = Setting(root)
timer = Timer(root)
unit = Unit(root)

root.mainloop()

""" 1. формируем словарь ключи название юнита плюс его производительность
2. К ключу маассив с обьектами задач
3. Включаем таймер когда срабатывает, бежим по списку извлекаем производительность из ключа минусуем из сложности которую тоже извлекаем перезаписывааем элемпент массива """
