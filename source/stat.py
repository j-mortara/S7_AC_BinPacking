#! /usr/bin/env python3

from random import randint

from source.algo import *


def moyenne_remplissage(res):
    return sum(res) / len(res)


def pourcentage_moyen_remplissage(res, t_bin):
    return moyenne_remplissage(res) * 100 / t_bin


if __name__ == '__main__':
    taille_bin = int(input("Taille bin : "))
    nb_objets = int(input("Nombre d'objets : "))
    valeur_min = int(input("Valeur minimale d'un objet : "))
    valeur_max = int(input("Valeur maximale d'un objet : "))
    nb_simulations = int(input("Nombre de simulations : "))
    for i in range(nb_simulations):
        print("Simulation " + str(i) + " :")
        objets = [randint(valeur_min, valeur_max) for _ in range(nb_objets)]
        print("Objets générés : " + str(objets))
        liste = first_fit([taille_bin, objets])
        print("Résultat : " + str(liste))
        print("Remplissage moyen : " + str(moyenne_remplissage(liste)))
        print("Pourcentage de remplissage moyen : " + str(pourcentage_moyen_remplissage(liste, taille_bin)) + " %")
        print()
