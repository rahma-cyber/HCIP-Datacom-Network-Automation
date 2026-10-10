# -*- coding: utf-8 -*-
"""
Lab2 - Python Data Types
Partie 1: Numerics, Strings, Lists, Tuples, Dictionaries, Sets
"""

# ==========================================
# 1. Types Numériques (Numerics)
# ==========================================
print("--- 1. Types Numerics ---")
print(True + False)  # Output: 1
print(True or False) # Output: True
print(5 // 2)        # Output: 2
print(5 % 2)         # Output: 1
print(3 ** 2)        # Output: 9
print(5 + 1.6)       # Output: 6.6
print()

# ==========================================
# 2. Chaînes de caractères (Strings)
# ==========================================
print("--- 2. Types Strings ---")
S = 'python'
print(len(S))
print(S[0], S[1], S[-1])
print(S + '1', S * 2)

# Test d'immuabilité
try:
    S[0] = 'Z'
except TypeError as e:
    print(f"Exception attendue (Immuabilite) : {e}")

S1 = 'Z' + S[1:]
print(f"S: {S}, S1: {S1}")
print(S.split('h'))
print(S.replace('py', 'PY'))
print(S.upper())
print('PYTHON'.lower())
print(''.join(['life', 'is', 'short']))
hw12 = '%s %s %d' % ('hello', 'world', 12)
print(hw12)
print()

# ==========================================
# 3. Listes (Lists)
# ==========================================
print("--- 3. Types Lists ---")
animals = ['cat', 'dog', 'monkey']
animals.append('fish')
print(animals)
animals.remove('fish')
print(animals)
animals.insert(1, 'fish')
print(animals)
animals.pop(1)
print(animals)

for i in enumerate(animals):
    print(i)

squares = [x*2 for x in animals]
print(squares)

list1 = [12, 45, 32, 55]
list1.sort()
print(list1)
list1.reverse()
print(list1)
print()

# ==========================================
# 4. Tuples
# ==========================================
print("--- 4. Types Tuples ---")
T = (1, 2, 3)
print(T + (4, 5))
tuple1 = (12, 45, 32, 55, [1, 0, 3])
try:
    tuple1[0] = "good"
except TypeError as e:
    print(f"Exception attendue (Immuabilite Tuple) : {e}")
tuple1[4][0] = 2
print(tuple1)
print()

# ==========================================
# 5. Dictionnaires (Dictionaries)
# ==========================================
print("--- 5. Types Dictionaries ---")
x = {'food': 'Spam', 'quantity': 4, 'color': 'pink'}
d = x.copy()
d['color'] = 'red'
print(x)
print(d)
print(d.get('name'))
print(d.get('name', 'The key value does not exist.'))
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))
d.clear()
print(d)
print()

# ==========================================
# 6. Ensembles (Sets)
# ==========================================
print("--- 6. Types Sets ---")
sample_set = {'Prince', 'Techs'}
print('Data' in sample_set)
sample_set.add('Data')
print(sample_set)
sample_set.remove('Data')
print(sample_set)
list2 = [1, 3, 1, 5, 3]
print(list(set(list2)))
