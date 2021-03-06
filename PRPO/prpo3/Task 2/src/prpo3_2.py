# -*- coding: utf-8 -*-
"""PRPO3_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ZZv6kmFY8v01epWwswGWfFTeokTva_8
"""

import numpy  as np
import pandas as pd
import math

import matplotlib.pyplot as plt

# Read data from gdrive first
from google.colab import drive
drive.mount('/content/drive')

# Task 1
data = pd.read_csv( '/content/drive/My Drive/data/data.csv', delimiter=',' )

# Task 2
print( data.describe() )

# Task 3
print( data.head() )

print( data.tail() )

# Task 6
data.rename( columns = { 'DebtRatio' : 'Debt' }, inplace = True )

# Task 5
data.loc[data['MonthlyIncome'].notnull(), "Debt"] = data.loc[data['MonthlyIncome'].notnull(), "Debt"] * data.loc[data['MonthlyIncome'].notnull(), "MonthlyIncome"]
print(data[["Debt", "Id"]])

# Task 7
mean = data.loc[data['MonthlyIncome'].notnull(), "MonthlyIncome"].mean()
data.loc[data['MonthlyIncome'].isnull(), "MonthlyIncome"] = mean

# Task 8
print(data['SeriousDlqin2yrs'].groupby(data['NumberOfDependents']).mean())
print('--------------------------------')
print(data['SeriousDlqin2yrs'].groupby(data['NumberRealEstateLoansOrLines']).mean())

fig, ax = plt.subplots()

zeroDebts = data.loc[data["SeriousDlqin2yrs"] == 0]
zeroDebts = zeroDebts.loc[zeroDebts["MonthlyIncome"] != mean]

moreThanZeroDebts = data.loc[data["SeriousDlqin2yrs"] > 0]
moreThanZeroDebts = moreThanZeroDebts.loc[moreThanZeroDebts["MonthlyIncome"] != mean]

ax.scatter(zeroDebts['age'], zeroDebts["Debt"], c="blue")
ax.scatter(moreThanZeroDebts['age'], moreThanZeroDebts["Debt"], c="red")
plt.scatter(zeroDebts['age'], zeroDebts['Debt'])
plt.show()

fig, ax = plt.subplots()
plt.xlim([0, 25000])
plt.title('Зарплата')
zeroDebts['MonthlyIncome'].plot.kde(ax=ax, label="Без серьезных задолжностей", color="#76D6FF")
moreThanZeroDebts['MonthlyIncome'].plot.kde(ax=ax, label="С серьезными задолжностями", color="#FF7E79")
plt.show()

incomeNoMoreThan25K = data.loc[data["MonthlyIncome"] <= 25000]
incomeNoMoreThan25K = data.loc[data["MonthlyIncome"] != mean]


plt.title("Возраст и зарплата")

plt.xlim([16, 100])
plt.ylim([0, 25000])
plt.plot(incomeNoMoreThan25K['age'],incomeNoMoreThan25K['MonthlyIncome'], 'o')
plt.show()

plt.title("Возраст и число детей")

plt.xlim([16, 100])
plt.ylim([0, 20])
yint = range(int(incomeNoMoreThan25K['NumberOfDependents'].min()), int(incomeNoMoreThan25K['NumberOfDependents'].max())+20)
plt.yticks(yint)
plt.plot(incomeNoMoreThan25K['age'],incomeNoMoreThan25K['NumberOfDependents'], 'o')
plt.show()

plt.title("Взаимосвязь зарплат и числа детей")

plt.xlim([0, 25000])
plt.ylim([0, 20])
yint = range(int(incomeNoMoreThan25K['NumberOfDependents'].min()), int(incomeNoMoreThan25K['NumberOfDependents'].max())+20)
plt.yticks(yint)
plt.plot(incomeNoMoreThan25K['MonthlyIncome'],incomeNoMoreThan25K['NumberOfDependents'], 'o')
plt.show()