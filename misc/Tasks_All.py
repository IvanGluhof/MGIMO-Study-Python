import random  
import math  
import tkinter as tk  
from tkinter import filedialog 


class switch(object):
  def __init__(self, value):
    self.value = value  
    self.empty = False  
  # end def __init__(self, value):

  def __iter__(self):
    yield self.case      
    raise StopIteration 
  # end def __iter__(self):

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

class TasksAll:
  def __init__(self):
    self.__print_header()
    self.CallTask = int(input("Input task number"))
    self.__choose_task()
  # end def __init__(self):

  def __print_header(self):
    print(
      "------------------------------------------------------------------------------------------------------\n"
      "1 - Task 1\n"
      "2 - Task 2\n"
      "3 - Task 3\n"
      "4 - Task 4\n"
      "5 - Task 5\n"
      "6 - Task 6\n"
      "9 - Task 7\n"
      "------------------------------------------------------------------------------------------------------\n")
  # def __print_header(self):

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
# Task 1                                                      #
# #############################################################
class Task_1:
  def __init__(self):
    self.__analyze(int(input("Input [1-9]: "))) 
  # end def __init__(self):

  def __analyze(self, x):

    bool_x1x3 = (x >= 1) and (x <= 3) 
    bool_x4x6 = (x >= 4) and (x <= 6) 
    bool_x7x9 = (x >= 7) and (x <= 9) 

    self.__x1x3() if bool_x1x3 else (self.__x4x6(x)
                  if bool_x4x6 else (self.__x7x9(x)
                  if bool_x7x9 else print("Error input")))
  # end def __analyze(self, x):

  def __x1x3(self):
    i = 0                                             
    s = str(input("Input string: "))                 
    n = int(input("Input number: ")) 

    while i < n:
      i = i + 1 
      print("Result: ", s) 
  # end def __x1x3(self):

  def __x4x6(self, x):
    m = int(input("Input number: ")) 
    print("Result: ", x ** m)  
  # end def __x4x6(self, x):

  def __x7x9(self, x):
    i = 0
    while i < 10:
      i = i + 1
      x = x + 1
      print("Result: ", x)
  # end def __x7x9(self, x):
# end class Task_1:


###############################################################
# Task 2                                                      #
# #############################################################
class Task_2_RandomArray:
  # Init with mode - auto or input
  def __init__(self, mode, size, top, bot):
    self.rnd_arr = []   
    self.size    = size 
    self.top     = top  
    self.bot     = bot  
    self.__create(mode)
  # end def __init__(self):

  def __create(self, mode):
    if( mode == 1 ):
      self.size = int(input("Input array range (2, 100): "))
      if ((self.size > 1) and (self.size <= 100)):
        self.bot = int(input("Input array bot range "))
        self.top = int(input("Input array top range: "))
        if (self.bot < self.top):
          self.__generate(self.size, self.top, self.bot)
        else:
          exit("Error: bot > top)
      else:
        exit("Error array value")
    else:
      if( (self.size > 1) and (self.size <= 1000000) ):
        if (self.bot < self.top):
          self.__generate(self.size, self.top, self.bot)
        else:
          exit("Error: bot > top")
      else:
        exit("Error array value")
  # end def __create(self):

  def __generate(self, size, top, bot):
    i = 0
    while i < size:
      self.rnd_arr.append(random.randint(bot, top))
      i += 1
    print("| Random array:  |")
    self.print()
  # end def __generate(self, size, top, bot):

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
    print(f'Min:  [', min_idx, '] =', min_num)
    print(f'Max: [', max_idx, '] =', max_num)
    print('Swap')
    print('\n')

    self.rnd_arr[max_idx] = min_num
    self.rnd_arr[min_idx] = max_num

    print("| Swapped min/max array:  |")
    self.print()
  # end def swap_min_max(self):

  def print(self):
    print("|--------------------|")
    for index, value in enumerate(self.rnd_arr):
      print(f'| [', index, '] =', value)
    print("|--------------------|")
  # end def print(self):
# end class RandomArray:


###############################################################
# Task 3                                                      #
# #############################################################
class Task_3():
  def __init__(self):
    v_rnd_1 = random.randint(-100, 100)
    v_rnd_2 = random.randint(-100, 100)
    v_rnd_3 = random.randint(-100, 100)

    b_max_1 = (v_rnd_2 < v_rnd_1 < v_rnd_3) or (v_rnd_3 < v_rnd_1 < v_rnd_2)
    b_max_2 = (v_rnd_1 < v_rnd_2 < v_rnd_3) or (v_rnd_3 < v_rnd_2 < v_rnd_1)
    b_max_3 = (v_rnd_1 < v_rnd_3 < v_rnd_2) or (v_rnd_2 < v_rnd_3 < v_rnd_1)

    v_max_second = v_rnd_1 if b_max_1 else v_rnd_2 \
                           if b_max_2 else v_rnd_3 \
                           if b_max_3 else 0
                           
    print("3 randoms: ", v_rnd_1, v_rnd_2, v_rnd_3,
          "\nSecond max is: ", v_max_second)
# end class Task_3():


###############################################################
# Task 3.1                                                    #
# #############################################################
class Tasks_PP3():
  def __init__(self):
    for case in switch(int(input("1  - Task A\n"
                                 "2  - Task B\n"
                                 "3  - Task C\n"
                                 "4  - Task A2\n"
                                 "5  - Task B2\n"
                                 "6  - Task C2\n"
                                 "7  - Task A3\n"
                                 "8  - Task B3\n"
                                 "9  - Task-2 A\n"
                                 "10 - Task-2 B\n"
                                 "11 - Task-2 C\n"
                                 "12 - Task A4\n"
                                 "13 - Task B4\n"
                                 "14 - Task C4\n"
                                 "15 - Task A5\n"
                                 "16 - Task B5\n"
                                 "17 - Task C5\n"
                                 ))):
      if case(1):
        a, b, c = map(int, input("Input 3 nums: ").split());
        print("Max ", (a if a > b else b if b > c else c));
        break;
      if case(2):
        arr = []
        a0, a1, a2, a3, a4 = map(int, input("Input 5 nums ").split());
        arr.append(a0)
        arr.append(a1)
        arr.append(a2)
        arr.append(a3)
        arr.append(a4)
        max = a0
        for a in arr:
          if a > max: max = a
        print("Max ", max)
        break;
      if case(4):
        a, b, c = map(int, input("Input 3 nums: ").split());
        if( a == b == c):
          print("All equal")
        elif( a == b or a == c or b == c):
          print("Two nums equal")
        else:
          print("None equal")
        break;
      if case(7):
        a, b = map(int, input("Input two number ").split());
        if( a < 0 or b < 0 or a > b):
          print("Error input")
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
        a, b = map(int, input("Input two numbers: ").split());
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

      if case(9):
        a = int(input("Input number:\n "))
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
        print("Summ " ", result)
        break;
      if case(10):
        a = int(input("Input number:\n "))
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
          print("Yes")
        else:
          print("No")
        break;
      if case(11):
        a = int(input("Input number:\n "))
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
          print("Yes")
        else:
          print("No")
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
        a = int(input("Input number:\n "))
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
          print("Number", a, "is Armstrong")
        else:
          print("Number", a, "is not Armstrong")
        break;
      if case(14):
        n = int(input("Input N:\n "))
        cnt = 1
        sqrt = 0
        while(sqrt < (n+1)):
          sqrt = cnt * cnt

          if(sqrt % 1000000 == cnt or
             sqrt % 100000  == cnt or
             sqrt % 10000   == cnt or
             sqrt % 1000    == cnt or
             sqrt % 100     == cnt or
             sqrt % 10      == cnt): print(sqrt, cnt)
          cnt = cnt + 1
      if case(15):

        a, b = map(int, input("Input range: ").split());
        if( a > b ):
          print("Error input")
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

      if case(17):
        n = int(input("Input N:\n "))
        inc = 1
        while(inc < (n+1)):
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

class Aux_Histogram:
  def __init__(self):
    self.content = 0
    self.max     = 0
    self.min     = 0
    self.__selection__()
  # end def __init__(self):

  def __selection__(self):
    choose = int(input("1 - read file \n"
                       "2 - random array \n"));
    if(   choose == 1 ):
      self.__read_file()
    elif( choose == 2 ):
      self.content = Task_2_RandomArray(mode=2, size=100000, bot=-1000, top=1000)
    else:
      print("Error input");
    self.__calc_nums()
  # end def __selection__(self):

  def __read_file(self):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    # restrict to txt files only
    if( not file_path.endswith('.txt') ):
      exit("Only .txt!")
    with open(file_path) as f:
      self.content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    self.content = [x.strip() for x in self.content]
  # end def __read_file(self):

  def __calc_nums(self):

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

def main():
  TasksAll()
# end def Main():

main()
