#!/usr/bin/env python
# For Linux test

# Determine object wear state

# imports
from skfuzzy \
import control           as ctrl;
import numpy             as nump;
import skfuzzy           as fuzz;
import matplotlib.pyplot as plot;

# Linguistic params
serv = ctrl.Antecedent(nump.arange(0, 50, 1), 'serv'); # Object served time
cond = ctrl.Antecedent(nump.arange(0, 10, 1), 'cond'); # Object condition
wear = ctrl.Consequent(nump.arange(0, 30, 1), 'wear'); # Object wear at glance

# State 
STATES=3
serv.automf(STATES)
cond.automf(STATES)

# 1) Object served time
sigma = 2 # Sigma for Gauss function
serv["LOW_SERVICE"] = fuzz.gaussmf(serv.universe, 0,  sigma)
serv["MED_SERVICE"] = fuzz.gaussmf(serv.universe, 10, sigma)
serv["EXT_SERVICE"] = fuzz.gaussmf(serv.universe, 20, sigma)
serv["OLD_SERVICE"] = fuzz.gaussmf(serv.universe, 30, sigma)
# 2) Object condition
sigma = 4 # Sigma for Gauss function
cond["NEW_COND"] = fuzz.gaussmf(cond.universe, 0, sigma)
cond["USE_COND"] = fuzz.gaussmf(cond.universe, 5, sigma)
cond["OLD_COND"] = fuzz.gaussmf(cond.universe, 10, sigma)
# 3) Object wear at glance
sigma = 6 # Sigma for Gauss function
wear['LOW_WEAR'] = fuzz.gaussmf(wear.universe, 0,  sigma)
wear['MED_WEAR'] = fuzz.gaussmf(wear.universe, 15, sigma) 
wear['OLD_WEAR'] = fuzz.gaussmf(wear.universe, 30, sigma) 

# Fuzzy rules
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

# Rules load
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

# Instance of the object
ctrl_instance = ctrl.ControlSystemSimulation(ctrl_sys)

# Input params
ctrl_instance.input['serv'] = 30
ctrl_instance.input['cond'] = 10

# Calculate
ctrl_instance.compute()

# View plots
serv.view(sim=ctrl_instance)
cond.view(sim=ctrl_instance)
wear.view(sim=ctrl_instance)

plot.show()

print("Wear is: ", ctrl_instance.output['wear'], "%")
