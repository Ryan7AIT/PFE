# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:02:38 2022

@author: micro
"""
from ortools.sat.python import cp_model
def addConstraints(data):
    model = cp_model.CpModel()

    x = {}
    
    for i in data['all_items']:
        x[i] = model.NewBoolVar(f'x_{i}')
        
        
    model.Add(
        sum(x[i] * int(data['vecContraint'][i])
            for i in data['all_items']) <= data['poid'] )
    
    return (x,model)