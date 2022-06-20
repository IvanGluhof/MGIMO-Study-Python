import tkinter as tk
from tkinter import filedialog
from data_processing import data_processing


class init:
  """docstring"""
  path_to_file = ""
  data = ""

  def __init__(self):
    """Constructor"""
    self.path_to_file = self.open_data_file()
    if self.path_to_file == "":
      print("Error - no file is selected")
    else:
      data_processing(self.path_to_file)
  # end ef __init__(self):
  
  @staticmethod
  def open_data_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()
  # end def open_data_file(self):
  
# end class init(object):
