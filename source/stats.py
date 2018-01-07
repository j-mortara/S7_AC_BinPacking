#! /usr/bin/env python3

import time
from random import randint

from algo import *

csv_path = "res.csv"
names = ["execution time", "packing percent", "bin number"]


def execStats(fit_func, inputs):
    """ This function executes the given function and returns statistics on the result of the function
    :param fit_func: the function to execute
    :param inputs: the inputs to give to the function
    :return: Execution Time, Percentage of packing, Number of bins, And the function's result
    """
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
    """
    Writes the statistics to a csv file
    :param file: File to write the data on
    :param nbs_objects: a list of ids that identifies several executions
    can be empty if there is only one for each fucntion
    :param stats: the statistics it is a dictionnary with functions as keys and arrays of arrays as values
    :return:
    """
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
    """Prints the given statistics on the standard output, name corresponds to
    function's name, objets the objects given to the function
    """
    print(name)
    print("Objets : " + str(objets))
    exec_time = round(exec_time, 6)
    print("Temps d'exécution", exec_time, "s")
    print("Résultat : " + str(result))
    print("Nombre de boites", bin_number)
    print("Pourcentage de remplissage des boites", percent, "%\n")


def main():
    functions = [next_fit, first_fit, worst_fit, worst_fit_log, almost_worst_fit,
                 best_fit]  # if no example is given doRandomTests
    bin_size = int(input("Taille bin : "))
    numbers_object = list(map(int, input("nombre d'objets : ").split(" ")))
    valeur_min = int(input("Valeur minimale d'un objet : "))
    valeur_max = int(input("Valeur maximale d'un objet : "))
    doRandomTests(functions, bin_size, valeur_max, valeur_min, numbers_object)


def doRandomTests(functions, bin_size, max_value, min_value, numbers_object):
    """
    Generates random lists of objects of different sizes and executes functions on them
    :param numbers_object: a list of numbers that represent the size of the object list
    :param functions: a list of functions to execute
    :param bin_size: size of the bin
    :param max_value: maximum value of an object
    :param min_value: minimum value of an object
    :return:
    """
    every_stats = {f.__name__: [] for f in functions}
    for nb in numbers_object:
        objects = [randint(min_value, max_value) for _ in range(nb)]
        execFunctionsStats(every_stats, functions, objects, bin_size)
    with open(csv_path, "w") as file:
        writeToCSVFile(file, numbers_object, every_stats)


def execFunctionsStats(every_stats, functions, objects, bin_size):
    """ the function executes the given functions and adds their stats to every_stats dict
    :param every_stats: A dict with keys that are function and values that are arrays
    :param functions: a list of functions to execute
    :param objects: a list of numbers representing the size of an object
    :param bin_size: the size of the bins
    """
    for f in functions:
        stats = execStats(f, (bin_size, objects))
        every_stats[f.__name__].append(stats)
        printStats(f.__name__, objects, *stats)


if __name__ == '__main__':
    main()
