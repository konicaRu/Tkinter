from tkinter import *
import random
import time

root = Tk()
root.title('Round robin')  # надпись на верху
root.geometry('500x300+300+200')  # ширина=500, высота=400, x=300, y=200 размер окна
root.resizable(True, False)  # размер окна может быть изменён только по горизонтали


class Window_performer():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list_performer
        self.list_performer = {}  # список пунктов в списке
        # for i in self.list_performer:
        #     self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список исполнителей', width=18, font=10, justify=LEFT)
        self.field_call.grid(row=0, column=0)
        self.listbox.grid(row=1, column=0)

        self.button_new = Button(main, text='New', width=16, font=10, command=self.unit_arr) # кнопка New на первом листе
        self.button_new.grid(row=3, column=0, sticky='s') # расположение кнопки New
        self.unit = Unit() # исполнители
        self.task = Task() # количество исполнителей
        self.list_unit_and_task = {} # массив для хранения исполнителей и задач
    def unit_arr(self):
        self.unit.unit_generate()
        self.task.task_generate()
        shift = 0
        for keys in self.unit.arr_unit:
            self.list_unit_and_task[keys] = [self.task.arr_task[val] for val in range(shift, len(self.task.arr_task), len(self.unit.arr_unit))]
            shift += 1
        int_arr_unit = []
        for key in self.list_unit_and_task:
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:
            int_arr_task.append(self.list_unit_and_task[key][0])
        self.list_performer = dict(zip(int_arr_unit, int_arr_task))
        for key, values in self.list_performer.items():
           self.listbox.insert(END, key, values)

class Window_task():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list
        self.list = []  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список задач', width=18, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=1)
        self.listbox.grid(row=1, column=1)


class Window_work():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list
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
    def __init__(self, sum= 3, min_speed=1, max_speed=6):
        self.sum_unit = sum
        self.min_speed_unit = min_speed
        self.max_speed_unit = max_speed
    def unit_generate(self):
        unit_names = ('Варвара', 'Вася', 'Наталья', 'Лидия', 'Федор', 'Петя', 'Агафона', 'Алла', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Пол', 'Мария', 'Тор')
        self.arr_unit = []
        for i in range(self.sum_unit):
            self.arr_unit.append("".join(random.choice(unit_names) + " " + str(random.randint(self.min_speed_unit, self.max_speed_unit))))


class Task():  # класс задачи
    def __init__(self, sum= 3, min_complex=1, max_complex=6):
        self.sum_task = sum
        self.min_complexity_task = min_complex  # сложность задачи
        self.max_complexity_task = max_complex
    def task_generate(self):
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
        self.window_open.geometry('700x200')  # размер окна
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
#ButtonNew = New(root)
windowsper = Window_performer(root)
WindowTask = Window_task(root)
WindowWork = Window_work(root)

ButtonSetting = Setting(root)
timer = Timer(root)
unit = Unit(root)

root.mainloop()

""" 1. формируем словарь ключи название юнита плюс его производительность
2. К ключу маассив с обьектами задач
3. Включаем таймер когда срабатывает, бежим по списку извлекаем производительность из ключа минусуем из сложности которую тоже извлекаем перезаписывааем элемпент массива """
