# -*- coding: utf-8 -*-
"""
Lab2 - Structures de Controle et Boucles (if, for, while)
"""

# 1. Structure Conditionnelle (if)
print("--- 1. Structure Conditionnelle (if) ---")
def evaluer_score(score_input):
    try:
        score = float(score_input)
        if 100 >= score >= 90:
            print("Excellent")
        elif 90 > score >= 80:
            print("good")
        elif 80 > score >= 60:
            print("medium")
        elif 60 > score >= 0:
            print("bad")
        else:
            raise ValueError
    except Exception:
        print("Enter a correct score.")

evaluer_score("85")
evaluer_score("invalid_score")
print()

# 2. Boucle for (Table de multiplication)
print("--- 2. Boucle for ---")
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %2d" % (i, j, i * j), end=" \t ")
    print()
print()

# 3. Boucle while (break et continue)
print("--- 3. Boucle while ---")
i = 0
while i < 9:
    i += 1
    if i == 3:
        print("End the current loop.")
        continue
    if i == 5:
        print("End the current big loop.")
        break
    print(i)
