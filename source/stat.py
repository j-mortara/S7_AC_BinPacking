#! /usr/bin/env python3

import time
from random import randint

from source.algo import *

path = "res.csv"


def execStats(fit_func, inputs):
    start = time.perf_counter()
    fit_result = fit_func(inputs)
    end = time.perf_counter()
    packing_mean = moyenne_remplissage(fit_result)
    percent_mean = pourcentage_moyen_remplissage(packing_mean, inputs[0])

    return round(end - start, 6), round(percent_mean, 6), len(fit_result), fit_result


def moyenne_remplissage(fit_result):
    return sum(fit_result) / len(fit_result)


def pourcentage_moyen_remplissage(mean, size):
    return mean * 100 / size


def writeToCSVFile(file, nbs_objects, stats):
    nb = len(list(stats.values())[0][0])
    name = ["execution time", "packing percent", "bin number"]
    file.write(";")
    for i in nbs_objects:
        file.write(str(i) + ";")
    file.write("\n")
    for i in range(nb - 1):
        for k, v in stats.items():
            file.write(k + " " + name[i] + ";")
            for stat in v:
                file.write(str(stat[i]) + ";")
            file.write("\n")


# file.write(name + ";" + ';'.join(map(str, stats)) + ";\n")


def printStats(name, objets, exec_time, percent, bin_number, result):
    print(name)
    print("Objets générés : " + str(objets))

    exec_time = round(exec_time, 6)
    print("Temps d'éxéctution", exec_time)
    print("Résultat : " + str(result))
    print("Nombre de boites", bin_number)
    print("Pourcentage de remplissage des boites", percent, "%\n")


def main():
    taille_bin = int(input("Taille bin : "))
    # nb_objects = int(input("Nombre d'objects : "))
    valeur_min = int(input("Valeur minimale d'un objet : "))
    valeur_max = int(input("Valeur maximale d'un objet : "))
    taille_bin = 100
    valeur_min = 1
    valeur_max = 100
    functions = [next_fit, first_fit, worst_fit, worst_fit_log, almost_worst_fit, best_fit]
    doRandomTests(functions, taille_bin, valeur_max, valeur_min)


def doRandomTests(functions, taille_bin, valeur_max, valeur_min):
    every_stats = {f.__name__: [] for f in functions}
    nbs_objects = [100, 200, 500, 1000, 10000]
    for nb in nbs_objects:
        objects = [randint(valeur_min, valeur_max) for _ in range(nb)]
        for f in functions:
            stats = execStats(f, (taille_bin, objects))
            every_stats[f.__name__].append(stats)
            printStats(f.__name__, objects, *stats)
        with open(path, "w") as file:
            writeToCSVFile(file, nbs_objects, every_stats)


if __name__ == '__main__':
    main()
