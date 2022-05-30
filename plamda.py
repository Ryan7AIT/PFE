# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:46:19 2022

@author: micro
"""

from initdata import initdata

from ortools.sat.python import cp_model

from addConstraints import addConstraints

from optimize import optimize

from afficheResultat import afficheResultat



def resoudrePλ(vecContraint,v1,v2,lmda,poid):
    #v1 esr le vect de valeur a maximiser
    #v2 est un vecteur au choid a minimiser (poid par exemple)
    
    data = initdata(vecContraint,v1, v2, poid)
    x,model = addConstraints(data)

    objectivev1 = []
    for i in data['all_items']:
        objectivev1.append(
            cp_model.LinearExpr.Term(x[i], lmda * int(data['v1'][i])))
             
    objectivev2 = []   
    for i in data['all_items']:
        objectivev2.append(
            cp_model.LinearExpr.Term(x[i], (lmda - 1  ) * int(data['v2'][i])))
    
    objective = objectivev1 + objectivev2
        
    optimize('Maximize', data, x, model,objective)

    (optimalvalue,pmax,v1all,v2all,xi) = afficheResultat(x, data, model)

    return (optimalvalue,pmax,v1all,v2all,xi)


