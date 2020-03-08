# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 00:56:56 2020

@author: stObasa
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

def risk_guage(DD_input, DC_input, USM_input, ABP_input, NBP_input, APS_input, EII_input, EIP_input, LPS_input, IAS_input, UIC_input, FF_input, FO_input, ND_input):
    # New Antecedent/Consequent objects hold universe variables and membership
    # function
    '''DD = ctrl.Antecedent(np.arange(0, 2, 1), 'Defective design')
    DC = ctrl.Antecedent(np.arange(0, 2, 1), 'Defective construction')
    USM = ctrl.Antecedent(np.arange(0, 2, 1), 'Use of substandard materials ')
    ABP = ctrl.Antecedent(np.arange(0, 2, 1), 'Absence of building permit')
    NBP = ctrl.Antecedent(np.arange(0, 2, 1), 'Non-Adherence to building plans')
    APS = ctrl.Antecedent(np.arange(0, 2, 1), 'Absence of proper site or soil investigation')
    EII = ctrl.Antecedent(np.arange(0, 2, 1), 'Engagement of ill-equipped, incompetent contractors')
    EIP = ctrl.Antecedent(np.arange(0, 2, 1), 'Engagement of inexperienced personnel to take charge of construction of works')
    LPS = ctrl.Antecedent(np.arange(0, 2, 1), 'Lack of proper supervision, inspection and monitoring of  construction works')
    IAS = ctrl.Antecedent(np.arange(0, 2, 1), 'Illegal conversion, alteration and addition to existing structures')
    UIC = ctrl.Antecedent(np.arange(0, 2, 1), 'Undue interference of client on building works')
    FF = ctrl.Antecedent(np.arange(0, 2, 1), 'Foundation failures')
    FO = ctrl.Antecedent(np.arange(0, 2, 1), 'Foundation failures')
    ND = ctrl.Antecedent(np.arange(0, 2, 1), 'Natural disasters')
    risk_level = ctrl.Antecedent(np.arange(0, 26, 1), 'Natural disasters' '''
    
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
    risk_level = ctrl.Antecedent(np.arange(0, 26, 1), 'risk_level')



    # Auto-membership function population
    name = ['yes', 'no']
    DD.automf(names=name)
    DC.automf(names=name)
    USM.automf(names=name)
    ABP.automf(names=name)
    NBP.automf(names=name)
    APS.automf(names=name)
    EII.automf(names=name)
    EIP.automf(names=name)
    LPS.automf(names=name)
    IAS.automf(names=name)
    UIC.automf(names=name)
    FF.automf(names=name)
    FO.automf(names=name)
    ND.automf(names=name)

    # Custom membership functions can be built interactively with a familiar,
    # Pythonic API
    risk_level['no_risk'] = fuzz.trimf(risk_level.universe, [0, 0, 0])
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
    rule1 = ctrl.Rule(DD['yes'] & DC['yes'] & USM['yes'] & ABP['yes'] & NBP['yes'] & APS['yes']
    & EII['yes'] & EIP['yes'] & LPS['yes'] & IAS['yes'] & UIC['yes'] & FF['yes'] & FO['yes'] & ND['yes'], risk_level['high'])

    rule2 = ctrl.Rule(DD['no'] & DC['no'] & USM['no'] & ABP['no'] & NBP['no'] & APS['no']
    & EII['no'] & EIP['no'] & LPS['no'] & IAS['no'] & UIC['no'] & FF['no'] & FO['no'] & ND['no'], risk_level['no_risk'])
    
    rule3 = ctrl.Rule(DD['no'] & DC['no'] & USM['no'] & ABP['no'] & NBP['no'] & APS['no']
    & EII['no'] & EIP['no'] & LPS['no'] & IAS['no'] & UIC['yes'] & FF['no'] & FO['yes'] & ND['yes'], risk_level['low'])
    
    rule4 = ctrl.Rule(DD['no'] & DC['no'] & USM['no'] & ABP['yes'] & NBP['no'] & APS['no']
    & EII['yes'] & EIP['no'] & LPS['yes'] & IAS['no'] & UIC['yes'] & FF['no'] & FO['yes'] & ND['yes'], risk_level['average'])
    

    #Creating a control system
    risk_factor_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
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


risk_guage(False,False,False,False,False,False,False,False,False,False,False,False,False,False)

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
structure['average'].view()
climate.view()
#fuzzy set is (low, average and high)