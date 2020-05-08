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


class Setting():
    def __init__(self, main):
        self.button_set = Button(main, text='Setting', width=16, font=10, command=self.window_set)
        self.button_set.grid(row=3, column=2)

    def window_set(self):
       self.window_open = Toplevel()
       self.window_open.geometry('400x200')


class Performer():
    def __init__(self, name, arr_task):
        self.name_performer = name
        self.task_performer = arr_task #[]


WindowPerformer = window_performer(root)
WindowTask = window_task(root)
WindowWork = window_work(root)
ButtonNew = New(root)
ButtonSetting = Setting(root)

root.mainloop()
