# Подключаемые библиотеки
import random  # Бибилотека для работы с random (рандомизатор)
import math  # Бибилотека мат. функций
import tkinter as tk  # GUI libs
from tkinter import filedialog  # file dialog lib


# custom switch в виде объекта
class switch(object):
  # Конструктор класса
  def __init__(self, value):
    self.value = value  # Искомое значение
    self.empty = False  # Пустые case'ы
  # end def __init__(self, value):

  # Итерация (для цикла for)
  def __iter__(self):
    yield self.case      # Возвращает один раз метод case
    raise StopIteration  # И завершает выполнение
  # end def __iter__(self):

  # Условия захода в case
  def case(self, *args):
    if self.empty or not args:
      return True
    elif self.value in args:
      self.empty = True
      return True
    else:
      return False
  # end def case(self, *args):
# end class switch(object):

# Общий класс для вызова всех заданий
class TasksAll:
  def __init__(self):
    self.__print_header()
    self.CallTask = int(input("Введите номер задания "))
    self.__choose_task()
  # end def __init__(self):

  # Вывод заголовка
  def __print_header(self):
    print(
      "------------------------------------------------------------------------------------------------------\n"
      "Глухов И.Д. - Задания\n"
      "1 - Задание 1 (Напишите код по следующему словесному алгоритму...)\n"
      "2 - Задание 2 (Напишите программу, которая бы выполняла следующие задачи...)\n"
      "3 - Задание 2 (Написать программу, которая меняет наибольший и наименьший элементы массива местами...)\n"
      "4 - Задание 3 (Даны три целых числа. Определите второе по величине из них...)\n"
      "5 - Задания из презентации 2\n"
      "6 - Задания из презентации 3\n"
      "9 - Доп. задание (Построить гистограмму распределения количества чисел по интервалам)\n"
      "------------------------------------------------------------------------------------------------------\n")
  # def __print_header(self):

  # Выбор задания
  def __choose_task(self):
    for case in switch(self.CallTask):
      if case(1): Task_1(); break;
      if case(2): Task_2(); break;
      if case(3):
        rnd_arr = Task_2_RandomArray(mode=1)
        rnd_arr.swap_min_max()
        break
      if case(4): Task_3();        break;
      if case(5): Tasks_PP2();     break;
      if case(6): Tasks_PP3();     break;
      if case(9): Aux_Histogram(); break;
      if case(): break  # default
  # end def __choose_task(self):
# end class All_Tasks:


###############################################################
# Задание 1                                                   #
# Напишите код по следующему словесному алгоритму...          #
# #############################################################
class Task_1:
  def __init__(self):
    self.__analyze(int(input("Ввести число от 1 до 9: ")))  # Считываем ввод, приводим к int
  # end def __init__(self):

  def __analyze(self, x):
    # Анализируем полученный результат
    bool_x1x3 = (x >= 1) and (x <= 3)  # 1) Если пользователь ввел число от 1 до 3 включительно, то ...
    bool_x4x6 = (x >= 4) and (x <= 6)  # 2) Если пользователь ввел число от 4 до 6 включительно, то ...
    bool_x7x9 = (x >= 7) and (x <= 9)  # 3) Если пользователь ввел число от 7 до 9, то ...
    # 4) Во всех остальных случаях выводить надпись "Ошибка ввода"
    self.__x1x3() if bool_x1x3 else (self.__x4x6(x)
                  if bool_x4x6 else (self.__x7x9(x)
                  if bool_x7x9 else print("Ошибка ввода")))
  # end def __analyze(self, x):

  def __x1x3(self):
    i = 0                                             # инициализируем перменную i
    s = str(input("Ввести строку: "))                 # считываем ввод в string
    n = int(input("Ввести число повторов строки: "))  # считываем ввод, приводим к int
    # Цикл
    while i < n:
      i = i + 1  # инкремент i
      print("Результат: ", s)  # вывод сообщения пользователю с результатом переменной s
  # end def __x1x3(self):

  def __x4x6(self, x):
    m = int(input("Ввести степень, в которую следует возвести число: "))  # считываем ввод, приводим к int
    print("Результат: ", x ** m)  # вывод сообщения пользователю с результатом переменной x
  # end def __x4x6(self, x):

  def __x7x9(self, x):
    i = 0
    while i < 10:
      i = i + 1
      x = x + 1
      print("Результат: ", x)
  # end def __x7x9(self, x):
# end class Task_1:

###############################################################
# Задание 2                                                   #
# Напишите программу, которая бы выполняла следующие задачи.. #
# #############################################################
class Task_2:
  def __init__(self):
    # выводила название программы "Общество в начале XXI века";
    # и запрашивала у пользователя его возраст;
    self.__analyze_age(int(input("|==========================|\n"
                                 "|Общество в начале XXI века|\n"
                                 "|==========================|\n\n"
                                 "Введите Ваш возраст: ")))
  # end def __init__(self):

  def __analyze_age(self, age):
    # boolean значения
    b_age_0_7    = (age > 0 ) and (age <= 7  )
    b_age_7_18   = (age > 7 ) and (age <= 18 )
    b_age_18_25  = (age > 18) and (age <= 25 )
    b_age_25_60  = (age > 25) and (age <= 60 )
    b_age_60_120 = (age > 60) and (age <= 120)
    b_age_0_120  = (age <= 0) or  (age >  120)
    # if ветвление
    # если пользователь вводит числа:
    for case in switch(True): # just for fun
      # от 0 до 7, то программа выводила надпись "Вам в детский сад";
      if case( b_age_0_7 ):
        print("Вам в детский сад");
        break;
      # от 7 до 18 - "Вам в школу";
      if case( b_age_7_18 ):
        print("Вам в школу");
        break;
      # от 18 до 25 - "Вам в профессиональное учебное заведение";
      if case( b_age_18_25 ):
        print("Вам в профессиональное учебное заведение");
        break;
      # от 25 до 60 - "Вам на работу";
      if case( b_age_25_60 ):
        print("Вам на работу");
        break;
      # от 60 до 120 – "Вам предоставляется выбор";
      if case( b_age_60_120 ):
        print("Вам предоставляется выбор");
        break;
      # меньше 0 и ("или") больше 120 – пятикратный вывод надписи "Ошибка! Это программа для людей!"
      if case( b_age_0_120 ):
        self.__print_err();
        break;
  # end def __analyze_age(self, age):

  def __print_err(self, i = 0):
    # цикл
    while i < 5: i += 1; print("Ошибка! Это программа для людей!");
  # end def __print_err(self, i=0):
# end class Task_2:


###############################################################
# Задание 2                                                   #
# Поменять местами макс. и мин. числа в массиве               #
# #############################################################
class Task_2_RandomArray:
  # Init with mode - auto or input
  def __init__(self, mode, size, top, bot):
    self.rnd_arr = []   # Инициализация массива
    self.size    = size # Инициализация значения размера массива
    self.top     = top  # Инициализация значения нижней границы массива
    self.bot     = bot  # Инициализация значения верхней границы массива
    self.__create(mode) # Создание рандмоного массива
  # end def __init__(self):

  # Метод для создание рандомного массива
  # Тип: private (закрытый)
  def __create(self, mode):
    if( mode == 1 ):
      self.size = int(input("Введите размер массива (от 2 до 100): "))
      if ((self.size > 1) and (self.size <= 100)):
        self.bot = int(input("Введите нижнюю границу массива: "))
        self.top = int(input("Введите верхнюю границу массива: "))
        if (self.bot < self.top):
          self.__generate(self.size, self.top, self.bot)
        else:
          exit("Ошибка: нижняя граница больше верхней")
      else:
        exit("Ошибка: неверное значение размера массива")
    else:
      if( (self.size > 1) and (self.size <= 1000000) ):
        if (self.bot < self.top):
          self.__generate(self.size, self.top, self.bot)
        else:
          exit("Ошибка: нижняя граница больше верхней")
      else:
        exit("Ошибка: неверное значение размера массива")
  # end def __create(self):

  # Метод для псевдо рандмоной генерации массива
  # Тип: private (закрытый)
  def __generate(self, size, top, bot):
    i = 0
    while i < size:
      self.rnd_arr.append(random.randint(bot, top))
      i += 1
    print("| Рандомный массив:  |")
    self.print()
  # end def __generate(self, size, top, bot):

  # Метод, меняющий местами максимальное и минимальное значения в массиве
  # Тип: public (открытый)
  def swap_min_max(self):
    max_num = self.rnd_arr[0]
    max_idx = 0
    min_num = self.rnd_arr[0]
    min_idx = 0
    for index, value in enumerate(self.rnd_arr):
      if (value >= max_num):
        max_num = value
        max_idx = index
        continue
      if (value <= min_num):
        min_num = value
        min_idx = index
        continue

    print('\n')
    print(f'Минимальное значение:  [', min_idx, '] =', min_num)
    print(f'Максимальное значение: [', max_idx, '] =', max_num)
    print('Меняю местами минимальное и ммксимальное значения')
    print('\n')

    self.rnd_arr[max_idx] = min_num
    self.rnd_arr[min_idx] = max_num

    print("| Изменённый массив:  |")
    self.print()
  # end def swap_min_max(self):

  # Метод, печатающий массив
  # Тип: public (открытый)
  def print(self):
    print("|--------------------|")
    for index, value in enumerate(self.rnd_arr):
      print(f'| [', index, '] =', value)
    print("|--------------------|")
  # end def print(self):
# end class RandomArray:


###############################################################
# Задание 3                                                   #
# Даны три целых числа. Определите второе по величине из них. #
# #############################################################
class Task_3():
  def __init__(self):
    # Рандомные значения
    v_rnd_1 = random.randint(-100, 100)
    v_rnd_2 = random.randint(-100, 100)
    v_rnd_3 = random.randint(-100, 100)

    # bool значения
    b_max_1 = (v_rnd_2 < v_rnd_1 < v_rnd_3) or (v_rnd_3 < v_rnd_1 < v_rnd_2)
    b_max_2 = (v_rnd_1 < v_rnd_2 < v_rnd_3) or (v_rnd_3 < v_rnd_2 < v_rnd_1)
    b_max_3 = (v_rnd_1 < v_rnd_3 < v_rnd_2) or (v_rnd_2 < v_rnd_3 < v_rnd_1)

    # Тернанрый if
    v_max_second = v_rnd_1 if b_max_1 else v_rnd_2 \
                           if b_max_2 else v_rnd_3 \
                           if b_max_3 else 0

    # Вывод реузультата
    print("Сгенерировано 3 случайных числа: ", v_rnd_1, v_rnd_2, v_rnd_3,
          "\nВторое по величине число: ", v_max_second)
# end class Task_3():

###############################################################
# Задания из презентации 2                                    #
# Тут без комментариев - не вижу смысла проставлять на каждую #
# строку по комментарию. И так всё тривиально                 #
# #############################################################
class Tasks_PP2():
  def __init__(self):
    for case in switch(int(input("1 - Задание B\n2 - Задание C\n3 - Задача A\n4 - Задача B\n5 - Задача C\n"))):
      # B
      if case(1): print("Вася\n\tпошел\n\t\tгулять"); break;
      # C
      if case(2): print("   Ж\n  ЖЖЖ\n ЖЖЖЖЖ\n НН НН \n ZZZZZ\n"); break;
      if case(3):
        a, b, c = map(int, input("Введите три целых числа: ").split());
        print("Числа: ", a,b,c, "\nСумма: ", a+b+c, "\nПроизведение: ", a*b*c, "\nСреднее арифметическое: ", float((a+b+c)/3));
        break;
      if case(4):
        print("Ввести координаты двух точек A и B")
        Ax, Ay = map(float, input("Ввести координаты точки A: ").split());
        Bx, By = map(float, input("Ввести координаты точки B: ").split());
        print("\nДлина отрезка AB ", math.sqrt(((Bx - Ax) ** 2) + \
                                               ((By - Ay) ** 2)));
        break;
      if case(5):
        a = random.randint(100, 999);
        print("Получено число: ", a, "\nЕго цифры: ", ((a//100)), ((a%100)//10), (a%10));  break;
      if case(): break  # default
  # end for
# end class Tasks_PP2()

###############################################################
# Задания из презентации 3                                    #
# Тут без комментариев - не вижу смысла проставлять на каждую #
# строку по комментарию. И так всё тривиально                 #
# #############################################################
class Tasks_PP3():
  def __init__(self):
    for case in switch(int(input("1  - Задача А\n"
                                 "2  - Задача B\n"
                                 "3  - Задача C\n"
                                 "4  - Задача A2\n"
                                 "5  - Задача B2\n"
                                 "6  - Задача C2\n"
                                 "7  - Задача A3\n"
                                 "8  - Задача B3\n"
                                 "9  - Задача-2 A\n"
                                 "10 - Задача-2 B\n"
                                 "11 - Задача-2 C\n"
                                 "12 - Задача A4\n"
                                 "13 - Задача B4\n"
                                 "14 - Задача C4\n"
                                 "15 - Задача А5\n"
                                 "16 - Задача B5\n"
                                 "17 - Задача C5\n"
                                 ))):
      if case(1):
        a, b, c = map(int, input("Введите три целых числа: ").split());
        print("Максимальное число ", (a if a > b else b if b > c else c));
        break;
      if case(2):
        arr = []
        a0, a1, a2, a3, a4 = map(int, input("Введите пять целых чисел: ").split());
        arr.append(a0)
        arr.append(a1)
        arr.append(a2)
        arr.append(a3)
        arr.append(a4)
        max = a0
        for a in arr:
          if a > max: max = a
        print("Максимальное число", max)
        break;
      if case(3):
        a1 = random.randint(10, 50); s1 = "Антона";
        a2 = random.randint(10, 50); s2 = "Бориса";
        a3 = random.randint(10, 50); s3 = "Виктора";
        print("Возраст", s1, ":", a1, "\nВозраст", s2,":", a2, "\nВозраст", s3, ":", a3)
        s_max = s1 if a1 > a2 else s2 if a2 > a3 else s3;
        print("Ответ:", s_max[:-1], "старше всех. ")
      if case(4):
        a, b, c = map(int, input("Введите три числа: ").split());
        if( a == b == c):
          print("Все числа одинаковые.")
        elif( a == b or a == c or b == c):
          print("Два числа одинаковые.")
        else:
          print("Нет одинаковых чисел.")
        break;
      if case(5):
        list = [
          "Январь",   # 1
          "Февраль",  # 2
          "Март",     # 3
          "Апрель",   # 4
          "Май",      # 5
          "Июнь",     # 6
          "Июль",     # 7
          "Август",   # 8
          "Сентябрь", # 9
          "Октябрь",  # 10
          "Ноябрь",   # 11
          "Декабрь",  # 12
        ]
        i = 1
        a = int(input("Введите номер месяца: "))
        if( a < 1 and a > 12 ): print("Неверный номер месяца.")
        for month in list:
          if i == a:
            print(month)
            if( a > 1 and a < 3 or a == 12 ):
              print("Зима")
            elif( a > 2 and a < 6):
              print("Весна")
            elif( a > 5 and a < 9):
              print("Лето")
            elif( a > 8 and a < 12):
              print("Осень")
          i = i + 1
        break;
      if case(6):
        a = int(input("Введите возраст: "))
        if a > 120 or a < 1:
          print("Возраст некорректен")
          break;
        if(a == 1 or a%10 == 1):
          print("Вам", a, "год")
        elif( (a > 4 and a < 21) or (a > 24 and ((a%10 > 4 and a%10 < 10) or a%10 == 0) ) ):
          print("Вам", a, "лет")
        elif((a == 2 or a == 3 or a == 4) or (a%10 == 2 or a%10 == 3 or a%10 == 4) ):
          print("Вам", a, "года")
        break;
      if case(7):
        a, b = map(int, input("Введите два целых числа: ").split());
        if( a < 0 or b < 0 or a > b):
          print("Некорректный ввод")
          break;
        while(a < (b+1)):
          print(a, "*", a, "=", a*a)
          a = a + 1
        break;
      if case(8):
        negative = False
        a_n = 0
        b_n = 0
        result = 0
        a, b = map(int, input("Введите два целых числа: ").split());
        if(a < 0 and b > 0):
          a_n = -a
          b_n = b
          negative = True
        elif(b < 0 and a > 0):
          a_n = a
          b_n = -b
          negative = True
        else:
          a_n = a
          b_n = b
        i = 0
        print(a_n, b_n)
        while(i < b_n):
          result = result + a_n
          i = i + 1
        if(negative == True): result = -result
        print(a, "*", b, "=", result)
      # Алгоритм нахождения кол-ва разрядов числа и его числа по отдельности
      # Далее в заданиях использую копи-паст этого алгоритма
      if case(9):
        a = int(input("Введите натуральное число:\n "))
        num = 0
        del_del = 10
        while(True):
          if( a//del_del != 0 ):
            del_del=del_del*10
            num = num + 1
          else:
            break;
        cnt = num
        del_del = int(del_del/10)
        result = 0
        while(True):
          if(cnt == num):
            result = result + (a//del_del)
            del_del = int(del_del/10)
            cnt = cnt - 1
          elif(cnt == 0):
            result = result + ((a%10))
            break;
          else:
            result = result + ((a // del_del) % 10)
            del_del = int(del_del/10)
            cnt = cnt - 1
        print("Сумма цифр ", result)
        break;
      if case(10):
        a = int(input("Введите натуральное число:\n "))
        num = 0
        del_del = 10
        while(True):
          if( a//del_del != 0 ):
            del_del=del_del*10
            num = num + 1
          else:
            break;
        cnt = num
        del_del = int(del_del/10)
        curr_num = 0
        is_cons = False
        while(True):
          prev_num = curr_num
          if(cnt == num):
            curr_num = (a//del_del)
            if( curr_num == prev_num ): is_cons = True
            del_del = int(del_del/10)
            cnt = cnt - 1
          elif(cnt == 0):
            curr_num = ((a%10))
            if (curr_num == prev_num): is_cons = True
            break;
          else:
            curr_num = ((a // del_del) % 10)
            if (curr_num == prev_num): is_cons = True
            del_del = int(del_del/10)
            cnt = cnt - 1
        if(is_cons == True):
          print("Да")
        else:
          print("Нет")
        break;
      if case(11):
        a = int(input("Введите натуральное число:\n "))
        num = 0
        del_del = 10
        while(True):
          if( a//del_del != 0 ):
            del_del=del_del*10
            num = num + 1
          else:
            break;
        cnt = num
        del_del = int(del_del/10)
        is_two = False
        arr = []
        while(True):
          if(cnt == num):
            curr_num = (a//del_del)
            if(curr_num in arr): is_two = True
            arr.append(curr_num)
            del_del = int(del_del/10)
            cnt = cnt - 1
          elif(cnt == 0):
            curr_num = ((a%10))
            if (curr_num in arr): is_two = True
            arr.append(curr_num)
            break;
          else:
            curr_num = ((a // del_del) % 10)
            if (curr_num in arr): is_two = True
            arr.append(curr_num)
            del_del = int(del_del/10)
            cnt = cnt - 1
        if(is_two == True):
          print("Да")
        else:
          print("Нет")
        break;
      if case(12):
        range_bot = 10000
        range_top = 100000
        while(range_bot < range_top):
          if(range_bot % 133 == 125): print(range_bot)
          if(range_bot % 134 == 111): print(range_bot)
          range_bot = range_bot + 1
        break;
      if case(13):
        a = int(input("Введите натуральное число:\n "))
        num = 0
        del_del = 10
        while (True):
          if (a // del_del != 0):
            del_del = del_del * 10
            num = num + 1
          else:
            break;
        cnt = num
        del_del = int(del_del / 10)
        result = 0
        while (True):
          if (cnt == num):
            curr_num = (a // del_del)
            result = result + curr_num ** (num+1)
            del_del = int(del_del / 10)
            cnt = cnt - 1
          elif (cnt == 0):
            curr_num = ((a % 10))
            result = result + curr_num ** (num+1)
            break;
          else:
            curr_num = ((a // del_del) % 10)
            result = result + curr_num ** (num+1)
            del_del = int(del_del / 10)
            cnt = cnt - 1
        if (result == a):
          print("Число", a, "является числом Армстронга")
        else:
          print("Число", a, "не является числом Армстронга")
        break;
      if case(14):
        n = int(input("Введите N:\n "))
        cnt = 1
        sqrt = 0
        while(sqrt < (n+1)):
          sqrt = cnt * cnt
          # Тут можно было бы сделать динамичную проверку, но я думаю общая логика тут ясна
          if(sqrt % 1000000 == cnt or
             sqrt % 100000  == cnt or
             sqrt % 10000   == cnt or
             sqrt % 1000    == cnt or
             sqrt % 100     == cnt or
             sqrt % 10      == cnt): print(sqrt, cnt)
          cnt = cnt + 1
      if case(15):
        # Для диапазона больше 100000 начинается ад
        a, b = map(int, input("Введите границы диапазона: ").split());
        if( a > b ):
          print("Некорректный ввод")
          break;
        while(a < (b+1)):
          i = 2
          while(True):
            if(i == a):
              print(a)
              break;
            elif( a % i == 0 ):
              break;
            i = i + 1
          a = a + 1
        break;
      if case(16):
        case_a = 15
        case_b = 17
        case_c = 21
        total  = 185
        i = 0
        j = 0
        for i in range(total // (case_a + 1)):
          for j in range(total // (case_b + 1)):
            result = total - ((i * case_a) + (j * case_b))
            if(result >= 0 and result % case_c == 0):
              print(i, j, (result // case_c));
        break;
      # Это вообще ахтунг
      if case(17):
        n = int(input("Введите N:\n "))
        inc = 1
        while(inc < (n+1)):
          # Костыли костыльные
          if(inc > 0 and inc < 11):
            if(inc == 10):
              inc = inc + 1
              continue
            else:
              print(inc);
              inc = inc + 1
              continue;
          num = 0
          del_del = 10
          while (True):
            if (inc // del_del != 0):
              del_del = del_del * 10
              num = num + 1
            else:
              break;
          cnt = num
          del_del = int(del_del / 10)
          while (True):
            if (cnt == num):
              curr_num = (inc // del_del)
              if( inc % curr_num != 0 ):break;
              del_del = int(del_del / 10)
              cnt = cnt - 1
            elif (cnt == 0):
              curr_num = ((inc % 10))
              if (inc % curr_num == 0):
                print(inc)
              break;
            else:
              curr_num = ((inc // del_del) % 10)
              if (inc % curr_num != 0): break;
              del_del = int(del_del / 10)
              cnt = cnt - 1
          inc = inc + 1
        break;
      if case(): break  # default
  # end for
# end class Tasks_PP2()

##################################################################################################################
# Доп. задание                                                                                                   #
# В файле даны целые числа (100000 шт.)                                                                          #
# В диапазоне от -1000 до 1000                                                                                   #
# Построить гистограмму распределения количества чисел по интервалам.                                            #
# Диапазон интервалов от -1000 до 1000                                                                           #
# Количество интервалов либо задается пользователем либо рассчитывается по формуле Стерджеса.                    #
# Предусмотреть возможность экспорта данных для построения гистограммы в формат, который может прочитать Эксель. #
##################################################################################################################
class Aux_Histogram:
  def __init__(self):
    self.content = 0
    self.max     = 0
    self.min     = 0
    self.__selection__()
  # end def __init__(self):

  def __selection__(self):
    choose = int(input("1 - чтение из файла  \n"
                       "2 - рандомный массив \n"));
    if(   choose == 1 ):
      self.__read_file()
    elif( choose == 2 ):
      self.content = Task_2_RandomArray(mode=2, size=100000, bot=-1000, top=1000)
    else:
      print("Некорректный ввод");
    self.__calc_nums()
  # end def __selection__(self):

  def __read_file(self):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    # restrict to txt files only
    if( not file_path.endswith('.txt') ):
      exit("Только .txt файлы!")
    with open(file_path) as f:
      self.content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    self.content = [x.strip() for x in self.content]
  # end def __read_file(self):

  def __calc_nums(self):
    # Определение числа групп по формуле Стерджесса
    n = math.floor(1 + 3.322 * math.log(24, 10))
    self.__find_max_min()
    print(self.max, self.min)

  def __find_max_min(self):
    for index, value in self.content:
      print(f'|1111111 [', index, '] =', value)
      # http://univer-nn.ru/zadachi-po-statistike-primeri/gruppirovka-formula-sterdzhessa/
      # if( num > self.max ): self.max = num
      # if( num < self.min ): self.min = num
# end class Aux_Histogram:


# Головная фукнция программы
def main():
  TasksAll()
# end def Main():


# Вызов головной фукнции программы
main()
