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


        main.bind('<Button-1>', self.click_on_citi)
        """У функций-обработчиков, которые вызываются через bind(), а не через свойство command,
должен быть обязательный параметр event, через который передается событие."""

    def click_on_citi(self, event):
        if self.state_varible.get() == 1:
            cursor = list(self.listbox.curselection()) # Метод   curselection()   позволяет   получить   в   виде   кортежа   индексы   выбранных   элементов экземпляра Listbox.
            for our_cities in cursor:
                if self.list[our_cities] == "Москва":
                    self.field_result['text'] = 'MCXLVII год'
                if self.list[our_cities] == "Санкт-Петербург":
                    self.field_result['text'] = 'MDCCIII год'
                if self.list[our_cities] == "Саратов":
                    self.field_result['text'] = 'MDXC год'
                if self.list[our_cities] == "Омск":
                    self.field_result['text'] = 'MDCCXVI год'
        if self.state_varible.get() == 0:
            cursor = list(self.listbox.curselection())
            for our_cities in cursor:
                if self.list[our_cities] == "Москва":
                    self.field_result['text'] = '1147 год'
                if self.list[our_cities] == "Санкт-Петербург":
                    self.field_result['text'] = '1703 год'
                if self.list[our_cities] == "Саратов":
                    self.field_result['text'] = '1590 год'
                if self.list[our_cities] == "Омск":
                    self.field_result['text'] = '1716 год'

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
        self.field_call = Label(main, text='Список работ', width=18, font=10, justify=LEFT)

        self.field_call.grid(row=0, column=2)
        self.listbox.grid(row=1, column=2)





WindowPerformer = window_performer(root)
WindowTask = window_task(root)
WindowWork = window_work(root)



root.mainloop()