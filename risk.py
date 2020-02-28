# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:56:56 2020

@author: PMIKE
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#import matplotlib.pyplot as plt

def risk_guage(climate_input, structure_input):
    # New Antecedent/Consequent objects hold universe variables and membership
    # function
    structure = ctrl.Antecedent(np.arange(0, 11, 1), 'structure')
    climate = ctrl.Antecedent(np.arange(0, 11, 1), 'climate')
    risk_level = ctrl.Consequent(np.arange(0, 26, 1), 'risk_level')
    # Auto-membership function population is possible with .automf(3, 5, or 7)
    structure .automf(3)
    climate.automf(3)

    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    risk_level['low'] = fuzz.trimf(risk_level.universe, [0, 0, 13])
    risk_level['average'] = fuzz.trimf(risk_level.universe, [0, 13, 25])
    risk_level['high'] = fuzz.trimf(risk_level.universe, [13, 25, 25])
    # You can see how these look with .view()
    #structure['average'].view()
    #climate.view()
    #fuzzy set is (low, average and high)


    # if structure  is good and climate good then building will have low risk factor
    # if structure is  moderate /average then building risk factor is average
    # if stucture is low and climate is poor  then building risk factor is high
    rule1 = ctrl.Rule(structure['poor'] | climate['poor'], risk_level['high'])
    rule2 = ctrl.Rule(structure['average'], risk_level['average'])
    rule3 = ctrl.Rule(structure['good'] | climate['good'], risk_level['low'])


    #Creating a control system
    risk_factor_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
    # simulating the control system
    risk_factor_guage = ctrl.ControlSystemSimulation(risk_factor_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

    dict_data = {'structure': structure_input, 'climate':climate_input}
    risk_factor_guage.inputs(dict_data)
    # Crunch the numbers
    risk_factor_guage.compute()


    risk_G = risk_factor_guage.output['risk_level']
    #risk_level.view(sim=risk_factor_guage)
    return risk_G


risk_guage(5,6)