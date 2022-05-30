# -*- coding: utf-8 -*-
"""
Created on Wed May 18 18:46:19 2022

@author: ryan
"""

from plamda import resoudrePλ
import random
import time


def aggregation(vecContraint, v1, v2, lmda, p, poid):
    start = time.time()

    counter = 0 
    alloptimal = []

    while lmda < 1:
        counter += 1
        
        (optimalvalue,pmax,v1all,v2all,xi) = resoudrePλ(vecContraint,v1, v2,lmda,poid)
        
        alloptimal.append(optimalvalue)
        
        lmda += p
        
    end = time.time()

    print('time: ', end-start)

        
    print(counter,'iteration  pour resoudre ce problem.')  
    
    return (optimalvalue,pmax,v1all,v2all,xi,alloptimal)
    
    

# (* To test this function with random data and a chosen number of item*)

# =============================================================================
# v1 = []
# v2 = []
# vecContraint  = []
# 
#     
# n = 300000 
# 
# 
# for i in range(n):
#     v1.append(random.randint(10,70))
#     v2.append(random.randint(10,70))
#     vecContraint.append(random.randint(10,70))
#     
# 
#     
# 
# aggregation(vecContraint,v1, v2, 0.0001, 0.3,70)
#     
# =============================================================================
