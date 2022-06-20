# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge


class data_processing:
  """docstring"""
  path_to_file = ""
  dataset      = ""
  data         = ""

  def __init__(self, path):
    """Constructor"""
    self.read_data(path, 0)
    self.standardize()
    self.init_ridge()
  # end def __init__(self):

  def read_data(self, path, header_read):
    cols = ['x', 'y']
    self.path_to_file = path
    self.dataset      = pd.read_csv(path, skiprows=[0], header = header_read, names = cols)
    self.data         = self.dataset.values
    
    if self.dataset.empty:
      print("Error - input data is empty")
      exit(1)
    else:
      if 0:
        # Гистограмма распределения (x_axis)
        self.dataset.plot(y='x',
                          kind='hist',
                          color='red',
                          title='x_axis distribution')
        # Гистограмма распределения (y_axis)
        self.dataset.plot(y='y',
                          kind='hist',
                          color='green',
                          title='y_axis distribution')
        self.dataset.plot(x = 'x', y  = 'y', kind = 'scatter')
        plt.plot(self.dataset['x'], self.dataset['y'], '.')
        plt.show()
      
      return
  # end def read_data(self, path):
  
  def standardize(self):
    for i in range(2, 16):  # power of 1 is already there
      column = 'x_%d' % i  # new var will be x_power
      self.dataset[column] = self.dataset['x'] ** i
    return
  # end def standardize(self):
  
  def init_ridge(self):
    # Initialize predictors to be set of 15 powers of x
    predictors = ['x']
    predictors.extend(['x_%d' % i for i in range(2, 16)])

    # Set the different values of alpha to be tested
    alpha_ridge = [1e-15, 1e-10, 1e-8, 1e-4, 1e-3, 1e-2, 1, 5, 10, 20]

    # Initialize the dataframe for storing coefficients.
    col = ['rss', 'intercept'] + ['coef_x_%d' % i for i in range(1, 16)]
    ind = ['alpha_%.2g' % alpha_ridge[i] for i in range(0, 10)]
    coef_matrix_ridge = pd.DataFrame(index=ind, columns=col)
  
    models_to_plot = {1e-15: 231, 1e-10: 232, 1e-4: 233, 1e-3: 234, 1e-2: 235, 5: 236}
    for i in range(10):
      coef_matrix_ridge.iloc[i, ] = self.ridge_regression(self.dataset, predictors, alpha_ridge[i], models_to_plot)

    # Set the display format to be scientific for ease of analysis
    pd.options.display.float_format = '{:,.2g}'.format
    print(coef_matrix_ridge)

    coef_matrix_ridge.apply(lambda x: sum(x.values == 0), axis=1)
    print(coef_matrix_ridge)
    
    plt.show()
    
    return
  # def init_ridge(self):
  
  def print_data(self):
    print(self.dataset)
  # end def print_data(self):

  @staticmethod
  def ridge_regression(data, predictors, alpha, models_to_plot = None):
    # Fit the model
    if models_to_plot is None:
      models_to_plot = {}
    ridge_reg = Ridge(alpha=alpha, normalize=True)
    ridge_reg.fit(data[predictors], data['y'])
    y_pred = ridge_reg.predict(data[predictors])

    # Check if a plot is to be made for the entered alpha
    if alpha in models_to_plot:
      plt.subplot(models_to_plot[alpha])
      plt.tight_layout()
      plt.plot(data['x'], y_pred)
      plt.plot(data['x'], data['y'], '.')
      plt.title('Plot for alpha: %.3g' % alpha)
      
    # Return the result in pre-defined format
    rss = sum((y_pred - data['y']) ** 2)
    ret = [rss]
    ret.extend([ridge_reg.intercept_])
    ret.extend(ridge_reg.coef_)
    return ret
  # end def ridge_regression(data, predictors, alpha, models_to_plot={}):

# end class data_processing():
