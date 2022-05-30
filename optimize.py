# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:19:57 2022

@author: micro
"""
from ortools.sat.python import cp_model

def optimize(opt,data,x,model,objective):
      
    if opt == 'Maximize' :
        model.Maximize(cp_model.LinearExpr.Sum(objective))
    else:
        model.Minimize(cp_model.LinearExpr.Sum(objective))
        
    return objective 