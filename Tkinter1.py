"""Напишите простую программу, которая работает с окнами, кнопками, списками, меню, флажками (Checkbox) переключателями (Radio)
и текстовыми полями ввода, включая многострочные, чтобы ко всем таким полям управления были привязаны какие-то реакции
 (например щелчок на кнопке или переключение чекбокса — в текстовом поле выводится сообщение)"""
# Для   выравнивания   строки   по   центру   в   текстовом   поле  используется  свойство   justify   со
# значением CENTER lflf.
from tkinter import *

root = Tk()
root.title('Пример приложения')  # надпись на верху
root.geometry('400x600+300+200')  # ширина=500, высота=400, x=300, y=200 размер окна
root.resizable(True, False)  # размер окна может быть изменён только по горизонтали


class BinaryConverter():  # класс для конвертера в 10 чную систему
    def __init__(self, main):
        self.field_enter = Entry(main, width=8, font=15)  # создаем окно ввода
        self.button_converter = Button(main, text='Конвертировать', width=15, font=10, command=self.calculate_binary)  # создаем кнопку конвертить
        self.field_result = Label(main, borderwidth=3, width=25, font=15)  # сождаем поле где будет высвечиваться результат
        self.field_call = Label(main, text='Конвертер в двоичную систему', borderwidth=1, width=27, font=15)  # создаем поле с названием конвертера
        # расположение полей
        self.field_call.pack()
        self.field_enter.pack()
        self.button_converter.pack()
        self.field_result.pack()


    def calculate_binary(self):  # фукнкция преобразования
        try:
            self.field_result['text'] = bin(int(self.field_enter.get()))[2:]  # получаем данные из поля преобразуем в 10 систему и отбрасываем 2 знака впереди лишнии
        except ValueError:
            self.field_result['text'] = 'Неверно: Введите цифры'


class ListOfCities():
    def __init__(self, main):
        self.listbox = Listbox(main, height=5, width=20, selectmode=EXTENDED)  # список с пуктами из листа list
        self.list = ["Москва", "Санкт-Петербург", "Саратов", "Омск"]  # список пунктов в списке
        for i in self.list:
            self.listbox.insert(END, i)

        self.field_call = Label(main, text='Год основания городов', width=27, font=15)
        self.field_result = Label(main, width=27, font=15)
        self.state_varible = BooleanVar()
        self.state_varible.set(0)
        self.switch_digit = Checkbutton(main, text='Отобразить римскими числами', variable=self.state_varible, onvalue=1, offvalue=0)  # строчка с галкой

        self.field_call.pack()
        self.listbox.pack()
        self.field_result.pack()
        self.switch_digit.pack()

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


class ManyStrok():
    def __init__(self, main):
        self.field_text = Text(main, width=25, height=5, bg="Snow", fg='Navy', wrap=WORD)
        self.button_delete = Button(main, text='Удалить текст', width=15, font=10, command=self.delete_text)  # создаем кнопку конвертить
        self.field_call = Label(main, text='Удаляем введенный текст ', borderwidth=3, width=27, font=15)
        self.field_call.pack()
        self.field_text.pack()
        self.button_delete.pack()


    def delete_text(self):
        self.field_text.delete(1.0, END)


class PhoneBook():
    def __init__(self, main):
        self.field_call = Label(main, text='Мини телефонный справочник', width=27, font=15)
        self.state_varible = IntVar()
        self.state_varible.set(0)
        self.radio_button_vasya = Radiobutton(main, text='Вася', variable=self.state_varible, value=1, indicatoron=0, command=self.phone_book)  #
        self.radio_button_petya = Radiobutton(main, text='Петя', variable=self.state_varible, value=2, indicatoron=0, command=self.phone_book)  #
        self.radio_button_lesha = Radiobutton(main, text='Леша', variable=self.state_varible, value=3, indicatoron=0, command=self.phone_book)  #
        self.field_result = Label(main, width=27, font=15)
        self.field_call.pack()
        self.radio_button_vasya.pack()
        self.radio_button_petya.pack()
        self.radio_button_lesha.pack()
        self.field_result.pack()

    def phone_book(self):
        if self.state_varible.get() == 1:
            self.field_result['text'] = '+79999999999'
        if self.state_varible.get() == 2:
            self.field_result['text'] = '+02356998714'
        if self.state_varible.get() == 3:
            self.field_result['text'] = '+88999998714'

class UpMenu():
    def __init__(self, main):
        self.main_menu = Menu(root)
        main.configure(menu=self.main_menu)

        self.first_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label='Active', menu=self.first_menu)
        self.first_menu.add_command(label='New window', command=self.open_new_window)


    def open_new_window(self):
        self.window = Toplevel(root)
        self.name_window = Label(self.window, text='Привет, я новое окно')
        self.name_window.pack()

window_calculate = BinaryConverter(root)
window_cities = ListOfCities(root)
window_many_text = ManyStrok(root)
window_phone = PhoneBook(root)
menu = UpMenu(root)
root.mainloop()
