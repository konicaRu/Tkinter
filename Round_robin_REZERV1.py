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

        self.listbox_ready_task = Listbox(main, height=25, width=45, selectmode=EXTENDED)  # список выполненных задач с пунктами из листа list
        self.field_call_ready_task = Label(main, text='Выполненные задачи', width=25, font=10, justify=LEFT)
        self.field_call_ready_task.grid(row=0, column=2)
        self.listbox_ready_task.grid(row=1, column=2)

        self.button_new = Button(main, text='New', width=16, font=10, command=self.unit_and_task_arr)  # кнопка New на первом листе
        self.button_new.grid(row=3, column=0, sticky='s')  # расположение кнопки New
        self.button_pause = Button(main, text='Pause', width=16, font=10, command=self.pause_timer)
        self.button_pause.grid(row=3, column=1)
        self.button_new = Button(main, text='Exit', width=16, font=10, command=self.close_main_win)  # кнопка New на первом листе
        self.button_new.grid(row=4, column=2, sticky='n')  # расположение кнопки New
        # self.unit = Unit()  # ссылка на класс исполнители
        self.task = Task()  # ссылка на класс задачи
        self.setting = Setting(main) # ссылка на класс Setting
        self.trigger_time = 3  # время срабатывания
        self.list_unit_and_task = {}  # массив для хранения исполнителей и задач
        self.count_work_unit = 0  # счетчик остатка задач в функции work_unit
        self.timer_count_operations = 0 # счетчик количества срабатываний таймера


    def close_main_win(self):  # функция закрывающая окно по кнопке cancel
            root.destroy()  # команда закрывающая окно

    def unit_and_task_arr(self):  # формируем  два списока исполнителей и задач self.list_unit_and_task-для работы и self.list_unit_and_task_to_display для отображения
        self.unit_generate(self.sum_unit_min, self.sum_unit_max, self.min_speed_unit, self.max_speed_unit)  # запускаем в классе Unit функцию unit_generate(), формируем список исполнителей
        self.task.task_generate()  # # запускаем в классе Task функцию task_generate(), формируем список задач
        shift = 0
        for keys in self.arr_unit:  # формируем рабочий словарь  self.list_unit_and_task вида {'Ivan 7': ['Пашет', 'Лудит', 'Закапывает'], 'Vasya 5': ['Сеет', 'Паяяет', 'Откапывает']}
            self.list_unit_and_task[keys] = [self.task.arr_task[val] for val in range(shift, len(self.task.arr_task), len(self.arr_unit))]  # генератор списков в словаре
            # Первому ключу из self.unit.arr_unit присваивается первое значение из self.task.arr_task,
            # второму -- вторая и т. д. N+1 - я задача снова назначается первому ключу, и так далее по кругу.
            shift += 1
        # формируем отдельный словарь для отображения в программе  исполнитель и первая завдача в списке
        int_arr_unit = []
        for key in self.list_unit_and_task:  # формируем список из ключей
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:  # формируем список из первых задач
            print(self.list_unit_and_task)
            int_arr_task.append(self.list_unit_and_task[key][0])
        self.list_unit_and_task_to_display = []
        for i in range(len(int_arr_unit)):  # обьеденяем два списка в один вложенный список [['Алекс 8', 'Выпил 8'], ['Абросимова 9', 'Сьел 9'], [' Алекс 7', ' Вдохнул 7']]
            inter_arr_displey = str(int_arr_unit[i]) + ' ' + str(int_arr_task[i])
            self.list_unit_and_task_to_display.append(inter_arr_displey)
        # это обьединялка в один словарь self.list_unit_and_task_to_display{}
        for unit in self.list_unit_and_task_to_display:  # пробегаем по словарю передаем в программу
            self.listbox.insert(END, unit)
        self.timer(self.trigger_time)  # запускаем функцию работу таймера

    def unit_generate(self, sum_min=1, sum_max=3, min_speed=30, max_speed=99):  # генерируем список исполнитерлей вида "Вася 5" случайным образом, где вася имя спонителя а 5 его производительность
        self.sum_unit_min = sum_min  # количество исполнителей
        self.sum_unit_max = sum_max
        self.min_speed_unit = min_speed  # мин производительность
        self.max_speed_unit = max_speed  # макс производительность
        unit_names = ('Варвара', 'Вася', 'Наталья', 'Лидия', 'Федор', 'Петя', 'Агафона', 'Алла', 'Светлана', 'Рената', 'Анна', 'Алекс', 'Жанна', 'Пол', 'Мария', 'Тор')
        self.sum_unit = random.randint(self.sum_unit_min, self.sum_unit_max)
        self.arr_unit = []
        for i in range(self.sum_unit):
            self.arr_unit.append(random.choice(unit_names) + "  " + str(random.randint(self.min_speed_unit, self.max_speed_unit)))

    def update_display (self): # обновляем отображение в первом окне при срабатывани таймера
        self.listbox.delete(0, END) # очищаем self.listbox чтобы заново заполнить его
        int_arr_unit = []
        for key in self.list_unit_and_task:  # формируем список из ключей
            int_arr_unit.append(key)
        int_arr_task = []
        for key in self.list_unit_and_task:  # формируем список из первых задач
            if self.list_unit_and_task[key] == []: # предучматриваем момент если список задач уже пуст
                int_arr_task.append('') # завиваем место пробелом чтобы ниже не выскакивало на диапазон
            else:
                int_arr_task.append(self.list_unit_and_task[key][0])
        self.list_unit_and_task_to_display = []
        for i in range(len(int_arr_unit)):  # обьеденяем два списка в один вложенный список [['Алекс 8', 'Выпил 8'], ['Абросимова 9', 'Сьел 9'], [' Алекс 7', ' Вдохнул 7']]
            inter_arr_displey = str(int_arr_unit[i]) + ' ' + str(int_arr_task[i])
            self.list_unit_and_task_to_display.append(inter_arr_displey)
        # это обьединялка в один словарь self.list_unit_and_task_to_display{}
        for unit in self.list_unit_and_task_to_display:  # пробегаем по словарю передаем в программу
            self.listbox.insert(END, unit)

    def timer(self, timer_trigger=2):
        self.trigger_time = timer_trigger
        global timer_after_id, count_timer
        timer_after_id = root.after(1000, self.timer) # таймер срабатывет каждые 1000 миллисекунд или 1 секунда
        count_timer += 1
        print(count_timer)
        if count_timer == self.trigger_time: #
            self.timer_count_operations += 1 # счетчик наличия задач
            self.work_unit()
            for key in self.list_unit_and_task:  # бежим по словарю проверяем остались  ли не выполненные задачи остались ли не пустые value
                if self.list_unit_and_task[key] != []:  # останавливаем работу когда все задачи удалены
                    self.count_work_unit += 1 #  почему то не удаляет все задачи срабатывает раньше чем они удалены
                    print('turn on')
            if self.count_work_unit == 0: # если 0 значит задач нет
                self.update_display()
                root.after_cancel(timer_after_id) # останавливаем работу когда все задачи удалены
                print('turn off = ', self.list_unit_and_task)
                count_timer = 0
            if self.count_work_unit != 0:#продолжаем  работу если задачи еще остались
                self.update_display() # обновдяем первое окно
                self.count_work_unit = 0 #
                count_timer = 0

    def pause_timer(self):
        root.after_cancel(timer_after_id)

    def work_unit(self):  # моделируем работу # на каждое срабатывание таймера бежим по рабочему словарю вычитаем из сложности первой задачи производительность юнита

        for key in self.list_unit_and_task:  # бежим по словарю
            if self.list_unit_and_task[key] == []:
                continue
            lvl_unit = int(key[-3:])  # вытаскиваем из кей значения производительности юнита от строка поэтому тащим срез
            lvl_first_task = int(self.list_unit_and_task[key][0][-3:])  # вытаскиваем производительность задачи , она тоже строка поэтому срез
            rest_of_task = lvl_first_task - lvl_unit  # минусуем из сложности производительность
            if rest_of_task <= 0:  # если задача выполнена те сложность меньше нуля
                self.list_ready_task = []  # список выполненных задач
                self.list_ready_task.append('Работник-' + ' ' + key[:-3] + ', ' + 'Задача-' + ' ' + self.list_unit_and_task[key][0][:-3]+''+'t='+str(self.timer_count_operations))
                for i in self.list_ready_task:
                    self.listbox_ready_task.insert(END, i)
                print(self.list_ready_task)
                self.list_unit_and_task[key].pop(0)  # удаляем задачу , она первая в массиве
                #с вероятностью 50 % (выпадет 1 или 2) србатывает фукция сменя первых задач в списке по кругу def change_task
                work_unit_count_task = 0
                for key in self.list_unit_and_task:
                    if self.list_unit_and_task[key] != []:
                        work_unit_count_task +=1
                    if work_unit_count_task == len(self.list_unit_and_task) and random.randint(1, 2) == 2:
                         # с вероятностью 50 % (выпадет 1 или 2) србатывает фукция сменя первых задач в списке по кругу def change_task
                        self.change_task()
                        print('change_task', self.list_unit_and_task)
            if rest_of_task > 0:
                inter_list_unit_and_task = self.list_unit_and_task[key][0][:-3]
                inter_list_unit_and_task_1 = inter_list_unit_and_task + ' ' + str(rest_of_task)
                self.list_unit_and_task[key][0] = inter_list_unit_and_task_1

    def change_task(self):  # меняем в списке list_unit_and_task первые задачи местами
        count_task = 1
        count_key = 0
        arr_keep_keys = []
        for key in self.list_unit_and_task:
            arr_keep_keys.append(key)

        first_task = self.list_unit_and_task[arr_keep_keys[count_key]][0]
        self.list_unit_and_task[arr_keep_keys[count_key]].pop(0)
        for key in self.list_unit_and_task:
            if count_task == len(self.list_unit_and_task):
                if self.list_unit_and_task[key] == []:
                    self.list_unit_and_task[key].append(first_task)
                else:
                    self.list_unit_and_task[key][0] = first_task
                break
            if self.list_unit_and_task[key] == []:
                self.list_unit_and_task[key].append(self.list_unit_and_task[arr_keep_keys[count_task]][0])
                count_task += 1
                continue

            self.list_unit_and_task[key][0] = self.list_unit_and_task[arr_keep_keys[count_task]][0]
            self.list_unit_and_task[arr_keep_keys[count_task]].pop(0)
            count_task += 1



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


class Task():  # класс задачи
    def __init__(self, sum_min=10, sum_max=10,  min_complex=200, max_complex=250):
        self.sum_task_min = sum_min  # количество задач
        self.sum_task_max = sum_max  # количество задач
        self.min_complexity_task = min_complex  # мин сложность задачи
        self.max_complexity_task = max_complex  # макс сложность задачи

    def task_generate(self):  # генерируем список задач вида "лудит  5" случайным образом, где Лудит вид задачи а 5 ее сложность
        task_names = ('Пашет', 'Сеет', 'Собирает', 'Починяет', 'Лудит', 'Паяяет', 'Культивирует', 'Копает', 'Закапывает', 'Откапывает', 'Режет', 'Чистит', 'Полирует', 'Выращивает')
        self.sum_task = random.randint(self.sum_task_min, self.sum_task_max)
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
        self.field_timer_trigger = Label(self.window_open, text='Время срабатывания таймера. сек ', borderwidth=3, width=40, font=10)
        self.field_timer_trigger.grid(row=0, column=0)  # название поля ввода
        self.entry_timer_trigger = Entry(self.window_open, width=8, font=15)
        self.entry_timer_trigger.grid(row=0, column=1)  # создаем окно ввода

        # минимальное и максимальное количество исполнителей
        self.field_number_unit_max = Label(self.window_open, text='Количество исполнителей. Максимальное:', justify='left', borderwidth=3, width=40, font=10)
        self.field_number_unit_max.grid(row=1, column=0)  # название поля ввода
        self.field_number_unit_max = Entry(self.window_open, width=8, font=15)
        self.field_number_unit_max.grid(row=1, column=1)  # создаем окно ввода
        self.field_number_unit_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right')
        self.field_number_unit_min.grid(row=1, column=2)  # название поля ввода
        self.field_number_unit_min = Entry(self.window_open, width=8, font=15)
        self.field_number_unit_min.grid(row=1, column=3)  # создаем окно ввода
        # минимальная и максимальная производительность исполнителя
        self.field_level_perform_max = Label(self.window_open, text='Производительность исполнителя. Макс:', borderwidth=3, width=40, font=10, justify='right')
        self.field_level_perform_max.grid(row=2, column=0)  # название поля ввода
        self.field_level_perform_max = Entry(self.window_open, width=8, font=15)
        self.field_level_perform_max.grid(row=2, column=1)  # создаем окно ввода
        self.field_level_perform_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right')
        self.field_level_perform_min.grid(row=2, column=2)  # название поля ввода
        self.field_level_perform_min = Entry(self.window_open, width=8, font=15)
        self.field_level_perform_min.grid(row=2, column=3)  # создаем окно ввода
        # минимальное и максимальное количество задач
        self.field_amount_task_max = Label(self.window_open, text='Количество задач. Макс:', borderwidth=3, width=40, font=10, justify='right')
        self.field_amount_task_max.grid(row=3, column=0)  # название поля ввода
        self.field_amount_task_max = Entry(self.window_open, width=8, font=15)
        self.field_amount_task_max.grid(row=3, column=1)  # создаем окно ввода
        self.field_amount_task_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right')
        self.field_amount_task_min.grid(row=3, column=2)  # название поля ввода
        self.field_amount_task_min = Entry(self.window_open, width=8, font=15)
        self.field_amount_task_min.grid(row=3, column=3)  # создаем окно ввода
        # минимальная и максимальная сложность задачи
        self.field_complexity_task_max = Label(self.window_open, text='Сложность задач. Макс:', borderwidth=3, width=40, font=10, justify='right')
        self.field_complexity_task_max.grid(row=4, column=0)  # название поля ввода
        self.field_complexity_task_max = Entry(self.window_open, width=8, font=15)
        self.field_complexity_task_max.grid(row=4, column=1)  # создаем окно ввода
        self.field_complexity_task_min = Label(self.window_open, text='Минимальное:', borderwidth=3, width=12, font=10, justify='right')
        self.field_complexity_task_min.grid(row=4, column=2)  # название поля ввода
        self.field_complexity_task_min = Entry(self.window_open, width=8, font=15)
        self.field_complexity_task_min.grid(row=4, column=3)  # создаем окно ввода
        # кнопки ок и кенсел
        self.button_ok = Button(self.window_open, text='OK', width=16, font=10, command=self.transit_date).grid(row=5, column=0)  # создаем кнопку ОК
        self.button_cancel = Button(self.window_open, text='Cancel', width=16, font=10, command=self.close_win_setting).grid(row=5, column=1)  # создаем кнопку кенсел с командой закрытия окна

    def transit_date(self):

            WindowUnit.trigger_time = int(self.entry_timer_trigger.get())
            WindowUnit.sum_unit_max = int(self.field_number_unit_max.get())
            WindowUnit.sum_unit_min = int(self.field_number_unit_min.get())
            WindowUnit.min_speed_unit = int(self.field_level_perform_min.get())
            WindowUnit.max_speed_unit = int(self.field_level_perform_max.get())
            Task.sum_task_min =  int(self.field_amount_task_min.get()) # количество задач
            Task.sum_task_max =  int(self.field_amount_task_max.get()) # количество задач
            Task.min_complexity_task = int(self.field_complexity_task_min.get())  # мин сложность задачи
            Task.max_complexity_task =  int(self.field_complexity_task_max.get())# макс сложность задачи


def close_win_setting(self):  # функция закрывающая окно по кнопке cancel
            self.window_open.destroy()  # команда закрывающая окно


window_unit = WindowUnit(root)
WindowTask = WindowTask(root)
ButtonSetting = Setting(root)



root.mainloop()

""" 1. формируем словарь ключи название юнита плюс его производительность
2. К ключу маассив с обьектами задач
3. Включаем таймер когда срабатывает, бежим по списку извлекаем производительность из ключа минусуем из сложности которую тоже извлекаем перезаписывааем элемпент массива """
