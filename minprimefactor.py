# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 14:48:27 2017

@author: ps
"""
isprime =1
TC = input()
N = [0]*TC
for i in range(TC):
    N[i] = input()

for i in range(TC):
    if(N[i] ==1):
        isprime =0
        print N[i]-1,1
    else:        
        for j in range(2,N[i]/2+2):
            if(N[i]%j == 0):
                isprime =0
                print N[i]-j,j
                break
        if(isprime):
            print 0,N[i]        
            

        