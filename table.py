"""
    table.py
    ========

    This script prints the amount of seats for various allocation algorithms.
    It also prints the gini coefficient for each algorithm.
"""

from gini import gini
import numpy

from json import load


# gini zero is perfect equality
# gini coefficient one is maximal inequality

datasets = ["current", "afco", "droppinguk", "equality", "cambridge"]
datasets = [load(open(dataset+"_seats.json")) for dataset in datasets]

pop = load(open('population.json'))


for dataset in datasets:
    pop_per_seat = []
    for country in dataset:
        pop_per_seat.append(pop[country] / dataset[country])

    data = numpy.array(pop_per_seat, 'float64')
    print(f'{round(gini(data)*100, 2)}', end='\t')
print()


for country in pop:
    print(f'{country.capitalize()}', end='\t')
    for dataset in datasets:
        if country not in dataset:
            print(f'0', end='\t')
        else:
            print(f'{dataset[country]}', end='\t')
    print()


for dataset in datasets:
    print(sum(dataset.values()), end='\t')
