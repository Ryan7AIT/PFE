# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:14:11 2022

@author: micro
"""
from ortools.sat.python import cp_model


def afficheResultat(x,data,model):
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.OPTIMAL:
        print(f'La Valeur optimal de f est : {solver.ObjectiveValue()}')
        
        obetpret = []
        total_poid = 0
        valeur1_total = 0
        valeur2_total = 0
        for i in data['all_items']:
            if solver.Value(x[i]) > 0:
                obetpret.append(1)
                print(
                    f"L'objet {i+1} de valeur1: {data['v1'][i]} valeur2: {data['v2'][i]}"
                )
                valeur1_total += int(data['v1'][i])
                valeur2_total += int(data['v2'][i])
                total_poid += int(data['vecContraint'][i])
            else:
                obetpret.append(0)

        print(f"Donc on a dans le sac une valeure 1 de : {valeur1_total}")
        print(f"Donc on a dans le sac une valeure 2 de : {valeur2_total}\n")
        print(f"Donc on a dans le sac un poid de : {total_poid}\n")

        
        return (solver.ObjectiveValue(), total_poid,valeur1_total,valeur2_total,obetpret)

        
    else:
        print('The problem does not have an optimal solution.')
        

        
        