# -*- coding: utf-8 -*-
"""
Lab2 - Deep Copy vs Shallow Copy
"""
import copy

print("--- Shallow Copy vs Deep Copy ---")
# Correction ici : Ajout de la liste [1, 2, 8] après 'num'
Dict1 = {'name': 'lee', 'age': 89, 'num': [1, 2, 8]} 
Dict_copy = Dict1.copy()          # Shallow copy
Dict_dcopy = copy.deepcopy(Dict1) # Deep copy
Dict2 = Dict1                     # Simple reference

# Modification de la liste imbriquee
Dict1['num'][1] = 6

print('Dict1:', Dict1)
print('Dict_copy:', Dict_copy)
print('Dict_dcopy:', Dict_dcopy)
print('Dict2:', Dict2)
