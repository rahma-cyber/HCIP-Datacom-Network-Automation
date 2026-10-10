# -*- coding: utf-8 -*-
"""
Lab2 - Programmation Orientee Objet (Classe, Encapsulation, Heritage, Polymorphisme)
"""

print("--- Programmation Orientee Objet ---")

class Dog():
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Attribut prive (Encapsulation)
        
    def get_age(self):
        return self.__age
        
    def shout(self):
        print('Dog shouts')

class Husky(Dog):
    def shout(self):
        print('woo')

class Tibetan_Mastiff(Dog):
    def shout(self):
        print('barking')

def sound(dog_instance):
    dog_instance.shout()

# Instanciation et Polymorphisme
dog1 = Husky('Larry', 3)
dog2 = Dog('Richard', 2)
dog3 = Tibetan_Mastiff('Sylvia', 4)

sound(dog1)  # Output: woo
sound(dog2)  # Output: Dog shouts
sound(dog3)  # Output: barking

print(dog1.name)
print(dog1.get_age())

# Tentative d'accès à l'attribut privé (Doit generer une exception)
try:
    print(dog1.__age)
except AttributeError as e:
    print(f"Exception attendue (Attribut Prive Protege) : {e}")
