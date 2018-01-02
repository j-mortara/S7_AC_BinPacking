#! /usr/bin/env python3

from random import randint
import time
from source.algo import *


def execStats(fit_func, inputs):
    start = time.perf_counter()
    fit_result = fit_func(inputs)
    end = time.perf_counter()
    packing_mean = moyenne_remplissage(fit_result)
    percent_mean = pourcentage_moyen_remplissage(packing_mean, inputs[0])
    return end - start, packing_mean, percent_mean, len(fit_result), fit_result


def moyenne_remplissage(fit_result):
    return sum(fit_result) / len(fit_result)


def pourcentage_moyen_remplissage(mean, size):
    return mean * 100 / size


def printStats(fit_func):
    print(fit_func.__name__)
    print("Objets générés : " + str(objets))
    exec_time, mean, percent, bin_number, result = execStats(fit_func, [taille_bin, objets])
    print("Temps d'éxéctution", exec_time)
    print("Résultat : " + str(result))
    print("Nombre de boites", bin_number)
    print("Moyenne de remplissage des boites", mean, "ou", percent, "%\n")


if __name__ == '__main__':
    taille_bin = int(input("Taille bin : "))
    nb_objets = int(input("Nombre d'objets : "))
    valeur_min = int(input("Valeur minimale d'un objet : "))
    valeur_max = int(input("Valeur maximale d'un objet : "))
    nb_simulations = int(input("Nombre de simulations : "))
    objets = [randint(valeur_min, valeur_max) for _ in range(nb_objets)]
    printStats(next_fit)
    printStats(first_fit)
    printStats(worst_fit)
    printStats(worst_fit_log)
    printStats(almost_worst_fit)
    printStats(best_fit)
