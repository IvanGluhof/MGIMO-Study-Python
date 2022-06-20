#!/usr/bin/env python
# For Linux test

# Определение степени износа предмета

# imports
from skfuzzy \
import control           as ctrl;
import numpy             as nump;
import skfuzzy           as fuzz;
import matplotlib.pyplot as plot;

# Лингвистические переменные
serv = ctrl.Antecedent(nump.arange(0, 50, 1), 'serv'); # Срок эксплуатации (до 50 лет)
cond = ctrl.Antecedent(nump.arange(0, 10, 1), 'cond'); # Качество предмета на вид
wear = ctrl.Consequent(nump.arange(0, 30, 1), 'wear'); # Степень износа изделия

# Кол-во состояний (3 default OK)
STATES=3
serv.automf(STATES);
cond.automf(STATES);

# Принадлежность
# 1) Срок эксплуатации
sigma = 2 # сигма для функции Гаусса
serv["LOW_SERVICE"] = fuzz.gaussmf(serv.universe, 0,  sigma); # малый срок
serv["MED_SERVICE"] = fuzz.gaussmf(serv.universe, 10, sigma); # средний срок
serv["EXT_SERVICE"] = fuzz.gaussmf(serv.universe, 20, sigma); # длительный срок
serv["OLD_SERVICE"] = fuzz.gaussmf(serv.universe, 30, sigma); # очень длительный срок
# 2) Качество предмта на вид
sigma = 4 # сигма для функции Гаусса
cond["NEW_COND"] = fuzz.gaussmf(cond.universe, 0, sigma); # новый
cond["USE_COND"] = fuzz.gaussmf(cond.universe, 5, sigma); # бывший в эксплуатации
cond["OLD_COND"] = fuzz.gaussmf(cond.universe, 10, sigma);# старый
# 3) Степень износа изделия
sigma = 6 # сигма для функции Гаусса
wear['LOW_WEAR'] = fuzz.gaussmf(wear.universe, 0,  sigma) # малый износ
wear['MED_WEAR'] = fuzz.gaussmf(wear.universe, 15, sigma) # средний износ
wear['OLD_WEAR'] = fuzz.gaussmf(wear.universe, 30, sigma) # большой износ
# Условные правила (нечеткие)
# LOW_WEAR
rule_low_1 = ctrl.Rule( serv["LOW_SERVICE"] & cond["NEW_COND"], wear['LOW_WEAR'] );
rule_low_2 = ctrl.Rule( serv["MED_SERVICE"] | cond["NEW_COND"], wear['LOW_WEAR'] );
# MED_WEAR
rule_med_1 = ctrl.Rule( serv["MED_SERVICE"] | cond["USE_COND"], wear['MED_WEAR'] );
rule_med_2 = ctrl.Rule( serv["EXT_SERVICE"] | cond["USE_COND"], wear['MED_WEAR'] );
rule_med_3 = ctrl.Rule( serv["EXT_SERVICE"] | cond["NEW_COND"], wear['MED_WEAR'] );
rule_med_4 = ctrl.Rule( serv["MED_SERVICE"] | cond["OLD_COND"], wear['MED_WEAR'] );
# OLD WEAR
rule_old_1 = ctrl.Rule( serv["EXT_SERVICE"] | cond["USE_COND"], wear['OLD_WEAR'] );
rule_old_2 = ctrl.Rule( serv["OLD_SERVICE"] | cond["USE_COND"], wear['MED_WEAR'] );
rule_old_3 = ctrl.Rule( serv["EXT_SERVICE"] | cond["OLD_COND"], wear['OLD_WEAR'] );
rule_old_4 = ctrl.Rule( serv["OLD_SERVICE"] | cond["OLD_COND"], wear['MED_WEAR'] );

# Загрузка правил
ctrl_sys = ctrl.ControlSystem(
  [
    rule_low_1,
    rule_low_2,
    rule_med_1,
    rule_med_2,
    rule_med_3,
    rule_med_4,
    rule_old_1,
    rule_old_2,
    rule_old_3,
    rule_old_4,
  ]
)

# Экземпляр объекта
ctrl_instance = ctrl.ControlSystemSimulation(ctrl_sys)

# Входные параметры
ctrl_instance.input['serv'] = 30
ctrl_instance.input['cond'] = 10

# Вычисление
ctrl_instance.compute()

# View plots
serv.view(sim=ctrl_instance)
cond.view(sim=ctrl_instance)
wear.view(sim=ctrl_instance)

plot.show()

print("Степень износа предмета: ", ctrl_instance.output['wear'], "%")
