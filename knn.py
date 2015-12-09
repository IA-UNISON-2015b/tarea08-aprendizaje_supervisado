#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = 'Luis Fernando Suarez Astiazaran'



def Clasificador(k, data, dataclass, inputs):
    
    nInputs = len(inputs)
    closest = [0 for _ in nInputs ]
    
    for i in range(nInputs):
        #calcula las distancias
        distances = sum((data - inputs[i,:]) **2, axis = 1)
        
    #identifica los vecinos mas cercanos
    indices = argsort(distances,axis=0)
    
    clases = unique(dataclass[indices[:k]])
    
    if len(clases) == 1 :
        
        closest[n] = unique(clases)
    else:
        
        counts = zeros(max(clases)+1)
        for i in range(k):
            counts[dataclass[indices[i]]] += 1
            closest[n] = max(counts)
            
    return closest
