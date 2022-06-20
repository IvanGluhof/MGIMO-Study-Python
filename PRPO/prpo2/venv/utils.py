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