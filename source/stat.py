from random import randint

from source.algo import *


def moyenne_remplissage(inputs):
    first_fit_result = first_fit(inputs)
    return sum(first_fit_result) / len(first_fit_result)


def pourcentage_moyen_remplissage(inputs):
    return moyenne_remplissage(inputs) * 100 / inputs[0]


if __name__ == '__main__':
    taille_bin = int(input("Taille bin : "))
    nb_objets = int(input("Nombre d'objets : "))
    valeur_min = int(input("Valeur minimale d'un objet : "))
    valeur_max = int(input("Valeur maximale d'un objet : "))
    objets = [randint(valeur_min, valeur_max) for _ in range(nb_objets)]
    print(objets)
    print(moyenne_remplissage([taille_bin, objets]))
    print(pourcentage_moyen_remplissage([taille_bin, objets]))
