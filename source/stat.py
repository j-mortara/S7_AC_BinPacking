#! /usr/bin/env python3

import time
from random import randint

from source.algo import *

path = "res.csv"
names = ["execution time", "packing percent", "bin number"]


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
    file.write(";")
    nb = len(list(stats.values())[0][0])
    for n in names:
        for number in nbs_objects:
            file.write(n + " " + str(number) + ";")
    file.write("\n")
    for k, statList in stats.items():
        file.write(k + ";")
        for i in range(nb - 1):
            for stat in statList:
                file.write(str(stat[i]) + ";")
        file.write("\n")


def printStats(name, objets, exec_time, percent, bin_number, result):
    print(name)
    print("Objets générés : " + str(objets))

    exec_time = round(exec_time, 6)
    print("Temps d'exécution", exec_time, "s")
    print("Résultat : " + str(result))
    print("Nombre de boites", bin_number)
    print("Pourcentage de remplissage des boites", percent, "%\n")


def main():
    functions = [next_fit, first_fit, worst_fit, worst_fit_log, almost_worst_fit, best_fit]
    example = input("Fichier d'exemple : ")
    if example == "":
        bin_size = int(input("Taille bin : "))
        valeur_min = int(input("Valeur minimale d'un objet : "))
        valeur_max = int(input("Valeur maximale d'un objet : "))
        doRandomTests(functions, bin_size, valeur_max, valeur_min)
    else:
        bin_size, objects = get_inputs(example)
        every_stats = {f.__name__: [] for f in functions}
        execFunctions(every_stats, functions, objects, bin_size)
        with open(path, "w") as file:
            writeToCSVFile(file, [""], every_stats)


def doRandomTests(functions, taille_bin, valeur_max, valeur_min):
    every_stats = {f.__name__: [] for f in functions}
    nbs_objects = [100, 200, 500, 1000]
    for nb in nbs_objects:
        objects = [randint(valeur_min, valeur_max) for _ in range(nb)]
        execFunctions(every_stats, functions, objects, taille_bin)
    with open(path, "w") as file:
        writeToCSVFile(file, nbs_objects, every_stats)


def execFunctions(every_stats, functions, objects, bin_size):
    for f in functions:
        stats = execStats(f, (bin_size, objects))
        every_stats[f.__name__].append(stats)
        printStats(f.__name__, objects, *stats)


if __name__ == '__main__':
    main()
