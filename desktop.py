# This file should be in Your PC

import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import math as m


# gets measurements from database and puts them segregated in list of lists.
# every sublist contains specified measurement from all cycles
def get_data():
    # predefined list schema contains lists of specified measurement of all cycles
    list_measures = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    # predefined list with integer(number of measurement in database)  that goes +1 for every loop
    measure_number = [0]
    for i in range(20):
        measure_number.append(measure_number[0] + 1)
        measure_number.remove(measure_number[0])
        # filters database for specified measurement
        c.execute("SELECT cycle, measure, value FROM tests WHERE measure = ?", measure_number)
        # fills list_measures lists with measurements
        for row in c.fetchall():
            list_measures[i].append(row[2])
    return list_measures


# input: all the measurements in segregated form. output: average for every measurement in all cycles
def process_data(list_measures):
    list_number = 0
    average_list = []
    for i in list_measures:
        # loop deletes 2 maximum and minimum measurements to get lesser bad readings in further process
        for i in range(2):
            list_measures[list_number].remove(max(list_measures[list_number]))
            list_measures[list_number].remove(min(list_measures[list_number]))
        # gets average from lists in list_measures
        average = sum(list_measures[list_number]) / float(len(list_measures[list_number]))
        average_list.append(average)

        list_number = list_number +1
    return average_list


# converts measures and it's angle to place on X/Y axis
def measures_to_xyparams():
    # provides degree for every measure
    measure_degree = 189 / len(average_list)
    start_degree = 0
    aver_list_numb = 0
    x_list = []
    y_list = []
    # populates lists X and Y with coordinates in degrees, converted from radians
    for i in average_list:
        x_value = average_list[aver_list_numb] * m.cos(m.radians(start_degree))
        y_value = average_list[aver_list_numb] * m.sin(m.radians(start_degree))
        x_list.append(x_value)
        y_list.append(y_value)
        start_degree = start_degree + measure_degree
        aver_list_numb = aver_list_numb + 1
    return x_list, y_list


# provides data to pyplot and creates chart
def params_to_graph(x_list, y_list):
    param_list = []
    number = 0
    # loop populates pyplots required data
    for i in x_list:
        params = [0, 0, x_list[number], y_list[number]]
        param_list.append(params)
        number = number + 1
    soa = np.array(param_list)

    # creates chart
    x, y, u, v = zip(*soa)
    plt.figure()
    ax = plt.gca()
    ax.quiver(x, y, u, v, angles='xy', scale_units='xy', scale=1)
    ax.set_xlim([-40, 40])
    ax.set_ylim([-1, 30])
    plt.draw()
    plt.show()


# connect to database. Example provided
conn = sqlite3.connect('robotbase.db')
c = conn.cursor()

# main part
list_measures = get_data()
average_list = process_data(list_measures)
measures_to_xyparams()
x_list, y_list = measures_to_xyparams()
params_to_graph(x_list, y_list)

# close database
c.close()
conn.close()
