# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 14:48:27 2017

@author: ps
"""
import time

TC = input()
N = [0]*TC
for i in range(TC):
    N[i] = input()

for i in range(TC):
    is_prime =True
    if(N[i] ==1):
        is_prime =False
        print N[i]-1,1
    else:        
        for j in range(2,int(math.ceil(math.sqrt(N[i])))+1):
            if(N[i]%j == 0):
                is_prime =False
                print N[i]-j,j
                break
            
    if(is_prime):
        print 0,N[i]        
        

        