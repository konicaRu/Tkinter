from tkinter import *

root = Tk()
root.title('Round robin')  # надпись на верху
root.geometry('500x300+300+200')  # ширина=500, высота=400, x=300, y=200 размер окна
root.resizable(True, False)  # размер окна может быть изменён только по горизонтали


class window_performer():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list
        self.list = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список исполнителей', width=18, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=0)
        self.listbox.grid(row=1, column=0)


class window_task():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list
        self.list = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список задач', width=18, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=1)
        self.listbox.grid(row=1, column=1)


class window_work():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=25, selectmode=EXTENDED)  # список с пуктами из листа list
        self.list = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)
        self.field_call = Label(main, text='Список работ', width=15, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=2)
        self.listbox.grid(row=1, column=2)


class New():
    def __init__(self, main):
        self.button_new = Button(main, text='New', width=16, font=10)
        self.button_new.grid(row=3, column=0, sticky='s')


class Setting():  # окно настройка
    def __init__(self, main):
        self.button_set = Button(main, text='Setting', width=16, font=10, command=self.window_set)
        self.button_set.grid(row=3, column=2)

    def window_set(self):  # открываем окно с настройкаами
        self.window_open = Toplevel()  # инициализируем новое окно
        self.window_open.title('Setting')  # титул окна
        self.window_open.geometry('700x200')  # размер окна
        # время срабатывания таймера
        self.field_timer = Label(self.window_open, text='Время срабатывания таймера. сек ', borderwidth=3, width=40, font=10).grid(row=0, column=0)  # название поля ввода
        self.entry_timer = Entry(self.window_open, width=8, font=15).grid(row=0, column=1)  # создаем окно ввода
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
# кнопки ок и кенсел
        # self.button_ok = Button(self.window_open, text='OK', width=16, font=10).grid(row=1, column=0)  # создаем кнопку ОК
        # self.button_cancel = Button(self.window_open, text='Cancel', width=16, font=10, command=self.close_win_setting).grid(row=2, column=0)  # создаем кнопку кенсел с командой закрытия окна

    def close_win_setting(self):  # функция закрывающая окно по кнопке кенсел
        self.close_win_setting = self.window_open.destroy()  # команда закрывающая окно


class Unit():  # класс исполнитель
    def __init__(self, name, speed, arr_task):
        self.name_unit = name
        self.speed_unit = speed
        self.task_unit = arr_task  # []


class Task():  # класс задачи
    def __init__(self, name, complex):
        self.name_task = name
        self.complexity_task = complex  # сложность задачи


WindowPerformer = window_performer(root)
WindowTask = window_task(root)
WindowWork = window_work(root)
ButtonNew = New(root)
ButtonSetting = Setting(root)

root.mainloop()
