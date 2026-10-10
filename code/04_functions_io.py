# -*- coding: utf-8 -*-
"""
Lab2 - Fonctions Personnalisees et Operations I/O
"""

# 1. Fonctions avec parametres par defaut et variables
print("--- 1. Fonctions Mots-cles et Longueur Variable ---")
def hello(greeting='hello', name='world'):
    print('%s, %s!' % (greeting, name))

hello()
hello('Greetings', name='Huawei')

def test(a, b, *c, **d):
    print(a)
    print(b)
    print(c)
    print(d)

test(1, 2, 3, 4, 5, x=10, y=11)
print()

# 2. Operations I/O avec Gestionnaire de Contexte (with)
print("--- 2. Operations I/O (Fichiers) ---")
with open("text1.txt", 'w') as f:
    f.write("python file operation")

with open("text1.txt", 'r') as f:
    print(f.read())
