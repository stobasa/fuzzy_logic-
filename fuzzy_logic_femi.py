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
    '''DD = ctrl.Antecedent(np.arange(0, 1, 1), 'Defective design')
    DC = ctrl.Antecedent(np.arange(0, 1, 1), 'Defective construction')
    USM = ctrl.Antecedent(np.arange(0, 1, 1), 'Use of substandard materials ')
    ABP = ctrl.Antecedent(np.arange(0, 1, 1), 'Absence of building permit')
    NBP = ctrl.Antecedent(np.arange(0, 1, 1), 'Non-Adherence to building plans')
    APS = ctrl.Antecedent(np.arange(0, 1, 1), 'Absence of proper site or soil investigation')
    EII = ctrl.Antecedent(np.arange(0, 1, 1), 'Engagement of ill-equipped, incompetent contractors')
    EIP = ctrl.Antecedent(np.arange(0, 1, 1), 'Engagement of inexperienced personnel to take charge of construction of works')
    LPS = ctrl.Antecedent(np.arange(0, 1, 1), 'Lack of proper supervision, inspection and monitoring of  construction works')
    IAS = ctrl.Antecedent(np.arange(0, 1, 1), 'Illegal conversion, alteration and addition to existing structures')
    UIC = ctrl.Antecedent(np.arange(0, 1, 1), 'Undue interference of client on building works')
    FF = ctrl.Antecedent(np.arange(0, 1, 1), 'Foundation failures')
    FO = ctrl.Antecedent(np.arange(0, 1, 1), 'Foundation failures')
    ND = ctrl.Antecedent(np.arange(0, 1, 1), 'Natural disasters')
    risk_level = ctrl.Antecedent(np.arange(0, 26, 1), 'Natural disasters' '''
    
    DD = ctrl.Antecedent(np.arange(0, 11, 1), 'DD')
    DC = ctrl.Antecedent(np.arange(0, 11, 1), 'DC')
    USM = ctrl.Antecedent(np.arange(0, 11, 1), 'USM')
    ABP = ctrl.Antecedent(np.arange(0, 11, 1), 'ABP')
    NBP = ctrl.Antecedent(np.arange(0, 11, 1), 'NBP')
    APS = ctrl.Antecedent(np.arange(0, 11, 1), 'APS')
    EII = ctrl.Antecedent(np.arange(0, 11, 1), 'EII')
    EIP = ctrl.Antecedent(np.arange(0, 11, 1), 'EIP')
    LPS = ctrl.Antecedent(np.arange(0, 11, 1), 'LPS')
    IAS = ctrl.Antecedent(np.arange(0, 11, 1), 'IAS')
    UIC = ctrl.Antecedent(np.arange(0, 11, 1), 'UIC')
    FF = ctrl.Antecedent(np.arange(0, 11, 1), 'FF')
    FO = ctrl.Antecedent(np.arange(0, 11, 1), 'FO')
    ND = ctrl.Antecedent(np.arange(0, 11, 1), 'ND')
    risk_level = ctrl.Antecedent(np.arange(0, 26, 1), 'risk_level')



    # Auto-membership function population
    name = ['lower', 'average','high']


    DD.automf(3,names = name)
    DC.automf(3,names =name)
    USM.automf(3,names =name)
    ABP.automf(3,names =name)
    NBP.automf(3,names =name)
    APS.automf(3,names =name)
    EII.automf(3,names =name)
    EIP.automf(3,names =name)
    LPS.automf(3,names =name)
    IAS.automf(3,names =name)
    UIC.automf(3,names =name)
    FF.automf(3,names =name)
    FO.automf(3,names =name)
    ND.automf(3,names =name)

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
    rule1 = ctrl.Rule(DD['high'] | DC['high'] | USM['high'] | ABP['high'] | NBP['high'] | APS['high']
    | EII['high'] | EIP['high'] | LPS['high'] | IAS['high'] | UIC['high'] | FF['high'] | FO['high'] | ND['high'], risk_level['high'])

    rule2 = ctrl.Rule(DD['lower'] | DC['lower'] | USM['lower'] | ABP['lower'] | NBP['lower'] | APS['lower']
    | EII['lower'] | EIP['lower'] | LPS['lower'] | IAS['lower'] | UIC['lower'] | FF['lower'] | FO['lower'] | ND['lower'], risk_level['no_risk'])
    
    rule3 = ctrl.Rule(DD['lower'] | DC['lower'] | USM['lower'] | ABP['lower'] | NBP['lower'] | APS['lower']
    | EII['lower'] | EIP['lower'] | LPS['lower'] | IAS['lower'] | UIC['high'] | FF['lower'] | FO['high'] | ND['high'], risk_level['low'])
    
    rule4 = ctrl.Rule(DD['lower'] | DC['lower'] | USM['lower'] | ABP['high'] | NBP['lower'] | APS['lower']
    | EII['high'] | EIP['lower'] | LPS['high'] | IAS['lower'] | UIC['high'] | FF['lower'] | FO['high'] | ND['high'], risk_level['average'])
    

    #Creating a control system
    risk_factor_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
    # simulating the control system
    risk_factor_guage = ctrl.ControlSystemSimulation(risk_factor_ctrl)

    # Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
    # Note: if you like passing many inputs all at once, use .inputs(dict_of_data)

    dict_data = {'DD':DD_input, 'DC':DC_input, 'USM':USM_input, 'ABP':ABP_input, 'NBP':NBP_input, 'APS':APS_input, 'EII':EII_input, 'EIP':EIP_input, 'LPS':LPS_input, 'IAS':IAS_input, 'UIC':UIC_input, 'FF':FF_input, 'FO':FO_input, 'ND':ND_input}
    print(dict_data)
    risk_factor_guage.inputs(dict_data)
    # Crunch the numbers
    risk_factor_guage.compute()


    print(risk_factor_guage.output['risk_level'])
    #risk_level.view(sim=risk_factor_guage)
    return risk_factor_guage.output['risk_level']


#risk_guage(1,1,1,1,1,1,1,1,1,1,1,1,1,1)

'''
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
'''