# -*- coding: utf-8 -*-
"""
Created on Wed May 25 14:52:17 2022

@author: micro
"""

def initdata(vecContraint ,v1,v2,poid):
        
    data = {}
    
    data['v1'] = v1
    data['v2'] = v2
    data['vecContraint'] = vecContraint
    data['poid'] = poid
    
    assert len(data['v1']) == len(data['v2'])
    
    data['num_items'] = len(data['v1'])
    data['all_items'] = range(data['num_items'])
    
    return data