# -*- coding: utf-8 -*-
"""
Created on Sun Apr 09 01:15:33 2017

@author: ps
"""

import math


def prime_gen(n):
    prime = [2,3]
    if(n>4):
        for i in range(4,n):
            isprime = 1
            for j in range(2,int(math.ceil(math.sqrt(i)))+1):
                if(i%j == 0):
                    isprime =0
                    break
            if(isprime):
                prime.append(i)
    
    return prime


TC = input()
N = [0]*TC
for i in range(TC):
    N[i] = input()
    
'''   
with open('primes.txt', 'r') as file:
    primes = []
    for line in file:
        primes.append(int(line))
'''    
max_N = max(N)

prime = prime_gen(max_N)


for i in range(TC):
    is_prime =True
    if(N[i] ==1):
        is_prime =False
        print 1,N[i]-1
    else:        
        for num in prime:
            if(N[i]%num == 0):
                is_prime =False
                print num,N[i]-num
                break
            
    if(is_prime):
        print N[i],0       
                

       