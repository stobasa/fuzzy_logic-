# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:56:56 2020

@author: PMIKE
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
#import matplotlib.pyplot as plt

def risk_guage(DD_input, DC_input, USM_input, ABP_input, NBP_input, APS_input, EII_input, EIP_input, LPS_input, IAS_input, UIC_input, FF_input, FO_input, ND_input):
    # New Antecedent/Consequent objects hold universe variables and membership
    # function

    DD = ctrl.Antecedent(np.arange(0, 2, 1), 'DD')
    DC = ctrl.Antecedent(np.arange(0, 2, 1), 'DC')
    USM = ctrl.Antecedent(np.arange(0, 2, 1), 'USM')
    ABP = ctrl.Antecedent(np.arange(0, 2, 1), 'ABP')
    NBP = ctrl.Antecedent(np.arange(0, 2, 1), 'NBP')
    APS = ctrl.Antecedent(np.arange(0, 2, 1), 'APS')
    EII = ctrl.Antecedent(np.arange(0, 2, 1), 'EII')
    EIP = ctrl.Antecedent(np.arange(0, 2, 1), 'EIP')
    LPS = ctrl.Antecedent(np.arange(0, 2, 1), 'LPS')
    IAS = ctrl.Antecedent(np.arange(0, 2, 1), 'IAS')
    UIC = ctrl.Antecedent(np.arange(0, 2, 1), 'UIC')
    FF = ctrl.Antecedent(np.arange(0, 2, 1), 'FF')
    FO = ctrl.Antecedent(np.arange(0, 2, 1), 'FO')
    ND = ctrl.Antecedent(np.arange(0, 2, 1), 'ND')
    risk_level = ctrl.Consequent(np.arange(0, 100, 1), 'risk_level')


    # Auto-membership function population is possible with .automf(3, 5, or 7)

    DD.automf(3)
    DC.automf(3)
    USM.automf(3)
    ABP.automf(3)
    NBP.automf(3)
    APS.automf(3)
    EII.automf(3)
    EIP.automf(3)
    LPS.automf(3)
    IAS.automf(3)
    UIC.automf(3)
    FF.automf(3)
    FO.automf(3)
    ND.automf(3)

    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    risk_level['low'] = fuzz.trimf(risk_level.universe, [0, 40, 75])
    risk_level['average'] = fuzz.trimf(risk_level.universe, [0, 75, 100])
    risk_level['good'] = fuzz.trimf(risk_level.universe, [75, 100, 100])
    risk_level['no_risk'] = fuzz.trimf(risk_level.universe, [0, 0, 0])


    # You can see how these look with .view()
    #structure['average'].view()
    #climate.view()
    #fuzzy set is (low, average and good)


    # if structure  is good and climate good then building will have low risk factor
    # if structure is  moderate /average then building risk factor is average
    # if stucture is low and climate is poor  then building risk factor is good
    rule1 = ctrl.Rule(DD['good'] | DC['good'] | USM['good'] | ABP['good'] | NBP['good'] | APS['good'] | EII['good'] | EIP['good'] | LPS['good'] | IAS['good'] | UIC['good'] | FF['good'] | FO['good'] | ND['good'], risk_level['good'])
    
    
    #ctrl.Rule(structure['poor'] | climate['poor'], risk_level['good'])

    rule2 = ctrl.Rule(DD['poor'] | DC['poor'] | USM['poor'] | ABP['poor'] | NBP['poor'] | APS['poor']
    | EII['poor'] | EIP['poor'] | LPS['poor'] | IAS['poor'] | UIC['poor'] | FF['poor'] | FO['poor'] | ND['poor'], risk_level['no_risk'])
    
    #ctrl.Rule(structure['average'], risk_level['average'])

    rule3 = ctrl.Rule(DD['poor'] | DC['poor'] | USM['poor'] | ABP['poor'] | NBP['poor'] | APS['poor']
    | EII['poor'] | EIP['poor'] | LPS['poor'] | IAS['poor'] | UIC['good'] | FF['poor'] | FO['good'] | ND['good'], risk_level['low'])


    rule4 = ctrl.Rule(DD['poor'] | DC['poor'] | USM['poor'] | ABP['good'] | NBP['poor'] | APS['poor']
    | EII['good'] | EIP['poor'] | LPS['good'] | IAS['poor'] | UIC['good'] | FF['poor'] & FO['good'] | ND['good'], risk_level['average'])

    #Creating a control system
    risk_factor_ctrl = ctrl.ControlSystem([rule1, rule2]) 
    # simulating the control system
    risk_factor_guage = ctrl.ControlSystemSimulation(risk_factor_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

    dict_data = {'DD':DD_input, 'DC':DC_input, 'USM':USM_input, 'ABP':ABP_input, 'NBP':NBP_input, 'APS':APS_input, 'EII':EII_input, 'EIP':EIP_input, 'LPS':LPS_input, 'IAS':IAS_input, 'UIC':UIC_input, 'FF':FF_input, 'FO':FO_input, 'ND':ND_input}
    risk_factor_guage.inputs(dict_data)
    # Crunch the numbers
    risk_factor_guage.compute()


    print(risk_factor_guage.output['risk_level'])
    #risk_level.view(sim=risk_factor_guage)
    return risk_factor_guage.output['risk_level']

risk_guage(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
risk_guage(1,1,1,1,1,1,1,1,1,1,1,1,1,1)
risk_guage(0,0,0,0,0,0,0,0,0,0,0,0,1,1)
risk_guage(0,0,0,1,0,0,1,0,1,0,1,0,1,1)