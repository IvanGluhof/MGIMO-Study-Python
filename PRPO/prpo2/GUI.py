# Libs
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
# My Modules
from shop import MyShop
from bot   import intelli_bot
from utils import *

class GUI:
    # menu array
    OptionList = [
        'Об авторе',
        'О программе',
        'Тренировка бота',
        'В магазин',
        'Выход'
    ]
    # root object to handle GUI
    root = Tk()
    tabControl = ttk.Notebook(root)

    bot_train_tabs = False

    def __init__(self):
        self.root.title("Магазин 2.0")

        # grid settings
        mainframe = Frame(self.root)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.pack(pady=100, padx=100)

        # tkinter variable
        tk_var = StringVar(self.root)

        # default option
        tk_var.set( self.OptionList[0] )

        menu = OptionMenu(mainframe, tk_var, *self.OptionList)
        menu.config(width=30, font=('Helvetica', 12))

        Label(mainframe, text="Сделайте выбор", font=('Helvetica', 12)).grid(row=1, column=1)

        menu.grid(row=2, column=1)

        # on change drop down value
        def menu_choice(*args):
            self.handle_choice(tk_var.get())

        # link function to change drop down
        tk_var.trace('w', menu_choice)

        self.root.mainloop()

    def handle_choice(self, choice):
        for case in switch(choice):
            if case(self.OptionList[0]): self.OutputMessageBox(self.OptionList[0], "Глухов И.Д.");                   break;
            if case(self.OptionList[1]): self.OutputMessageBox(self.OptionList[0], "Это магазин по подбору товара"); break;
            if case(self.OptionList[2]): self.BotTrain();                                                            break;
            if case(self.OptionList[3]): self.GoShop();                                                              break;
            if case(self.OptionList[4]): exit(0);                                                                    break;
            if case(): break  # default

    def OutputMessageBox(self, title, msg):
        messagebox.showinfo(title=title, message=msg)

    def BotTrain(self):
        shop = MyShop("myShop.xml")
        shop.addSampleData(200, 3, 4)
        df = shop.getTrainingData()

        tab1 = ttk.Frame(self.tabControl)
        tab2 = ttk.Frame(self.tabControl)
        tab3 = ttk.Frame(self.tabControl)

        if( self.bot_train_tabs == True ):
            ttk.Label(tab1, text="str").grid(column=0, row=0, padx=30, pady=30)
            ttk.Label(tab2, text=shop.print_products()).grid(column=0, row=0, padx=30, pady=30)
            ttk.Label(tab3, text=str(df)).grid(column=0, row=0, padx=30, pady=30)
        else:
            # Materials tab
            self.tabControl.add(tab1, text='Материалы')
            self.tabControl.pack(expand=1, fill="both")
            ttk.Label(tab1, text=shop.print_materials()).grid(column=0, row=0,padx=30, pady=30)

            # Products tab
            self.tabControl.add(tab2, text='Продукты')
            self.tabControl.pack(expand=1, fill="both")
            ttk.Label(tab2, text=shop.print_products()).grid(column=0, row=0,padx=30, pady=30)

            # df tab
            self.tabControl.add(tab3, text='DF')
            self.tabControl.pack(expand=1, fill="both")
            ttk.Label(tab3, text=str(df)).grid(column=0, row=0, padx=30, pady=30)

            self.bot_train_tabs = True

    def GoShop(self):
        # Создаем магазин товаров
        myShop = MyShop("myShop.xml")
        # myShop.printProduct()

        # Добавляем тестовые данные
        myShop.addSampleData(200, 2, 2)
        # myShop.printProduct()
        myShop.saveXML("new.xml")

        # Создаем бота
        bot = intelli_bot(myShop)
        # обучаем бота
        bot.botTraining(1)

        window = tk.Tk()
        window.title("Подбор товара")

        tk.Label(window, text="Возраст").grid(row=0)
        tk.Label(window, text="Пол(M/F)").grid(row=1)
        tk.Label(window, text="Адрес").grid(row=2)
        tk.Label(window, text="Категория").grid(row=3)
        tk.Label(window, text="Цена").grid(row=4)
        tk.Label(window, text="Цвет").grid(row=5)
        tk.Label(window, text="Сезон").grid(row=6)
        tk.Label(window, text="Материал").grid(row=7)

        age      = tk.Entry(window)
        sex      = tk.Entry(window)
        address  = tk.Entry(window)
        category = tk.Entry(window)
        price    = tk.Entry(window)
        color    = tk.Entry(window)
        season   = tk.Entry(window)
        material = tk.Entry(window)

        age.grid(row=0, column=1)
        sex.grid(row=1, column=1)
        address.grid(row=2, column=1)
        category.grid(row=3, column=1)
        price.grid(row=4, column=1)
        color.grid(row=5, column=1)
        season.grid(row=6, column=1)
        material.grid(row=7, column=1)

        def get_entry_fields():
            gp = bot.getUserChoice_GUI(age.get(),
                                       sex.get(),
                                       address.get(),
                                       category.get(),
                                       price.get(),
                                       color.get(),
                                       season.get(),
                                       material.get())
            pr = bot.getPrecigion(gp)
            str = "Ваш рекомендуемый товар: "
            str += pr
            self.OutputMessageBox("Результат", str)

        tk.Button(window,
                  text='Ввести',
                  command=get_entry_fields).grid(row=8,
                                                  column=1,
                                                  sticky=tk.W,
                                                  pady=4)

        tk.mainloop()
#end class GUI